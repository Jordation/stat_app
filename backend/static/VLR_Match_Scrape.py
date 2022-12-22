from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field

CATEGORIES_PLAYERS = ['Player', 'Agent', 'ACS',
                      'Kills', 'Deaths', 'Assists', 'KAST',
                      'ADR', 'Headshot %', 'First Bloods',
                      'First deaths']
CATEGORIES_MAP = ['Map', 'Team 1 Stats', 'Team 2 Stats']
SHOULD_BE_INT = ['ACS', 'Kills', 'Deaths', 'Assists', 'ADR', 'First Bloods', 'First deaths', 'KAST', 'Headshot %']
# i understand objects way better now lmao idk why they are data classes
# rebuild this properly without classes
#
#
# this list is used to iterate against header_text indicies to pull the data I want,
# will have to change if the structure of this changes in their html
# MATCH_DATA_IND = [
#     5, 13,  # T1, T2
#     8, 10,  # score
#     0, 1,  # match details
# ]

# CATEGORIES_MATCH = ['Team 1', 'Team 2',
#                     'Team 1 Maps W', 'Team 2 Maps W',
#                     'Event Title', 'Series', 'Patch',
#                     'Picks/Bans', 'Best Of'] rly sad. have to change this. might find fix later
MATCH_DATA_IND = [
    5, 13,  # T1, T2
    8, 10,  # score
    0, 1, 4,  # match details
    13  # picks and bans
]

CATEGORIES_MATCH = ['Team 1', 'Team 2',
                    'Team 1 Maps W', 'Team 2 Maps W',
                    'Event Title', 'Series',
                    'Best Of']

PICK_BAN_FORMAT_BO5 = ['T1 B1', 'T2 B1',
                       'T1 P1', 'T2 P1',
                       'T1 P2', 'T2 P2',
                       'Remains']

LINK_IN = 'https://www.vlr.gg/130685/loud-vs-optic-gaming-valorant-champions-2022-gf'


# helper funcs
#

def fixMapList(maps):
    for x in range(len(maps)):
        for i in maps[x]:
            if i.isnumeric():
                maps[x] = maps[x].split(i)[0]
    return maps
# helper func because final map in series doesnt contain pick data (last remaining)
# so final map picks up match run time in string

def nlk(x):    
    return [y for y in x if y != '\n']
# soup always has new line in the contents, i kill

def checkforstupidshit(a, d): 
    return [x.replace(u'\xa0', u'0') for x in a], [x.replace(u'\xa0', u'0') for x in d]
# vlr fuckers only include rating on the combined stats line rather than a rating for atk
# it leaves behind some heinous unicode shit that I cant get rid of any other way, this func deals with that

def findRoundScore(data):  
    return [x for x in data.stripped_strings if x.isnumeric()]
# simple finds round scores

def getSoup(url):
    page = (requests.get(url)).text
    return BeautifulSoup(page, "html.parser")
# gives me soup :)

#
# end helper funcs


# soup prep funcs
#

def splitHeaderData(header_soup):
    teams_data = nlk(header_soup[1].contents)
    raw_event_series = header_soup[0].contents[1].text.split("\n")

    n = 6  # look here if something breaks lol
    event = " ".join(raw_event_series[:n]).replace("\t", "").replace("\n", "").strip()
    series = " ".join(raw_event_series[n:]).replace("\t", "").replace("\n", "").strip()

    team_names = [
        teams_data[0].text.split("[")[0].replace("\t", "").replace("\n", ""),
        teams_data[2].text.split("[")[0].replace("\t", "").replace("\n", "")
        ]
    scores_bestof = [x for x in teams_data[1].text if x.isnumeric()]
    
    return team_names[0], team_names[1], scores_bestof[0], scores_bestof[1], event, series, scores_bestof[2]

def splitPlayerStats(soup_plyrs):
    def aggregateForPlayer(row):
        player_name = [text for text in row("td", class_="mod-player")[0].stripped_strings][0]
        agent = row("td", class_="mod-agents")[0].img.attrs['title']
        
        atk_stat_vals = [str(x).split(">", 1)[1].split("<", 1)[0] for x in row("span", class_="mod-t")]
        def_stat_vals = [str(x).split(">", 1)[1].split("<", 1)[0] for x in row("span", class_="mod-ct")]
        getmethestupidfuckingrating = row("span", class_="mod-both")
        # row.contents[5]
        del atk_stat_vals[0], atk_stat_vals[4], atk_stat_vals[9]
        del def_stat_vals[0], def_stat_vals[4], def_stat_vals[9]
        
        atk_full = [player_name, agent]
        def_full = [player_name, agent]
        atk_full.extend(atk_stat_vals)
        def_full.extend(def_stat_vals)
        
        return checkforstupidshit(atk_full, def_full)

    stat_rows = soup_plyrs("tr")
    del stat_rows[0], stat_rows[5]
    
    # stat_rows[0].contents[5].contents[1].contents[1]
    return [aggregateForPlayer(x) for x in stat_rows]

#
# end of soup prep funcs


# takes in a soup, separates out the different parts of the page
# collapses the data into lists for processing 
def prepareSoup(soup):
    match_header = nlk(soup.find(class_='match-header').contents)
    match_data = splitHeaderData(match_header)
    
    maps = soup(class_='vm-stats-game')
    map_data = [nlk(y.contents) for y in maps if y.attrs['data-game-id'] != 'all']
    maps_list = fixMapList([x[0].contents[3].text.split("PICK")[0].replace("\t", "").replace("\n", "") for x in map_data])

    rounds_won = [(findRoundScore(x[0].contents[1]), findRoundScore(x[0].contents[5])) for x in map_data]
    scores = [{"Team 1": [match_data[0], x[0][0]], "Team 2": [match_data[1], x[1][2]]} for x in rounds_won]

    player_stats = [splitPlayerStats(x[3]) for x in map_data]

    return [match_data, maps_list, scores, player_stats]


# funcs to create map dics
#



#
# end map funcs




# funcs to create player dicts
#



#
# end player funcs


# this is the function that does it all
def getTheStats(url):
    soup = getSoup(url)
    cleaned_data = prepareSoup(soup)
    
    match_data = {
        'maps_played': cleaned_data[1],
        'match_data': {key: cleaned_data[0][i] for i, key in enumerate(CATEGORIES_MATCH)},
        
    }
    
    
    
    
    
    pass










class ScrapeOBJ:
    def __init__(self, url):
        print(f"active {url=}")
        self.rdy_data = SoupsPrepare(url).cleaned_data
        self.match = Match(self.rdy_data)


class SoupsPrepare:
    def __init__(self, url):
        self.soup = self.getSoup(url)
        self.cleaned_data = self.doSplit(self.soup)

    @staticmethod
    def getSoup(page_link):
        html_page = (requests.get(page_link)).text
        theSOUP = BeautifulSoup(html_page, "html.parser")
        return theSOUP

    @staticmethod
    def doSplit(soup):
        pass


@dataclass
class Match:
    data_list: list = field(default_factory=list)

    @property
    def mapsPlayed(self):
        return self.data_list[1]

    @property
    def matchData(self):
        return {key: self.data_list[0][i] for i, key in enumerate(CATEGORIES_MATCH)}
    
    @property
    def maps(self):
        return [Map(item, self.mapsPlayed[ind], self.data_list[2][ind]) for ind, item in enumerate(self.data_list[3])]


    @property
    def matchWinner(self):
        if int(self.matchData['Team 1 Maps W']) > int(self.matchData['Team 2 Maps W']):
            return self.matchData['Team 1']
        else:
            return self.matchData['Team 2']

def ensureTypes(dicts):
    def doEnsure(data_dict):
        data_dict['ACS'] = int(data_dict['ACS'])
        data_dict['Kills'] = int(data_dict['Kills'])
        data_dict['Deaths'] = int(data_dict['Deaths'])
        data_dict['Assists'] = int(data_dict['Assists'])
        data_dict['ADR'] = int(data_dict['ADR'])
        data_dict['First Bloods'] = int(data_dict['First Bloods'])
        data_dict['First deaths'] = int(data_dict['First deaths'])
        data_dict['KAST'] = int(data_dict['KAST'].split('%')[0])
        data_dict['Headshot %'] = int(data_dict['Headshot %'].split('%')[0])
        return data_dict
    for eaDict in dicts:
        eaDict = doEnsure(eaDict.stats)
    return dicts

@dataclass
class Map:
    data_list: list = field(default_factory=list)
    map_played: str = "Map Name"
    score: dict = field(default_factory=dict)

    @property
    def map_winner(self):
        t1 = self.score["Team 1"]
        t2 = self.score["Team 2"]
        result = t1[0] if int(t1[1]) > int(t2[1]) else t2[0]
        return result

    @property
    def team_1_stats(self):
        if len(self.data_list[0]) > 10:
            raise Exception("Not Configured for > or < 5 a side currently.")
        working = self.data_list[:5]
        atk_stat = [Player({key: x[0][i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in working]
        def_stat = [Player({key: x[1][i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in working]
        return {"atk_stats": ensureTypes(atk_stat), "def_stats": ensureTypes(def_stat)}

    @property
    def team_2_stats(self):
        if len(self.data_list[0]) > 10:
            raise Exception("Not Configured for > or < 5 a side currently.")
        working = self.data_list[5:]
        atk_stat = [Player({key: x[0][i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in working]
        def_stat = [Player({key: x[1][i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in working]
        return {"atk_stats": ensureTypes(atk_stat), "def_stats": ensureTypes(def_stat)}



@dataclass
class Player:
    stats: dict = field(default_factory=dict)
    
    
if __name__ == '__main__':
    getTheStats(LINK_IN)

