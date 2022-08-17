from flask import Flask
from flask import render_template
from db import DB
import os

app = Flask(__name__)

@app.route('/')
def index():
    #A Flask view to serve the welome page.
	
	values_1 = [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451]
	
	#clanless = [{"name": "test_1", "tag": "#12345", "th": "13", "last_tried": "yesterday", "attempts": "5"}, {"name": "test_2", "tag": "#67890", "th": "14", "last_tried": "today", "attempts": "3"}]
	db=DB()
	clanless_bods = db.getPlayersWithoutClan()
	
	#split clanless into th13 and 14
	th13_stats = sum(x.get('th') == '13' for x in clanless_bods)
	th14_stats = sum(x.get('th') == '14' for x in clanless_bods)
	th_stats = [th13_stats, th14_stats]

	return render_template("index.html", values_1=values_1, th_stats=th_stats, clanless_bods=clanless_bods)

	
	
@app.route('/cp')
def test():
    #A Flask view to serve the welome page.
	
	#Pull all available players into a (list?) for table - data goes right in HTML
	#Get data for chart #1
	#Get data for chart #2
	
	return render_template("controlpanel.html")	
	
	
