#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":

    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    searched_name = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states INNER JOIN cities ON states.id = cities.state_id WHERE states.name = %s",
        (searched_name,
         ))

    rows = cur.fetchall()
    rows_length = len(rows)

    for i, row in enumerate(rows):
        print(f'{row[4]}', end='')
        if i < rows_length - 1:
            print(', ', end='')
        else:
            print()

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
