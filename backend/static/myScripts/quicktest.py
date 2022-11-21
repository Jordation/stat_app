token = {
    "data": {
        "match data": {
            "Tournament": 1,
            "Match": 1,
            "Best Of": 1,
        },
        "maps played": [
            {
                "map": "map name",
                "t1_atk_stat": [[], []],
                "t1_def_stat": [[], []],

                "t2_atk_stat": [[], []],
                "t2_def_stat": [[], []]
            },
        ]
    }
}


match_data = {
    "Tournament": 1,
    "Match": 1,
    "Best Of": 1,
}

maps_played = [
    {
        "map": "map name",
        "t1_atk_stat": [[], [], [], [], []],
        "t1_def_stat": [[], [], [], [], []],

        "t2_atk_stat": [[], [], [], [], []],
        "t2_def_stat": [[], [], [], [], []]
    },
]

data = {"match data": match_data,
        "maps played": maps_played
        }




token = {
    'data': {
        'match_data': 1,
        'm1_data': 1
    }
}










def main():
    for i in range(1, 4):
        print(i)
    return


if __name__ == '__main__':
    main()