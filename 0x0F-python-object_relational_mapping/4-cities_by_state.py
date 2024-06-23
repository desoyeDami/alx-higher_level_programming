#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":

    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[2]}', '{row[4]}')")
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
