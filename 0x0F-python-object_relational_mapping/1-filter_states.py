#!/usr/bin/python3
"""This module contains a script that lists all states from the database
hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, database=db_name)
    cur = db.cursor()
    query = """
    SELECT id, name FROM states WHERE states.name
    LIKE 'N%' ORDER BY states.id ASC
    """
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
