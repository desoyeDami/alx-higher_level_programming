#!/usr/bin/python3

"""
Module that connects a Python script to a
MySQL database and retrieves data from a table.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Database connection parameters
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]  # MySQL username provided as command-line argument
    MY_PASS = sys.argv[2]  # MySQL password provided as command-line argument
    # MySQL database name provided as command-line argument
    MY_DB = sys.argv[3]

    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    # Creating a cursor object to interact with the database
    cur = db.cursor()

    # Executing a SQL query to fetch data from the 'states' table ordered by
    # 'id'
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all rows from the result set
    rows = cur.fetchall()

    # Iterating through fetched rows and printing each row
    for row in rows:
        print(row)

    # Closing the cursor to release database resources
    cur.close()

    # Closing the database connection
    db.close()
