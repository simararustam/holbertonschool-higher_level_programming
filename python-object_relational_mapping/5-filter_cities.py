#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities
                JOIN states ON states.id = cities.state_id
                WHERE BINARY states.name = %s AND states.name IS NOT NULL
                ORDER BY cities.id;""".format(state_name), (state_name,))
    result = cur.fetchall()

    for x in result:
        print(x[0], end=", " if x != result[-1] else "")
    print()

    cur.close()
    db.close()
