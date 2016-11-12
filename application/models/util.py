from application.config import *
from peewee import *

def getDB (dbName):
  dbPath = config.databases[dbName].filename
  # print "DB Name: {0}\nDB Path: {1}".format(dbName, dbPath)
  theDB = SqliteDatabase (dbPath,
                          pragmas = ( ('busy_timeout',  100),
                                      ('journal_mode', 'WAL')
                                  ),
                          threadlocals = True)
  config.databases[dbName].theDB = theDB
  return theDB
  