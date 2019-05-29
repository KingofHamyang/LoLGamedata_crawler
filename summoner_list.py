## parser.py
import requests
import json
from bs4 import BeautifulSoup

## HTTP GET Request
data = []

#top ranker6
req = requests.get('https://www.op.gg/ranking/ladder/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

summonerlist = soup.find_all("a" , {'class' : 'ranking-highest__name'})

for item in summonerlist:
    print(item.text)

summonerlist2 = soup.find_all('tr',{'class' : 'ranking-table__row'})

for item in summonerlist2:
    print(item.find('a').find('span').text)

