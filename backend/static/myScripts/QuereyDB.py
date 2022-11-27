from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF




# TODO figure out how im going to use joins to easily deal with grouping results of child to their parent without going through the extra steps

def matchesFromEvent():
    pass

def mapsFromMatch():
    pass

def statsFromMap(**kwargs):
    if kwargs['atk']:
        pass
    if kwargs['def']:
        pass
    if kwargs['all']:
        pass
    pass
