#!/usr/bin/python3

"""
Script to connect to a MySQL database and
fetch states whose names start with 'N'.
"""

if __name__ == "__main__":
    import sys  # Module to access command-line arguments
    import MySQLdb  # Module that provides interface for MySQL databases
    # MySQL connection parameters obtained from command-line arguments
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]  # MySQL username
    MY_PASS = sys.argv[2]  # MySQL password
    MY_DB = sys.argv[3]    # MySQL database name

    # Establish a connection to MySQL database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()  # Create a cursor object to interact with the database

    # Execute a SELECT query to retrieve rows from the 'states' table
    # where the 'name' column starts with 'N' and order by 'id' in asc order
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()  # Fetch all rows returned by the query
    for row in rows:
        print(row)  # Print each row fetched from the database

    cur.close()  # Close the cursor to release resources
    db.close()   # Close the database connection
