import psycopg2
from psycopg2.extras import execute_batch
import datetime
import os
from dotenv import load_dotenv

#Retrieve and set environment variables
load_dotenv()
DATABASE_HOST = os.getenv('DATBASE_HOST')
DATABASE_TABLE = os.getenv('DATABASE_TABLE')
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_PORT = os.environ['DATABASE_PORT']


class DB(object):

	#init method or constructor
	def __init__(self):
		DATABASE_URL = os.environ['DATABASE_URL']
		self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		
		#------ Local Dev
		#self.conn = psycopg2.connect(
		#host=DATABASE_HOST,
		#database=DATABASE_TABLE,
		#user=DATABASE_USER,
		#password=DATABASE_PASSWORD)
		#self.conn.set_session(autocommit=True)
	
	def __del__(self):
		self.conn.close()
	
	def getPlayersWithoutClan(self):
		cursor = self.conn.cursor()
		try:
			stmt = "SELECT * FROM player_info WHERE inClan='false'"
			cursor.execute(stmt)
			results = cursor.fetchall()
			players_from_db_dict = list()
			for player_db_record in results:
				player_info = {}
				player_info.update({'id': str(player_db_record[0])})
				player_info.update({'inClan': str(player_db_record[1])})
				player_info.update({'th': str(player_db_record[2])})
				player_info.update({'last_attempt': str(player_db_record[3])})
				player_info.update({'no_clan_detected': str(player_db_record[4])})
				player_info.update({'attempts': str(player_db_record[5])})				
				player_info.update({'banned': str(player_db_record[6])})
				players_from_db_dict.append(player_info)
				#print("player_info: " +str(player_info))
				player_info.clear
			return players_from_db_dict
		except Exception as err:
			print("Error: " +str(err))		

	def upsertPlayer(self, player_id, player_attempts, player_last_attempt):
		cursor = self.conn.cursor()
		try:
			stmt = "INSERT INTO player_info (id, attempts, last_attempt, inclan, th) VALUES (%s,%s,%s,%s,%s) ON CONFLICT(id) DO UPDATE SET attempts=excluded.attempts, last_attempt=excluded.last_attempt"
			cursor.execute(stmt, (player_id, player_attempts, player_last_attempt, 'false', '0'))
			self.conn.commit()
		except Exception as err:
			print("Error #2: " +str(err))					

			
		
			