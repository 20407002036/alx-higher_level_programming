#!/usr/bin/python3
"""_summary_
    for the updated version of this
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the username, database and host from terminal
    username, password, dbname = sys.argv[1:]
    
    # Connect to the server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)
    
    # create a cursor object
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    # The like 'N% is not case sensitive
    
    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


    