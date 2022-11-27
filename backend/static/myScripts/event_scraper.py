
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

