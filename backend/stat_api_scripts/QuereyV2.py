from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker, with_parent, aliased, Bundle

from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
#from static.myScripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF

import random
USEQ= {
        'graph_dimensions': {
            'y': 'mapname',  #randYComp()
            'x': 'k, acs, fb, hsp'
        },
        
        'transform': {
            'process': 'ave', #randProcess()
            'p_target': 'mapname, player' # needs to be able to do multiple, group by player and map i.e. kills chamber ascent 
        },
        
        'reqs': {
            'on_mapname': '',
            'on_agent': 'Chamber',
            'on_team': '',
            'on_player': 'yay, f0rsakeN, Derke', # well yeah i had to ok
        },
        'side': 'combined'
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
    ret = ""
    for targ in targs:
        ret += row[targ] + " "
        
    return ret[:-1]

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
    new_data = groupRowsBy(rows, q_transforms['p_target'])
    averaged_data = averageRowsByGroup(new_data)
    
    return averaged_data 
    


def randProcess():
    return random.choice(COMP_PROCEEZE)
def randMap():
    return random.choice(MAPS_NAMES)
def randAgent():
    return random.choice(AGENTS_NAMES)
def randX():
    return random.choice(X_TARGETS_NAMES)
def randY():
    return random.choice(Y_TARGETS_NAMES)
def randYComp():
    return random.choice(Y_COMP_TARGETS_NAMES)


def SQLfromSplit(value, keyStr):
    retStr = ''
    for val in value.split(', '):
        retStr += "OR " + keyStr + " == \"" + val + "\" "
    return retStr[3:] # removes first OR, so i dont need to remove the last

def SQLfromQuereyRequirements(quereyReqs, side):
    
    sql_stmt = "SELECT * FROM player_stats_" + side + " WHERE "
    filterStr = ""
    
    for key, value in quereyReqs.items():
        if value == '':
            continue
        keyStr = str(key).split('on_')[1]
        filterStr += ("AND " + SQLfromSplit(value, keyStr))
    sql_stmt += filterStr[4:-1] + ';'
    print(f'{sql_stmt=}')
    return sql_stmt

def SortRows(vals, reverse: bool): # sorts by each dict (x) key 'title', if reverse true, sorts with highest value first (z-a, 100-0 
    return sorted(vals, key=lambda x:x['title'], reverse=reverse)

def processQuerey(querey):

    engine = create_engine(r"sqlite:///stat_api_scripts/the_database/test_db.db", echo=True, future=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.close()
    SQL_Stmt = SQLfromQuereyRequirements(querey['reqs'], querey['side'])
    
    result_rows = session.execute(text(SQL_Stmt))
    
    rows_as_dicts = []
    for res in result_rows:
        rows_as_dicts.append(dict(res._mapping))
        
    transformed_rows = doTransform(rows_as_dicts, querey['transform'])
    
    ordered_rows = SortRows(transformed_rows, False)
    
    return {'data': transformed_rows}


if __name__ == '__main__':
    processQuerey(USEQ)
    