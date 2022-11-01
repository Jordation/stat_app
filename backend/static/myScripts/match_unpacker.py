# from match_object import ScrapeMatch
import pandas as pd


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


# def returnDF(*args):
#     links = getLinks(list(args))
#     matches = [ScrapeMatch(x).match for x in links]
#     frames = []
#     for match in matches:
#         frames.extend(unpackMatch(match))
#     return_dataframe = stackFrames(frames)
#     return return_dataframe


def unpackAndJSON(match_object):
    frames = unpackMatch(match_object)
    df = stackFrames(frames)
    return df.to_json(orient="table")
