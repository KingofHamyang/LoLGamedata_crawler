## parser.py
import requests
import json
from bs4 import BeautifulSoup

## HTTP GET Request
f=open("summoner_list.txt")
f_result = open("data_result.csv" , 'w')



while True:
    item = f.readline()
    if not item: break
    print(item)
    req = requests.get('https://www.op.gg/summoner/userName=' + item)
    soup = BeautifulSoup(req.text , 'html.parser')
   
    #소환사별 게임 정보들

    summoner_id = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div')[0]['data-summoner-id']
    url = 'https://www.op.gg/summoner/matches/ajax/averageAndList/startInfo=0&summonerId='+ summoner_id+'&type=soloranked'
    #ajax 요청
    request_per_summoner = requests.get(url)
    summoner_solorank = request_per_summoner.text
    #print(summoner_solorank)
    if(request_per_summoner.status_code == 200):
        html2 = json.loads(summoner_solorank)
        parsed_solorank = BeautifulSoup(html2['html'],'html.parser')

        game_list = parsed_solorank.find_all("div" , {'class' : 'GameItemWrap'})
        for item2 in game_list:
            
            win_or_def = item2.find("div", {'class' : 'GameResult'}).text.strip()
            left_or_right = 0
            gammer_info = item2.find_all("div", {'class' : 'FollowPlayers Names'})
            summoners_in_each_game = gammer_info[0].find_all("a")
            used_champion = gammer_info[0].find_all("div",{'class' : 'ChampionImage'})
            data_index = []
            X1_champion_info =[]
            X2_champion_winrate = []
            X3_summoner_winrate = []
            for index in range(len(summoners_in_each_game)) :
                used_champion_name = used_champion[index].find("div").text
                if(summoners_in_each_game[index].text == item[:-1]):
                    
                    if(index > 4):
            
                        left_or_right = 1
                    else :

                        left_or_right =0

                url_champion_master = "https://www.op.gg/summoner/champions/userName=" +summoners_in_each_game[index].text
                request_champion_master = requests.get(url_champion_master)
                champion_master = BeautifulSoup(request_champion_master.text, 'html.parser')

                champion_master_name = champion_master.find_all("td", {'class' : 'ChampionName Cell'})
                champion_master_winrate = champion_master.find_all("td", {'class' : 'RatioGraph Cell'})
                champion_master_winrating_number = 0
                for index2 in range(len(champion_master_name)):
                    if(champion_master_name[index2]['data-value'] == used_champion_name):
                        champion_master_winrating_number = champion_master_winrate[index2]['data-value']
                        
                        break
                
                X1_champion_info.append(used_champion_name)
                X2_champion_winrate.append(champion_master_winrating_number)
                data_index.append(used_champion_name)
                data_index.append(champion_master_winrating_number)
                f_result.write(used_champion_name)
                f_result.write(', ')
                f_result.write(str(champion_master_winrating_number))
                f_result.write(', ')




                summoner_id_page = requests.get('https://www.op.gg/summoner/userName=' +summoners_in_each_game[index].text )
                parsed_summoner_page = BeautifulSoup(summoner_id_page.text,'html.parser')


                summoner_id_for_winrate = parsed_summoner_page.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div')[0]['data-summoner-id']




                url_summoner_recent_winrate = 'https://www.op.gg/summoner/matches/ajax/averageAndList/startInfo=0&summonerId='+ summoner_id_for_winrate+'&type=soloranked' 
                request_summoner_recent_winrate = requests.get(url_summoner_recent_winrate)

                if(request_summoner_recent_winrate.status_code == 200):
                    new_data_winrate = json.loads(request_summoner_recent_winrate.text)

                    summoner_recent_winrate = BeautifulSoup(new_data_winrate['html'] , 'html.parser')
                    winrate = summoner_recent_winrate.find_all('div', {'class' : 'WinRatioGraph'})[0].find_all('div',{'class' : 'Text'})[0].text
                    data_index.append(winrate[:-1])
                    X3_summoner_winrate.append(winrate[:-1])
                    f_result.write(winrate[:-1])
                    f_result.write(', ')
                    




            #print(X1_champion_info)
            #print(X2_champion_winrate)
           # print(X3_summoner_winrate)
            win = 0

            if(win_or_def == 'Victory' ) :
                if(left_or_right == 0) : 
                    win = 0
                else:
                    win  = 1
            elif(win_or_def == 'Defeat'):
                if(left_or_right == 0):
                    win = 1
                else:
                    win = 0
            else:
                win = 2
            #print(left_or_right )
        
            #print(win_or_def)
            print(win_or_def)
            data_index.append(win)
            f_result.write(str(win))
            f_result.write('\n')
            print(data_index)


            
        









    
