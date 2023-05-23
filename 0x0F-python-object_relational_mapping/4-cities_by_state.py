#!/usr/bin/python3
"""This module contains a script that lists all cities from the database
hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, database=db_name)
    cur = db.cursor()
    query = """
        SELECT a.id, a.name, b.name
        FROM cities AS a
            INNER JOIN states AS b
            ON a.state_id = b.id
        ORDER BY a.id ASC
    """
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
