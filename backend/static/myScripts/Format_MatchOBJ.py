import pandas as pd
from match_object import ScrapeOBJ

URL = "https://www.vlr.gg/130685/loud-vs-optic-gaming-valorant-champions-2022-gf"

# return [pd.Series(x) for x in new_dicts]

def combineStat(a_frame, d_frame):
    def doCombine(a, d):
        combined = {
            'Player': a['Player'],
            'Agent': a['Agent'],
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


def createToken(dataOBJ: ScrapeOBJ(URL).match):
    new_token = {'data': {}}

    new_token['data']['match_data'] = {
        "event": dataOBJ.matchData["Event Title"],
        "series": dataOBJ.matchData["Series"],
        "bestof": dataOBJ.matchData["Best Of"]
    }

    for i in range(1, len(dataOBJ.maps) + 1):
        t1a, t1d, t2a, t2d = [], [], [], []

        for plyr in dataOBJ.maps[i-1].team_1_stats['atk_stats']:
            t1a.append(plyr.stats)
        for plyr in dataOBJ.maps[i-1].team_1_stats['def_stats']:
            t1d.append(plyr.stats)

        for plyr in dataOBJ.maps[i-1].team_2_stats['atk_stats']:
            t2a.append(plyr.stats)
        for plyr in dataOBJ.maps[i-1].team_2_stats['def_stats']:
            t2d.append(plyr.stats)

        new_token['data'][f"m{i}_data"] = {
            "map": dataOBJ.maps[i - 1].map_played,
            "winner": dataOBJ.maps[i - 1].map_winner,
            "t1": dataOBJ.matchData['Team 1'],
            "t2": dataOBJ.matchData['Team 2'],

            't1_a': t1a,
            't1_d': t1d,
            't1_c': combineStat(t1a, t1d),

            't2_a': t2a,
            't2_d': t2d,
            't2_c': combineStat(t2a, t2d)
        }
    return new_token
