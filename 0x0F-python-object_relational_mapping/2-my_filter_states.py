#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    #Get the arguments
    # search is the value to check in the db
    username, password, dbname, search = sys.argv[1:]
    
    # Create connection to db
    # use value to check db
    db = MySQLdb.connect(host = 'localhost',
                         port = 3306,
                         user = username,
                         passwd = password,
                         db = dbname,)
    # create cursor 
    cursor = db.cursor()
    
    # The cursor will associate the command
    cursor.execute("SELECT * FROM states WHERE name=%s",(search,))
    
    #To display the contenst of the command
    rows= cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()
    