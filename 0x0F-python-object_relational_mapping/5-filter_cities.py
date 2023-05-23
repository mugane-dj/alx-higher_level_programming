#!/usr/bin/python3
"""This module contains a script that lists all cities from the database
hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, database=db_name)
    cur = db.cursor()
    query = """
        SELECT a.name FROM cities AS a
            INNER JOIN states AS b
            ON a.state_id = b.id
            WHERE b.name = %s
        ORDER BY a.id
    """
    cur.execute(query, [state_name])
    cities = cur.fetchall()
    print(', '.join(["{:s}".format(city[0]) for city in cities]))
    cur.close()
    db.close()
