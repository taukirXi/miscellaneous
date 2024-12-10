# working with databaes

import sqlite3

try:
    # connecting with sqlite databaes
    con = sqlite3.connect('music.sqlite3')
    # creating a cursor
    cur = con.cursor()

    cur.execute("drop table if exists movies")
    cur.execute("CREATE TABLE Movies (title TEXT, year NUMBER, score NUMBER)")
    ans = input("Table is created....")

    cur.execute(
        """INSERT INTO Movies VALUES("the lion king", 1994, 4), ("tangled", 2010, 5), ("moana", 2016, 4)""")

    ans = input("records are inserted")
    con.commit()
    ans = input("data is saved")

    cur.execute("SELECT * FROM Movies")

    for row in cur:
        print(row)

    ans = input("updating the table")
    cur.execute("UPDATE Movies set score=3 WHERE title='the lion king' ")

    print("display the record of the asecending order")
    cur.execute("SELECT * FROM Movies ORDER BY score ASC")

    for row in cur:
        print(row)
except sqlite3.DatabaseError as e:
    print(f"error {e}")
    print(f"reverting the changes")
    con.rollback()
finally:
    cur.close()
    con.close()
