# Authorization data
import requests
import os
from dotenv import load_dotenv

#Retrieve Environment Variables
load_dotenv()
#Set Environment Variables
CLASH_TOKEN = os.getenv('CLASH_TOKEN')

## Define header for making API calls that will hold authentication data
headersAPI = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+ CLASH_TOKEN,
}

def getPlayerStats(tag):
	url_encoded_player_tag = tag.replace('#', '%23')
	response = requests.get('https://api.clashofclans.com/v1/players/' + url_encoded_player_tag, headers=headersAPI, verify=True)
	player_info = response.json()	
	return player_info

