from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    #A Flask view to serve the welome page.
	
	values_1 = [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451]
	values_2 = [4215, 5312, 6251, 7841, 9821, 14984]
	
	values_3 = [{"name": "test_1", "tag": "#12345", "th": "13", "last_tried": "yesterday", "attempts": "5"}, {"name": "test_2", "tag": "#67890", "th": "14", "last_tried": "today", "attempts": "3"}]
	
	return render_template("index.html", values_1=values_1, values_2=values_2, values_3=values_3)

	
	
@app.route('/test')
def test():
    #A Flask view to serve the welome page.
	
	#Pull all available players into a (list?) for table - data goes right in HTML
	#Get data for chart #1
	#Get data for chart #2
	
	return render_template("charttest.html")	
	
	
