#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported"""
import MySQLdb
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Invalid number of arguments !")
        exit()

    user, password, db_name = arguments

    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=user,
            password=password,
            db=db_name,
            port=3306
        )
    except Exception as e:
        print("Can't connect to the database:", e)
        exit()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    cursor.close()
    db_connection.close()
