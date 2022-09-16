import requests
from bs4 import BeautifulSoup

#cells
NUM = 0
PLAYER = 1
HRS = 2
YEAR = 3
BIRTH_DAY = 4

def get_content():
    url = "https://static.webucator.com/media/public/documents/hrleaders.html"
    req = requests.get(url)
    return req.text

def get_soup(content):
    return BeautifulSoup(content, "lxml")

def get_players(soup):
    data_cont = soup.find("tbody")
    rows = data_cont.find_all('tr')

    players = []
    for row in rows:
        hrs = int(row.find_all('td')[HRS].text)
        if hrs >= 50:
            player = row.find_all('td')[PLAYER].text
            if player not in players:
                players.append(player)
        if hrs < 50:
            pass
    return players

def main():
    content = get_content()
    soup = get_soup(content)
    players = get_players(soup)
    for i, player in enumerate(players, 1):
        print(f"{i}. {player}")

main()