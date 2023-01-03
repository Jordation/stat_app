from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker

#########################################
# server side querey processing testing #

import random

MAPS_NAMES = ['Ascent', 'Icebox', 'Fracture', 'Split', 'Breeze', 'Bind', 'Haven'] # pearl :^)
AGENTS_NAMES = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 
                'Jett', 'Kay/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 
                'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
NUMBER_TARGETS = ['acs', 'k', 'd', 'a', 'kast', 'adr', 'hsp', 'fb', 'fd']
PROCESS_TARGETS = ['player', 'mapename', 'agent']
Y_OPTIONS = []
X_OPTIONS = ['k','d', 'a',]

USEQ= {
    'graph_shape': { # i think this one can eventually stay off the server and just control chartjs stuff
        'y': '',
        'x': '',
        'dataset_group_by': 'team',
        'stack_group_by': '',
    },
    'data_shape': {
        'group_effect': 'average_over', # not in-use
        'group_targets': 'team, mapname',
        'order_by': 'team'
    },
    'row_reqs': {
        'on_mapname': '',
        'on_agent': 'Sova',
        'on_team': 'Paper Rex, OpTic Gaming, DRX, FNATIC',
        'on_player': '', 
    },
    'side': 'combined',
    'col_limit': 5,
}



# funcs to deal with random q returns for testing - idk why this took me so long to make LMFAO - dumb cunt dumb cunt dumb cunt
MAPS_NAMES = ['Ascent', 'Icebox', 'Fracture', 'Split', 'Breeze', 'Bind', 'Haven'] # pearl :^)
AGENTS_NAMES = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 
                'Jett', 'Kay/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 
                'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
X_TARGETS_NAMES = ['k', 'd', 'a', 'kast', 'adr', 'acs', 'fb', 'fd']
Y_TARGETS_NAMES = ['mapname', '']
Y_COMP_TARGETS_NAMES = ['mapname', 'agent', 'team']
COMP_PROCEEZE = ['ave', 'count']

# adds up values that are integers // mostly a helper for sumNumbersFromDicts
def sumValuesWithKey(key, dicts):
    num = 0
    for d in dicts:
        num += d[key]
        
    return num


def avgValuesOverSet(len_dataset, new_data):
    for k,v in new_data.items():
        new_data[k] = v/len_dataset
        
    return new_data
    
    
def avgNumbersFromDicts(dicts):
    data = dicts['data']
    summable_rows = ['acs', 'k', 'd', 'a', 'kast', 'adr', 'hsp', 'fb', 'fd']
    averaged_dict = {}
    for key in summable_rows:
        averaged_dict[key] = sumValuesWithKey(key, data)
    dicts['data'] = dicts['data'][0] | avgValuesOverSet(len(dicts['data']), averaged_dict)
    
    return dicts
    

def makeGroupedTitle(row, targets):
    targs = targets.split(', ')
    ret = []
    for targ in targs:
        ret.append(row[targ])
        
    return ret


def averageRowsByGroup(grouped_rows):

    new_data = []
    for group in grouped_rows:
        new_data.append(avgNumbersFromDicts(group))
    
    
    return new_data


def groupRowsBy(rows, targets):
    grouped_data = []
    
    for row in rows:
        title = makeGroupedTitle(row, targets)
        if {'title': title, 'data': []} not in grouped_data:
            grouped_data.append({'title': title, 'data': []})
    
    for group in grouped_data:
        for row in rows:
            if makeGroupedTitle(row, targets) == group['title']:
                group['data'].append(row)
                
    return grouped_data


def doTransform(rows, q_transforms):
    grouped_data = groupRowsBy(rows, q_transforms['group_targets'])
    averaged_data = averageRowsByGroup(grouped_data)
    return averaged_data 
    
    
def SQLfromSplit(value, keyStr):
    retStr = ''
    for val in value.split(', '):
        retStr += " OR " + keyStr + " == \"" + val + "\""
    return '('+retStr[3:]+')' # removes first OR, so i dont need to remove the last


def SQLfromQuereyRequirements(quereyReqs, side):
    
    sql_stmt = "SELECT * FROM player_stats_" + side + " WHERE "
    filterStr = ""
    
    for key, value in quereyReqs.items():
        if value == '': # if the querey type wasnt entered 
            continue
        keyStr = str(key).split('on_')[1]                   # "SELECT * FROM player_stats_SIDE WHERE
        filterStr += (" AND " + SQLfromSplit(value, keyStr)) # combines filter type and inputs as (AND) "FILTER == "VALUE" OR "
    sql_stmt += filterStr[4:] + ';' #"SELECT * FROM player_stats_SIDE WHERE ((AND) ("FILTER == "VALUE" OR ")) - remove first and with some list slices
    
    return sql_stmt #"SELECT * FROM player_stats_SIDE WHERE (("FILTER == "VALUE" OR )"AND)


def SortRows(vals, reverse: bool, order_target_index): # sorts by each dict (x) key 'title', if reverse true, sorts with highest value first (z-a, 100-0)
    return sorted(vals, key=lambda x:x['title'][order_target_index], reverse=reverse)


def GroupRows(rows, dataset_splitter):
    grouped_dict = {}
    for row in rows:
        dataset_targ = row['title'][dataset_splitter]
        if dataset_targ not in grouped_dict:
            grouped_dict[dataset_targ] = {'dataset': dataset_targ, 'data': [row['data']]}
        else: grouped_dict[dataset_targ]['data'].append(row['data'])

    return [value for key, value in grouped_dict.items()]


def findMostCompleteSet(datasets):
    max_set_size = 0
    for x in datasets:
        set_len =  len(x['data'])
        if set_len > max_set_size:
            max_set_size = set_len
            complete_dataset = x
    return complete_dataset

def prepareDatasets(label_key, data):
    complete_dataset = findMostCompleteSet(data)

    labels = [x[label_key] for x in complete_dataset['data']]

    for group in data:
        for index, label in enumerate(labels):  # labels list is used for this logic because it was made from the most complete set 
                                                # i.e. knows MINIMUM data point amount hence can insert None values
            try:
                if group['data'][index][label_key] == label:
                    continue
                else: group['data'].insert(index, None)
            except: group['data'].insert(index, None)
        


    return {'data': data, 'labels': labels}

def findProcessOrder(processes):
    d = {}
    for index, x in enumerate(processes):
        d[x] = index
    return d

def getSession():
    engine = create_engine(r"sqlite:///stat_api_scripts/the_database/test_db.db", echo=True, future=True)
    Session = sessionmaker(bind=engine)
    return Session()
def getRowsAsDicts(session, SQL_Stmt):
    result_rows = session.execute(text(SQL_Stmt))
    return [dict(x._mapping) for x in result_rows]

def processQuerey():
    querey = USEQ
    SQL_Stmt = SQLfromQuereyRequirements(querey['row_reqs'], querey['side'])
    
    session = getSession()
    rows_as_dicts = getRowsAsDicts(session, SQL_Stmt)
    session.close()

    transformed_rows = doTransform(rows_as_dicts, querey['data_shape']) #average over, etc

    data_process_order = findProcessOrder(querey['data_shape']['group_targets'].split(', ')) # find correct index to use for dataset grouping
    dataset_target_index = data_process_order[querey['graph_shape']['dataset_group_by']]
    order_by_target_index = data_process_order[querey['data_shape']['order_by']]
    ordered_rows = SortRows(transformed_rows, False, dataset_target_index) # should order by the labels target value so a full size set can be mapped correctly
    grouped_rows = GroupRows(ordered_rows, dataset_target_index)
    
    datasets = prepareDatasets('mapname', grouped_rows)
    
    return {'data': datasets}


if __name__ == '__main__':
    processQuerey()
    