#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It sould prevent an SQL Injection.
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=sys.argv[1],
      passwd=sys.argv[2],
      db=sys.argv[3]
    )
    new_st = sys.argv[4].replace("'", "\\")

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE '{}%' \
      ORDER BY states.id ASC".format(new_st))

    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()
    db.close()
