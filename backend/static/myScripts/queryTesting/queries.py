
from statistics import median
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from .my_tables import TBL_Tourney, TBL_Match, TBL_Map, TBL_Stat

ENGINE = create_engine(r"sqlite:///static\myScripts\queryTesting\made_up_data.db", echo=True, future=True)
MAPS = ["Ascent", "Haven", "Icebox", "Breeze", "Pearl", "Bind", "Fracture"]


def getMapIDs(mapname):
    ids = []
    with Session(ENGINE) as session:
        for map_ in session.query(TBL_Map).filter(TBL_Map.mapname.ilike('%' + mapname + '%')):
            ids.append(map_.id)
    return ids


def splitResults(stmt):
    mySesh = sessionmaker(bind=ENGINE)
    session = mySesh()
    l = []
    for result in session.scalars(stmt):
        l.append(result)
    session.close()
    return l


def averageValuesOverList(values):
    l = []
    for i in values:
        l.append(median(i))
    return l


def statByMap(ids):
    stmts = []
    grouped_values = []
    for item in MAPS:
        stmts.append(select(TBL_Stat.k).where(TBL_Stat.map_id.in_(ids[item])))
    for result in stmts:
        grouped_values.append(splitResults(result))
    return grouped_values


def idsByMap():
    mySesh = sessionmaker(bind=ENGINE)
    session = mySesh()
    ids = []
    for item in MAPS:
        ids.append(getMapIDs(item))
    session.close()
    rd = {key: ids[x] for x, key in enumerate(MAPS)}
    return rd


def getMapIDz(mapname):
    ids = []
    with Session(ENGINE) as session:
        for map_ in session.query(TBL_Map).filter(TBL_Map.mapname.ilike('%' + mapname + '%')):
            ids.append(map_.id)
    return ids


def stmttest(mapname):
    print(mapname)
    l = []
    with Session(ENGINE) as session:
        stmt = select(TBL_Stat).where(TBL_Stat.map_id.in_(getMapIDz(mapname)))
        match: TBL_Stat
        for match in session.scalars(stmt):
            l.append({"id": match.id, "map_id": match.map_id, "player": match.name,
                      "k": match.k, "d": match.d, "a": match.a})
    return l


# yeah = idsByMap()
# yeah2 = statByMap(yeah)
# yeah3 = averageValuesOverList(yeah2)


# return k/results
# [avg k]
# [mname]
