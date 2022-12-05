from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF


QUEREY = {
    'scope': {
        'all': False,
        'from_event': '',
        'from_series': '',
        'from_map': '',
        'from_player': 'yay',
    },
    'filters': {
        'on_map': '',
        'on_agent': 'Chamber',
        'on_team': '',
        'x_target': 'fb',
        'y_target': 'player',
        'side_target': 'c',
    }
}

def mapIDsFromSeries(scope, sesison):

    get_series_id_stmt = select(TBL_Match.id).where(TBL_Match.matchname == scope['from_series'])
    series_id = valuesFromSTMT(sesison.execute(get_series_id_stmt))

    get_map_ids_stmt = select(TBL_Map.id).where(TBL_Map.match_id == series_id)
    map_ids = valuesFromSTMT(sesison.execute(get_map_ids_stmt))

    return map_ids


def mapIDsFromEvent(scope, session):

    get_event_id_stmt = select(TBL_Events.id).where(TBL_Events.event == scope['from_event'])
    event_id = valuesFromSTMT(session.execute(get_event_id_stmt))
    get_match_ids_stmt = select(TBL_Match.id).where(TBL_Match.event_id == event_id)
    match_ids = valuesFromSTMT(session.execute(get_match_ids_stmt))

    get_map_ids_stmt = select(TBL_Map.id).where(TBL_Map.id.in_(match_ids))
    map_ids = valuesFromSTMT(session.execute(get_map_ids_stmt))

    return map_ids


def getAllMaps(session):

    get_map_ids_stmt = select(TBL_Map.id)
    map_ids = valuesFromSTMT(session.execute(get_map_ids_stmt))

    return map_ids


def mapIDsFromMapName(scope, session):

    get_map_ids_stmt = select(TBL_Map.id).where(TBL_Map.mapname == scope['from_map'])
    map_ids = valuesFromSTMT(session.execute(get_map_ids_stmt))

    return map_ids


def findEntry(scope, session):

    map_id_set = []
    if scope['all']:
        map_id_set = getAllMaps(session)
    if scope['from_event']:
        map_id_set = mapIDsFromEvent(scope, session)
    if scope['from_series']:
        map_id_set = mapIDsFromSeries(scope, session)
    if scope['from_map']:
        map_id_set = mapIDsFromMapName(scope, session)

    return map_id_set


def doFilters(filters, session):



    pass


def processQuerey(querey, session):

    if querey['scope']['from_player']:  # findEntry not needed if user only requests stats of 1 player.
        if querey['filters']['side_target'] == 'c':
            get_stats_stmt = select(TBL_Stats).where(TBL_Stats.player == querey['scope']['from_player'])
        if querey['filters']['side_target'] == 'd':
            get_stats_stmt = select(TBL_Stats_DEF).where(TBL_Stats_DEF.player == querey['scope']['from_player'])
        if querey['filters']['side_target'] == 'a':
            get_stats_stmt = select(TBL_Stats_ATK).where(TBL_Stats_ATK.player == querey['scope']['from_player'])
        stat_set = valuesFromSTMT(session.execute(get_stats_stmt))
    else:
        map_ids_set = findEntry(querey['scope'], session)

    return stat_set


def valuesFromSTMT(stmt):
    l = [x for x in stmt.scalars()]
    if len(l) == 1:
        return l[0]
    else:
        return l


def mapsFromMatches(matches, session):
    stmt = select(TBL_Map.id).where(TBL_Map.match_id.in_(matches))
    result = valuesFromSTMT(session.execute(stmt))
    return result

def filterByOnMap(mapname, session, map_ids):
    stmt = select(TBL_Map.id).where(TBL_Map.id.in_(map_ids)).where(TBL_Map.mapname == mapname)
    result = valuesFromSTMT(session.execute(stmt))
    return result


def main():
    engine = create_engine("sqlite:///db/test_db.db", echo=True, future=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = processQuerey(QUEREY, session)
    for x in result:
        print(f'{x.k=}, {x.agent=}, {x.player=}')




    session.close()
    return result


if __name__ == '__main__':
    main()
