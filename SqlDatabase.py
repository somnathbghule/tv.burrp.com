import sqlite3
#CREATE TABLE epg(
#PK INTEGER PRIMARY KEY AUTOINCREMENT,
#eventId INTEGER DEFAULT 0,
#startTime INTEGER DEFAULT 0,
#duration INTEGER DEFAULT 0,
#endTime INTEGER DEFAULT 0,
#genre INTEGER DEFAULT 0,
#iso639code INTEGER DEFAULT 0,
#metaInfo TEXT DEFAULT '',
#name TEXT,
#shortDesc TEXT,
#longDesc TEXT
#);
class EPGDatabase(object):
	def __init__(self, databasename):
		self.databasename=databasename
		self.conn=sqlite3.connect(self.databasename)

	def setQuery(self, query):
		self.conn.execute(query)
		self.conn.commit();
	def close(self):
		self.conn.close()
