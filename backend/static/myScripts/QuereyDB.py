from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
#from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
from static.myScripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF


ZZZ = {
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
        'vs_team': '',
        'x_target': 'fb',
        'y_target': 'player',
        'side_target': 'c',
    }
}

def bundleByScope(querey, session):
    
    pass

def processQuerey(querey, session):
    
    

    return 123


def valuesFromSTMT(stmt):
    l = [x for x in stmt.scalars()]
    if len(l) == 1:
        return l[0]
    else:
        return l


def quereyRequest(querey):
    engine = create_engine(r"sqlite:///static/myScripts/the_database/test_db.db", echo=True, future=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(querey)
    result = processQuerey(querey, session)

    vals = [{"l": x.mapname, 
            "v": x.k}
            for x in result]
    sorted_vals = sorted(vals, key=lambda x:x["v"], reverse=True)
    print(sorted_vals[:10])
    session.close()
    return sorted_vals[:10]