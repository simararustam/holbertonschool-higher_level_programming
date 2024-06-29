#!/usr/bin/python3
"""Get all states"""

import sys
import MySQLdb as mysql


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = mysql.connect(
        host="localhost",
        port=3306,
        user=mysql_username, 
        passwd=mysql_password, 
        db=database_name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
