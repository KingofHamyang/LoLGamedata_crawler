## parser.py
import requests
import json
from bs4 import BeautifulSoup


champ_html = requests.get('https://www.op.gg/champion/statistics').text
champ_parse = BeautifulSoup(champ_html, 'html.parser')
champ_name = champ_parse.find_all("div", {'class' : 'champion-index__champion-item__name'})
for item in champ_name:
    print(item.text)
