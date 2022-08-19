from flask import Flask
from flask import render_template
from db import DB
import os
import addons 
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route('/')
def index():
    #A Flask view to serve the welome page.
	

	db=DB()

	#Graph: Elibigle TH
	clanless_bods = db.getPlayersWithoutClan()
	th13_stats = sum(x.get('th') == '13' for x in clanless_bods)
	th14_stats = sum(x.get('th') == '14' for x in clanless_bods)
	th_stats = [th13_stats, th14_stats]

	#Graph: Attempts Made
	dt_now_zerod = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
	tminus0 = sum((dt_now_zerod-timedelta(days=1) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=0) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus1 = sum((dt_now_zerod-timedelta(days=2) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=1) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus2 = sum((dt_now_zerod-timedelta(days=3) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=2) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus3 = sum((dt_now_zerod-timedelta(days=4) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=3) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus4 = sum((dt_now_zerod-timedelta(days=5) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=4) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus5 = sum((dt_now_zerod-timedelta(days=6) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=5) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus6 = sum((dt_now_zerod-timedelta(days=7) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_zerod-timedelta(days=6) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	attempts_stats = [tminus0, tminus1, tminus2, tminus3, tminus4, tminus5, tminus6]

	clanless_bods_data = {}
	for player in clanless_bods:
		player_info_from_api = addons.getPlayerStats(player['id'])
		print("waiting....")
		clanless_bods_data.update({player['id'] : player_info_from_api})

		#preloader if this take a bit of time.....
	#https://codepen.io/RaulC/pen/KgWZjo

	#https://getbootstrap.com/docs/4.0/components/modal/
	
	for bod in clanless_bods_data:
		print(clanless_bods_data[bod]['name'])
	
	#pass all player info down locally 
	#load each player stats into an object with the id as a key, that way model can launch on table button click and pull up info
	#bit overload but see how it goes
	
	#have an attempt button, to increment attempts, would need refresh?	
	test="Ajax Testing!!!"
	return render_template("index.html", attempts_stats=attempts_stats, th_stats=th_stats, clanless_bods=clanless_bods, test=test)

	
	
@app.route("/test", methods=["POST"])
def getPlayerInfo():
	print("Testing Ajax!")
	test="Ajax Testing!!!"
	return str(test)
	
@app.route('/cp')
def test():
    #A Flask view to serve the welome page.
	
	#Pull all available players into a (list?) for table - data goes right in HTML
	#Get data for chart #1
	#Get data for chart #2
	
	return render_template("controlpanel.html")	
	
	
