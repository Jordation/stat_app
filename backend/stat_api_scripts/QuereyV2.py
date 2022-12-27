from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, with_parent, aliased

#from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
#from static.myScripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF

import random

# funcs to deal with random q returns for testing - idk why this took me so long to make LMFAO - dumb cunt dumb cunt dumb cunt
MAPS_NAMES = ['Ascent', 'Icebox', 'Fracture', 'Split', 'Breeze', 'Bind', 'Haven'] # pearl :^)
AGENTS_NAMES = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 
                'Jett', 'Kay/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 
                'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
X_TARGETS_NAMES = ['k', 'd', 'a', 'kast', 'adr', 'acs', 'fb', 'fd']
Y_TARGETS_NAMES = ['mapname']
COMPARITOR_NAMES = ['player', 'team']
def getRandomQuerey():
    return {
    'scope': {
        'all': '',
        'from_event': '',
        'from_series': '',
        'from_map': '',
        'from_player': 'Derke, yay',
    },
    'filters': {
        'on_map': 'Icebox',
        'on_agent': 'Chamber',
        'on_team': '', 
    },
    'targets': {
        'x': randX(),
        'y': randY(),
        'comparitor': randComparitor(),
        'max_columns': random.randint(5, 10)
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


def processQuerey(querey):
    engine = create_engine(r"sqlite:///static/myScripts/the_database/test_db.db", echo=True, future=True)
    #engine = create_engine('sqlite:///the_database/test_db.db', echo=True, future=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    print(querey)
    #vals = processQuerey(querey, session)
    session.close()
    return


if __name__ == '__main__':
    processQuerey(getRandomQuerey())