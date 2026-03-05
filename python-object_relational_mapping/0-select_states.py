#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported"""
import MySQLdb
import sys

if __name__ == "__main__":

    i = 0
    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Invalid number of arguments !")
        exit()

    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=arguments[0],
            password=arguments[1],
            db=arguments[2],
            port=3306
        )
    except Exception as e:
        print("Can't connect to the database :", e)
        exit()

    cursor = db_connection.cursor()
    states_num = cursor.execute("SELECT * FROM states ORDER BY states.id")
    while i < states_num:
        m = cursor.fetchone()
        print(m)
        i += 1

    cursor.close()
    db_connection.close()
