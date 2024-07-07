#!/usr/bin/python3

"""
MySQL query script: Connects to MySQL DB and fetches rows from 'states' table.
"""

if __name__ == "__main__":
    import sys      # OS interaction
    import MySQLdb  # MySQL connector

    # Retrieve command-line arguments
    MY_USER = sys.argv[1]   # MySQL username (provided as CLI argument)
    MY_PASS = sys.argv[2]   # MySQL password (provided as CLI argument)
    MY_DB = sys.argv[3]     # MySQL database name (provided as CLI argument)
    srch_name = sys.argv[4]  # Name to search in 'states' table (CLI argument)

    # MySQL database connection parameters
    MY_HOST = "localhost"   # Assuming MySQL server is running locally

    # Connect to MySQL database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    # Create cursor to interact with database
    cur = db.cursor()

    # Execute SELECT query to fetch rows from 'states' table where name
    # matches srch_name
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (srch_name,))

    # Fetch all rows returned by SELECT query
    rows = cur.fetchall()

    # Iterate through fetched rows and print each row
    for row in rows:
        print(row)

    # Close cursor to release database resources
    cur.close()

    # Close database connection
    db.close()
