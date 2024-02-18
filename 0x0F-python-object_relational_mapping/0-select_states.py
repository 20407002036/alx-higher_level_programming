#!/usr/bin/python3

"""
__Summary for the update
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """_summary_
    This will act root file
    By Solomon Kaniaru
    """
    # Command line arguments: username, password, database name
    username, password, dbname = sys.argv[1:]

    # Connect to MySQL server
    # MySqldb provides us with an intreface to interact with the server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
