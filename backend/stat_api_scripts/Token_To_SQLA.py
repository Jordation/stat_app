
# from event_scraper import rizzLinks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF

# from VLR_Match_Scrape import getTheStats

from stat_api_scripts.event_scraper import rizzLinks
from stat_api_scripts.SQLA_Schema import TBL_Events, TBL_Match, TBL_Map, TBL_Stats, TBL_Stats_ATK, TBL_Stats_DEF
from stat_api_scripts.VLR_Match_Scrape import getTheStats

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
    link = 'https://www.vlr.gg/event/matches/1169/red-bull-home-ground-3/?series_id=2267'
    match_urls = rizzLinks(link)
    tokens = []
    for url in match_urls:
        try:
            tokens.append(getTheStats(url))
        except:
            print("url failed")
    # insertIntoDB(tokens)
    return


if __name__ == "__main__":
    main()
