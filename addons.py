# Authorization data
import requests
import os
from dotenv import load_dotenv

#Retrieve Environment Variables
load_dotenv()
#Set Environment Variables
CLASH_TOKEN = os.getenv('CLASH_TOKEN')
FIXIE_URL = os.getenv('FIXIE_URL')

proxyDict = {
              "http"  : os.environ.get('FIXIE_URL', ''),
              "https" : os.environ.get('FIXIE_URL', '')
            }


## Define header for making API calls that will hold authentication data
headersAPI = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+ str(CLASH_TOKEN),
}

def getPlayerStats(tag):
	url_encoded_player_tag = tag.replace('#', '%23')
	response = requests.get('https://api.clashofclans.com/v1/players/' + url_encoded_player_tag, headers=headersAPI, verify=True, proxies=proxyDict)
	player_info = response.json()	
	print("Player Info:")	
	print(player_info)
	player_name = player_info['name']
	player_th=player_info['townHallLevel']
	player_war_stars = player_info['warStars']
	all_player_heroes=player_info['heroes']
	player_heroes={}
	for hero in all_player_heroes:
		if (hero.get('village') == 'home'):
			if (hero.get('name') == 'Barbarian King'):
				print("BK level: " +str(hero.get('level')))
				player_heroes['bk'] = hero['level']
			elif (hero.get('name') == 'Archer Queen'):
				player_heroes['aq'] = hero['level']
			elif (hero.get('name') == 'Grand Warden'):
				player_heroes['gw'] = hero['level']
			elif (hero.get('name') == 'Royal Champion'):
				player_heroes['rc'] = hero['level']
	
	mini_player = {"name" : player_name, "th": player_th, "war_stars": player_war_stars, "heroes": player_heroes}
		
	return mini_player

