
from event_scraper import rizzLinks
from VLR_Match_Scrape import getTheStats
def main():
    URL = "https://www.vlr.gg/event/matches/1169/red-bull-home-ground-3/?series_id=2267"
    matches = rizzLinks(URL)

    data = []
    for match in matches:
        try:
            data.append(getTheStats(match))
        except:
            print("error at current url")
    print(data)


if __name__ == "__main__":
    main()
