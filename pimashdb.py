#!/usr/bin/python

import sqlite3
import time

class PimashDB:
	def __init__(self):
		self.db = sqlite3.connect('./db/templog.db')
		self.db.row_factory = sqlite3.Row    # Required in order to access Row values by name rather than index
		self.tablename = "brew_" + time.strftime("%Y_%m_%d_%H_%M")
		print("Using table: " + self.tablename)
		self.db.execute("CREATE TABLE " + self.tablename + " (timestamp DATETIME, temp NUMERIC, state TEXT)")

	def log_temp (self, state, temp):
	    # sql to insert the temperature
	    self.db.execute("INSERT INTO " + self.tablename + " values(time('now'), (?), (?))", (temp, state))
	    # commit the changes
	    self.db.commit()

	def get_log(self):
		log = [["Timestamp", "Temperature"]]
		for row in self.db.execute("select timestamp, temp from " + self.tablename):
			log.append([row["timestamp"], row["temp"]])
		return log

	def close(self):
		self.conn.close()
