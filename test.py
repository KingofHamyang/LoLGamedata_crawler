import requests
import json,ast
from bs4 import BeautifulSoup

data = []

req = requests.get("https://www.op.gg/summoner/champions/userName=타+잔")

html = req.text
soup = BeautifulSoup(html, 'html.parser')

summonerlist = soup.find_all("td", {'class' : 'ChampionName Cell'})
summonerlist2 = soup.find_all("td", {'class' : 'RatioGraph Cell'})


for item in range(len(summonerlist)):
    print(summonerlist[item]['data-value'])
    print(summonerlist2[item]['data-value'])









