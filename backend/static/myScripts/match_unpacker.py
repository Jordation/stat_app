from match_object import ScrapeOBJ
import pandas as pd

URL = "https://www.vlr.gg/157703/team-heretics-vs-bleed-valorant-india-invitational-by-galaxy-racer-sf/?game=104329&tab=overview"


def unpackMatch(matchOBJ):
    new_dicts = []
    match_values = {"Event": matchOBJ.matchData["Event Title"],
                    "Series": matchOBJ.matchData["Series"],
                    "BO": matchOBJ.matchData["Best Of"]}

    for _map in matchOBJ.maps:
        map_values = {"Map": _map.map_played,
                      "Winner": _map.map_winner}

        for plyr in _map.team_1_stats:
            new_dicts.append(plyr.stats | map_values | match_values |
                             {"Team": matchOBJ.matchData["Team 1"]})

        for plyr in _map.team_2_stats:
            new_dicts.append(plyr.stats | map_values | match_values |
                             {"Team": matchOBJ.matchData["Team 2"]})

    return [pd.Series(x) for x in new_dicts]


def stackFrames(stacked_frames):
    player_stat_df = pd.concat(stacked_frames, axis=1)
    return player_stat_df

# hello jordan of another day, you may want to leave this as individual series or split the maps into their own dfs
# to later be spat into your sqlite db where you can iterate over it as nessesary 

# last time the note to future me was great, so here's another
# when(if) i implement riot api i can  use pandas features to do most of the formatting of my data since
# I can look at it round by round.
# So, it'll be worth learning in greater depth :)


def unpackAndJSON(match_object):
    frames = unpackMatch(match_object)
    df = stackFrames(frames)
    return df.to_json(orient="table")




def main():
    data_set = ScrapeOBJ(URL).match

    pass


if __name__ == '__main__':
    main()
