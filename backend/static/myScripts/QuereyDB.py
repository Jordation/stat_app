from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, with_parent, aliased
#from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
from static.myScripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
import os

ZZZ = {
    'scope': {
        'all': False,
        'from_event': 'Valorant Champions 2022',
        'from_series': '',
        'from_map': '',
        'from_player': '',
    },
    'filters': {
        'on_map': 'Icebox',
        'on_agent': '',
        'on_team': '',
        'vs_team': '',   
    },
    'targets': {
        'x': 'k',
        'y': 'mapname',
        'side': 'c',
        'max_columns': 15
    }
}

# some helper funcs
def makeTitle(querey):
    return "your graph title here"

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
    stmt = select(TBL_Stats).join(
    TBL_Map, TBL_Map.id == TBL_Stats.map_id).where(
        TBL_Stats.player == querey['scope']['from_player']).subquery()
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
    vals = []
    for res in results:
        vals.append({'l': vars(res)[targets['y']], 'v': vars(res)[targets['x']]})
    return vals


def prepareForPlot():
    pass


def processQuerey(querey, session):
    if not querey['scope']['all']:
        scope_bundled = bundleByScope(querey, session)
    else:
        scope_bundled = False
    
    bundled_rows = doFilters(querey['filters'], session, scope_bundled)

    target_values = getValues(querey['targets'], session, bundled_rows)
    title = makeTitle(querey)
    return target_values



def valuesFromSTMT(stmt):
    l = [x for x in stmt.scalars()]
    if len(l) == 1:
        return l[0]
    else:
        return l


def quereyRequest(querey):
    engine = create_engine(r"sqlite:///static/myScripts/the_database/test_db.db", echo=True, future=True)
    #engine = create_engine('sqlite:///the_database/test_db.db', echo=True, future=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    vals = processQuerey(querey, session)
    sorted_vals = sorted(vals, key=lambda x:x["v"], reverse=True)
    return sorted_vals[:25]
    # result = processQuerey(querey, session)
    # vals = [{"l": x.mapname, 
    #         "v": x.k}
    #         for x in result]
    # sorted_vals = sorted(vals, key=lambda x:x["v"], reverse=True)
    # print(sorted_vals[:10])
    # session.close()
    # return sorted_vals[:10]

#if __name__ == "__main__":
#    quereyRequest(ZZZ)