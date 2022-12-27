from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, with_parent, aliased

from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
#from static.myScripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF

import random

# funcs to deal with random q returns for testing - idk why this took me so long to make LMFAO - dumb cunt dumb cunt dumb cunt
MAPS_NAMES = ['Ascent', 'Icebox', 'Fracture', 'Split', 'Breeze', 'Bind', 'Haven'] # pearl :^)
AGENTS_NAMES = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 
                'Jett', 'Kay/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 
                'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
X_TARGETS_NAMES = ['k', 'd', 'a', 'kast', 'adr', 'acs', 'fb', 'fd']
Y_TARGETS_NAMES = ['mapname', '']
COMPARITOR_NAMES = ['player', 'team']
def getRandomQuerey():
    return {
    'scope': {
        'all': False,
        'from_event': '',
        'from_series': '',
        'from_map': '',
        'from_player': 'Derke, yay',
    },
    'filters': {
        'on_map': 'Icebox, Bind, Haven',
        'on_agent': 'Chamber',
        'on_team': '', 
    },
    'targets': {
        'x': ['fb','fd'], 
        'y': 'player',
        'comparitor': 'player',
        'max_columns': 15
    }
}

def randMap():
    return random.choice(MAPS_NAMES)
def randAgent():
    return random.choice(AGENTS_NAMES)
def randX():
    return random.choice(X_TARGETS_NAMES)
def randY():
    return random.choice(Y_TARGETS_NAMES)
def randComparitor():
    return random.choice(COMPARITOR_NAMES)

# some helper funcs
def findEnemy(row):
    if row.team == row.team1:
        return row.team2
    else:
        return row.team1
def checkResultLen(iter):
    return sum(1 for _ in iter)

#

def fromSeries(querey, session):

    stmt = select(TBL_Stats).join(
        TBL_Map, TBL_Map.id == TBL_Stats.map_id).join(
        TBL_Match, TBL_Match.id == TBL_Map.match_id).where(
        TBL_Match.matchname == querey['scope']['from_series']).subquery()
    bundle = aliased(TBL_Stats, stmt)
    return bundle


def fromEvent(querey, session):
    stmt = select(TBL_Stats).join(
        TBL_Map, TBL_Map.id == TBL_Stats.map_id).join(
        TBL_Match, TBL_Match.id == TBL_Map.match_id).join(
        TBL_Events, TBL_Events.id == TBL_Match.event_id).where(
        TBL_Events.event == querey['scope']['from_event']).subquery()

    bundle = aliased(TBL_Stats, stmt)
    return bundle


def fromPlayer(querey, session):
    print(querey['scope']['from_player'])
    stmt = select(TBL_Stats).join(
    TBL_Map, TBL_Map.id == TBL_Stats.map_id).where(
        TBL_Stats.player.in_(querey['scope']['from_player'].split(', '))).subquery()
    bundle = aliased(TBL_Stats, stmt)
    return bundle


def bundleByScope(querey, session):
    if querey['scope']['from_event']:
        bundle = fromEvent(querey, session)
    if querey['scope']['from_series']:
        bundle = fromSeries(querey, session)
    if querey['scope']['from_player']:
        bundle = fromPlayer(querey, session)
    return bundle


def filterMap(filters, session, bundle):
    stmt = select(bundle).where(
        bundle.mapname.in_(filters['on_map'].split(', '))).subquery()
    filtered_bundle = aliased(TBL_Stats, stmt)
    return filtered_bundle
def filterAgent(filters, session, bundle):
    stmt = select(bundle).where(
    bundle.agent.in_(filters['on_agent'].split(', '))).subquery()
    filtered_bundle = aliased(TBL_Stats, stmt)
    return filtered_bundle
def filterTeam(filters, session, bundle):
    stmt  = select(bundle).where(
        bundle.team.in_(filters['on_team'].split(', '))).subquery()
    filtered_bundle = aliased(TBL_Stats, stmt)
    return filtered_bundle

def filterAll(filters, session):
    stmt = select(TBL_Stats).join(
    TBL_Map, TBL_Map.id == TBL_Stats.map_id).join(
    TBL_Match, TBL_Match.id == TBL_Map.match_id).join(
    TBL_Events, TBL_Events.id == TBL_Match.event_id).subquery()
    bundle = aliased(TBL_Stats, stmt)
    return bundle

def doFilters(filters, session, bundle):
    if not bundle:
        bundle = filterAll(filters, session)
    if filters['on_map']:
        bundle = filterMap(filters, session, bundle)
    if filters['on_agent']:
        bundle = filterAgent(filters, session, bundle)
    if filters['on_team']:
        bundle = filterTeam(filters, session, bundle)
    return bundle


def getValues(targets, session, bundled_rows):
    #if a target value is outside of TBL_Stats, perform joins on bundle to get it
    rows = select(bundled_rows).join(
        TBL_Map.winner, TBL_Map.id == bundled_rows.map_id)
    results = session.scalars(rows)
    d_vals = []
    for res in results:
        row = vars(res)
        del row['_sa_instance_state']
        d_vals.append(row)
    return d_vals



def getRows(querey, session):
    if not querey['scope']['all']:
        scope_bundled = bundleByScope(querey, session)
    else:
        scope_bundled = False
    
    bundled_rows = doFilters(querey['filters'], session, scope_bundled)

    vals = getValues(querey['targets'], session, bundled_rows)
    return vals


def processQuerey(querey):
    max_cols = int(querey['targets']['max_columns'])
    sort_target = querey['targets']['x'][0]
    
    engine = create_engine(r"sqlite:///stat_api_scripts/the_database/test_db.db", echo=True, future=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    
    vals = getRows(querey, session)

    session.close()

    
    for item in vals:
        item = dict(item)
    sorted_vals = sorted(vals, key=lambda x:x[sort_target], reverse=True)
    if len(vals) < max_cols:
        return sorted_vals
    else:
        return sorted_vals[:max_cols]


#if __name__ == '__main__':
#    processQuerey(getRandomQuerey())