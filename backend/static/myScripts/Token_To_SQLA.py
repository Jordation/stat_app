from Format_MatchOBJ import createToken
from event_scraper import rizzLinks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF

BASE_EVENTS = ['https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=all',
               'https://www.vlr.gg/event/matches/449/valorant-champions-2021/?series_id=all',
               'https://www.vlr.gg/event/matches/926/valorant-champions-tour-stage-1-masters-reykjav-k/?series_id=all',
               'https://www.vlr.gg/event/matches/466/valorant-champions-tour-stage-3-masters-berlin/?series_id=all',
               'https://www.vlr.gg/event/matches/1014/valorant-champions-tour-stage-2-masters-copenhagen/?series_id=all',
               'https://www.vlr.gg/event/matches/1063/champions-tour-asia-pacific-stage-2-challengers-playoffs/?series_id=2061',
               'https://www.vlr.gg/event/matches/984/champions-tour-emea-stage-2-challengers/?series_id=1931',
               'https://www.vlr.gg/event/matches/984/champions-tour-emea-stage-2-challengers/?series_id=1932',
               'https://www.vlr.gg/event/matches/800/champions-tour-north-america-stage-2-challengers/?series_id=1953',
               'https://www.vlr.gg/event/matches/800/champions-tour-north-america-stage-2-challengers/?series_id=1561',
               'https://www.vlr.gg/event/matches/884/champions-tour-asia-pacific-stage-1-challengers-playoffs/?series_id=1753',
               'https://www.vlr.gg/event/matches/799/champions-tour-north-america-stage-1-challengers/?series_id=1559',
               'https://www.vlr.gg/event/matches/799/champions-tour-north-america-stage-1-challengers/?series_id=1737',
               'https://www.vlr.gg/event/matches/854/champions-tour-stage-1-emea-challengers/?series_id=1669',
               'https://www.vlr.gg/event/matches/854/champions-tour-stage-1-emea-challengers/?series_id=1670'
               ]

class TokenGetter:
    def __init__(self, links):
        self.tokens = []
        self.getTokens(links)

    def getTokens(self, links):
        if len(links) != 1:
            self.tokens = [createToken(link) for link in links]
        else:
            self.tokens = [createToken(links[0])]


def fillAtk(data, team):
    tbl = TBL_Stats_ATK(
        player=data['Player'],
        agent=data['Agent'],
        team=team,
        acs=data['ACS'],
        k=data['Kills'],
        d=data['Deaths'],
        a=data['Assists'],
        kast=data['KAST'],
        adr=data['ADR'],
        hsp=data['Headshot %'],
        fb=data['First Bloods'],
        fd=data['First deaths']
    )
    return tbl
def fillDef(data, team):
    tbl = TBL_Stats_DEF(
        player=data['Player'],
        agent=data['Agent'],
        team=team,
        acs=data['ACS'],
        k=data['Kills'],
        d=data['Deaths'],
        a=data['Assists'],
        kast=data['KAST'],
        adr=data['ADR'],
        hsp=data['Headshot %'],
        fb=data['First Bloods'],
        fd=data['First deaths']
    )
    return tbl
def fillStat(data, team):
    tbl = TBL_Stats(
        player=data['Player'],
        agent=data['Agent'],
        team=team,
        acs=data['ACS'],
        k=data['Kills'],
        d=data['Deaths'],
        a=data['Assists'],
        kast=data['KAST'],
        adr=data['ADR'],
        hsp=data['Headshot %'],
        fb=data['First Bloods'],
        fd=data['First deaths']
    )
    return tbl


def insertIntoEvent(tokens):
    matches = insertIntoMatch(tokens)
    new_event = TBL_Events(
        event=tokens[0]['data']['match_data']['event'],
        matches_played=matches

    )
    return new_event


def insertIntoMatch(tokens):
    match_list = []
    for token in tokens:
        maps_of_match = insertIntoMap(token)

        match_list.append(TBL_Match(
            matchname=token['data']['match_data']['series'],
            bestof=token['data']['match_data']['bestof'],
            winner=token['data']['match_data']['winner'],
            maps_played=maps_of_match
            )
        )
    return match_list


def insertIntoMap(token):
    maps_list = []
    maps_played = token['data']['match_data']['maps_played']

    for i in range(1, maps_played+1):
        stat_set = insertIntoStats(token['data'][f'm{i}_data'])
        maps_list.append(TBL_Map(
            mapname=token['data'][f'm{i}_data']['map'],
            team1=token['data'][f'm{i}_data']['t1'],
            team2=token['data'][f'm{i}_data']['t2'],
            winner=token['data'][f'm{i}_data']['winner'],
            player_stats_combined=stat_set[0],
            player_stats_attack=stat_set[1],
            player_stats_defence=stat_set[2],
            comb_map=stat_set[0],
            atk_map=stat_set[1],
            def_map=stat_set[2]
            )
        )
    return maps_list


def insertIntoStats(map_data):
    team_1 = map_data['t1']
    team_2 = map_data['t2']
    t1_c = [fillStat(stat, team_1) for stat in map_data['t1_c']]
    t1_a = [fillAtk(stat, team_1) for stat in map_data['t1_a']]
    t1_d = [fillDef(stat, team_1) for stat in map_data['t1_d']]
    t2_c = [fillStat(stat, team_2) for stat in map_data['t2_c']]
    t2_a = [fillAtk(stat, team_2) for stat in map_data['t2_a']]
    t2_d = [fillDef(stat, team_2) for stat in map_data['t2_d']]

    comb_stat = t1_c + t2_c
    atk_stat = t1_a + t2_a
    def_stat = t1_d + t2_d

    return comb_stat, atk_stat, def_stat


def insertIntoDB(tokens):
    engine = create_engine("sqlite:///db/test_db.db", echo=True, future=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    event = insertIntoEvent(tokens)
    session.add(event)
    session.commit()
    session.close()
    return


def main():

    # create loop to get token set per match, not per event and commit on completion rather than a large chunk of tokens
    # wrap in a try: pass to avoid busted matches taking out an entire event

    match_urls = rizzLinks(BASE_EVENTS[15])
    tokens = TokenGetter(match_urls).tokens
    insertIntoDB(tokens)
    return


if __name__ == "__main__":
    main()
