#!/usr/bin/python3
"""This module contains a script that lists all states from the database
hbtn_0e_0_usa"""
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
db = MySQLdb.connect(host='localhost', port=3306, user=username,
                     password=password, database=db_name)
cur = db.cursor()
cur.execute("SELECT id, name FROM states")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
