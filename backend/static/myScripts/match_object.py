
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field

CATEGORIES_PLAYERS = ['Player', 'Team', 'Agent', 'ACS',
                      'Kills', 'Deaths', 'Assists', 'KAST',
                      'ADR', 'Headshot %', 'First Bloods',
                      'First deaths']
CATEGORIES_MAP = ['Map', 'Team 1 Stats', 'Team 2 Stats']

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


def nlk(x):
    return [y for y in x if y != '\n']


class ScrapeMatch:
    def __init__(self, url):
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
        def splitHeaderData(header_soup):
            teams_data = nlk(header_soup[1].contents)
            raw_event_series = header_soup[0].contents[1].text.split("\n")

            n = 6  # yeah, this might be fucked but all good
            event = " ".join(raw_event_series[:n]).replace("\t", "").replace("\n", "").strip()
            series = " ".join(raw_event_series[n:]).replace("\t", "").replace("\n", "").strip()
            team_names = [teams_data[0].text.split("[")[0].replace("\t", "").replace("\n", ""),
                          teams_data[2].text.split("[")[0].replace("\t", "").replace("\n", "")]
            scores_bestof = [x for x in teams_data[1].text if x.isnumeric()]
            return team_names[0], team_names[1], scores_bestof[0], scores_bestof[1], event, series, scores_bestof[2]

        def splitPlayerStats(soup_plyrs):
            def aggregateForPlayer(row):
                player_N_team_data = [text for text in row("td", class_="mod-player")[0].stripped_strings]
                agent = row("td", class_="mod-agents")[0].img.attrs['title']
                stat_nums = [str(x).split(">", 1)[1].split("<", 1)[0] for x in row("span", class_="mod-both")]
                stat_nums.pop(4)
                stat_nums.pop(9)
                ret_list = [player_N_team_data[0], player_N_team_data[1], agent]
                ret_list.extend(stat_nums)
                return ret_list
#
            stat_rows = soup_plyrs("tr")
            stat_rows.pop(0)
            stat_rows.pop(5)
            return_data = [aggregateForPlayer(x) for x in stat_rows]
            return return_data

        def findRoundScore(data):
            return [x for x in data.stripped_strings if x.isnumeric()]

        match_header = nlk(soup.find(class_='match-header').contents)
        maps = soup(class_='vm-stats-game')
        map_data = [nlk(y.contents) for y in maps if y.attrs['data-game-id'] != 'all']

        player_stats = [splitPlayerStats(x[3]) for x in map_data]
        match_data = splitHeaderData(match_header)
        # other stat blocks in map list shit
        maps_list = [x[0].contents[3].text.split("PICK")[0].replace("\t", "").replace("\n", "") for x in map_data]
        rounds_won = [(findRoundScore(x[0].contents[1]), findRoundScore(x[0].contents[5])) for x in map_data]
        scores = [{"Team 1": [match_data[0], x[0][0]], "Team 2": [match_data[1], x[1][2]]} for x in rounds_won]
        return [match_data, maps_list, scores, player_stats]


@dataclass
class Match:
    data_list: list = field(default_factory=list)

    @property
    def mapsPlayed(self):
        return self.data_list[1]

    @property
    def maps(self):
        return [Map(item, self.mapsPlayed[ind], self.data_list[2][ind]) for ind, item in enumerate(self.data_list[3])]

    @property
    def matchData(self):
        return {key: self.data_list[0][i] for i, key in enumerate(CATEGORIES_MATCH)}


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
        if len(self.data_list) > 10:
            raise Exception("Not Configured for > or < 5 a side currently.")
        return [Player({key: x[i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in self.data_list[:5]]

    @property
    def team_2_stats(self):
        if len(self.data_list) > 10:
            raise Exception("Not Configured for > or < 5 a side currently.")
        return [Player({key: x[i] for i, key in enumerate(CATEGORIES_PLAYERS)}) for x in self.data_list[5:]]


@dataclass
class Player:
    stats: dict = field(default_factory=dict)

