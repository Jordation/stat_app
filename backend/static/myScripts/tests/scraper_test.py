from match_object import ScrapeOBJ


def main():
    URL = "https://www.vlr.gg/130685/loud-vs-optic-gaming-valorant-champions-2022-gf"
    data = ScrapeOBJ(URL).match
    print("stop")


if __name__ == "__main__":
    main()
