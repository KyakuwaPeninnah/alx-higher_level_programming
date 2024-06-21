#!/usr/bin/python3
"""Sript that lists all states"""


import MySQLdb
import sys


if __name__ == "__main__":

    my_db = MySQLdb.connect(host="localhost",
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            port=3306)
    cur = my_db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
