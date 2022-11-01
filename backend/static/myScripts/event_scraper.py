
from bs4 import BeautifulSoup
import requests
BASE_URL = "https://vlr.gg"


def getSoup(page_link):
    html_page = (requests.get(page_link)).text
    theSOUP = BeautifulSoup(html_page, "html.parser")
    return theSOUP


def rizzLinks(url):
    soup = getSoup(url)
    items = soup("a", class_="match-item")
    links = [(BASE_URL + x.attrs['href']) for x in items]
    return links


def gatherEventLinks():
    links = ["https://www.vlr.gg/event/matches/868/champions-tour-game-changers-asia-pacific-elite",
             "https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=all&group=all"
             ]
    return links


def getLinks(*args):
    if len(args) < 1:
        event_pages = gatherEventLinks()
    else:
        event_pages = [item for item in args[0]]

    all_links = []
    for link in event_pages:
        all_links.extend(rizzLinks(link))

    return all_links

