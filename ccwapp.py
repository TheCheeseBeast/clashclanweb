from flask import Flask, request, jsonify, render_template
from db import DB
import os
import addons 
from datetime import datetime, timedelta


app = Flask(__name__)

#Need to tidy all code, including HTML

@app.route('/')
def index():
    #A Flask view to serve the welome page.
	

	db=DB()

	#Graph: Elibigle TH
	clanless_bods = db.getPlayersWithoutClan()
	th13_stats = sum(x.get('th') == '13' for x in clanless_bods)
	th14_stats = sum(x.get('th') == '14' for x in clanless_bods)
	th_stats = [th13_stats, th14_stats]

	print(clanless_bods)
	
	#Graph: Attempts Made
	dt_now_zerod = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
	dt_now_maxed = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)
	#dt_now_zerod = datetime.now()
	tminus0 = sum((dt_now_zerod-timedelta(days=0) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=0) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus1 = sum((dt_now_zerod-timedelta(days=1) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=1) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus2 = sum((dt_now_zerod-timedelta(days=2) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=2) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus3 = sum((dt_now_zerod-timedelta(days=3) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=3) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus4 = sum((dt_now_zerod-timedelta(days=4) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=4) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus5 = sum((dt_now_zerod-timedelta(days=5) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=5) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus6 = sum((dt_now_zerod-timedelta(days=6) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=6) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	attempts_stats = [tminus0, tminus1, tminus2, tminus3, tminus4, tminus5, tminus6]


	#preloader if this take a bit of time.....
	#https://codepen.io/RaulC/pen/KgWZjo

	#https://getbootstrap.com/docs/4.0/components/modal/
	
	#for bod in clanless_bods_data:
	#	print(clanless_bods_data[bod]['name'])
	
	#pass all player info down locally 
	#load each player stats into an object with the id as a key, that way model can launch on table button click and pull up info
	#bit overload but see how it goes
	
	#have an attempt button, to increment attempts, would need refresh?	
	test="Ajax Testing!!!"
	player_id = ""
	return render_template("index.html", attempts_stats=attempts_stats, th_stats=th_stats, clanless_bods=clanless_bods, test=test)
	
	
@app.route("/getPlayerInfo", methods=['POST', 'GET'])
def getPlayerInfo():
	player_id_bytes =  request.get_data('player_id');
	player_id = player_id_bytes.decode('utf-8')
	player_data = addons.getPlayerStats(player_id)
	print(player_data)
	return (player_data)

	
	
@app.route("/tryPlayer", methods=['POST', 'GET'])
def tryPlayer():
	#update db, attempt num and new date

	split_response  = request.get_data().decode('utf-8').split("-")
	player_attempts = split_response[0]
	player_id = split_response[1]
	
	if player_attempts == 'None':
		player_attempts = 0
	else:
		player_attempts = int(split_response[0])
	player_attempts +=1
		
		
	player_last_attempt=datetime.now().strftime("%Y-%m-%d %H:%M:%S");
	
	db=DB();
	db.upsertPlayer(player_id, player_attempts, player_last_attempt);
	
		
	#db=DB()
	clanless_bods = db.getPlayersWithoutClan()
	#Graph: Attempts Made
	dt_now_zerod = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
	dt_now_maxed = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)
	#dt_now_zerod = datetime.now()
	tminus0 = sum((dt_now_zerod-timedelta(days=0) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=0) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus1 = sum((dt_now_zerod-timedelta(days=1) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=1) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus2 = sum((dt_now_zerod-timedelta(days=2) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=2) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus3 = sum((dt_now_zerod-timedelta(days=3) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=3) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus4 = sum((dt_now_zerod-timedelta(days=4) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=4) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus5 = sum((dt_now_zerod-timedelta(days=5) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=5) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	tminus6 = sum((dt_now_zerod-timedelta(days=6) < (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S'))) and (dt_now_maxed-timedelta(days=6) > (datetime.strptime(x['last_attempt'], '%Y-%m-%d %H:%M:%S')))for x in clanless_bods)
	attempts_stats = [tminus0, tminus1, tminus2, tminus3, tminus4, tminus5, tminus6]
	
	
	hmmm = {"attempts":str(player_attempts), "lastAttempt":player_last_attempt, "attempts_stats":attempts_stats}
	print(hmmm)
	return (hmmm)
	#return "test"

	#return new date and new attemps value
	#refresh graph data??? Send updated var down with new value.... 'attempts_stats'
	#could set JS var , could be lazy and make 'attempts_stats' global, why not?
	

	
@app.route('/cp')
def test():
    #A Flask view to serve the welome page.
	
	#Pull all available players into a (list?) for table - data goes right in HTML
	#Get data for chart #1
	#Get data for chart #2
	
	return render_template("controlpanel.html")	
	
	
