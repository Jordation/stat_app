from match_object import ScrapeOBJ
from event_scraper import rizzLinks

def main():
    URL = "https://www.vlr.gg/event/matches/353/valorant-champions-tour-stage-2-masters-reykjav-k/?series_id=all"
    matches = rizzLinks(URL)

    data = []
    for match in matches:
        data.append(ScrapeOBJ(match).match)
    print(data)


if __name__ == "__main__":
    main()
