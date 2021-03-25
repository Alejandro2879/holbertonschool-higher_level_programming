#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()

c.execute("SELECT * FROM states")

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)
