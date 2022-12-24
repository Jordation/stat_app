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
def findMatchWinner(m_d):
    if m_d['Team 1 Maps W'] > m_d['Team 2 Maps W']:
        return m_d['Team 1']
    else: 
        return m_d['Team 2']
#

def findMapWinner(t1, t2):
    t1_s, t2_s = int(t1[1]), int(t2[1])
    if t1_s > t2_s:
        return t1[0]
    else:
        return t2[0]
#

def combineStat(a_frame, d_frame):
    def doCombine(a, d):
        combined = {
            'Player': a['Player'],
            'Agent': a['Agent'],
            #'Rating': stupidfuckingratingnumber
            'ACS': (a['ACS'] + d['ACS'])//2,
            'Kills': a['Kills']+d['Kills'],
            'Deaths': a['Deaths']+d['Deaths'],
            'Assists': a['Assists']+d['Assists'],
            'KAST': (a['KAST'] + d['KAST'])//2,
            'ADR': (a['ADR']+d['ADR'])//2,
            'Headshot %': (a['Headshot %'] + d['Headshot %'])//2,
            'First Bloods': a['First Bloods']+d['First Bloods'],
            'First deaths': a['First deaths']+d['First deaths']
        }
        return combined

    l = []
    for i in range(len(a_frame)):
        l.append(doCombine(a_frame[i], d_frame[i]))

    return l
# combines the atk and def stats for each player

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
        eaDict = doEnsure(eaDict)
    return dicts

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

def splitMaps(stats, map_winner, map_name, teams):
    t1a, t1d, t2a, t2d = splitTeams(stats)
    t1c = combineStat(t1a, t1d)
    t2c = combineStat(t2a, t2d)
    d = {
        
        'map': map_name,
        'winner': map_winner,
        't1': teams[0],
        't2': teams[1],
        
        't1_a': t1a,
        't1_d': t1d,
        't1_c': t1c,
        
        't2_a': t2a,
        't2_d': t2d,
        't2_c': t2c,
    }
    return d

#
# end map funcs




# funcs to create player dicts
#

def splitTeams(stats):
    t1 = stats[:5]
    t2 = stats[5:]
    
    t1_a = [{key: x[0][i] for i, key in enumerate(CATEGORIES_PLAYERS)} for x in t1]
    t1_d = [{key: x[1][i] for i, key in enumerate(CATEGORIES_PLAYERS)} for x in t1]
    t2_a = [{key: x[0][i] for i, key in enumerate(CATEGORIES_PLAYERS)} for x in t2]
    t2_d = [{key: x[1][i] for i, key in enumerate(CATEGORIES_PLAYERS)} for x in t2]

    return ensureTypes(t1_a), ensureTypes(t1_d), ensureTypes(t2_a), ensureTypes(t2_d)

#
# end player funcs


# this is the function that does it all
def getTheStats(url):
    soup = getSoup(url)
    print(f'{url=}')
    cleaned_data = prepareSoup(soup)
    
    match_data = {key: cleaned_data[0][i] for i, key in enumerate(CATEGORIES_MATCH)}
    match_data['Maps Played'] = cleaned_data[1]
    match_data['Winner'] = findMatchWinner(match_data)
    
    token = {
        'data':{
            'match_data': {
                'event': match_data['Event Title'],
                'series': match_data['Series'],
                'bestof': match_data['Best Of'],
                'winner': match_data['Winner'],
                'maps_played': len(match_data['Maps Played']),
            }
        }        
    }

    for i in range(len(cleaned_data[3])):
        winner = findMapWinner(cleaned_data[2][i]['Team 1'], cleaned_data[2][i]['Team 2'])
        teams = [cleaned_data[0][0], cleaned_data[0][1]]
        mapname = cleaned_data[1][i]
        token['data'][f'm{i+1}_data'] = splitMaps(cleaned_data[3][i], winner, mapname, teams)
    
    return token

if __name__ == '__main__':
    token = getTheStats('https://www.hltv.org/matches/2340000/tyloo-vs-tyloo-esea-mdl-season-34-north-america')
    print(123)