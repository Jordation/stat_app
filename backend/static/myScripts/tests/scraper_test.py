from match_object import ScrapeOBJ


def main():
    URL = "https://www.vlr.gg/112325/drx-vs-optic-gaming-valorant-champions-tour-stage-2-masters-copenhagen-ubsf/?game=90652&tab=overview"
    data = ScrapeOBJ(URL).match
    print(data)


if __name__ == "__main__":
    main()
