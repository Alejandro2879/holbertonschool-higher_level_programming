#!/usr/bin/python3
if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=sys.argv[1],
      passwd=sys.argv[2],
      db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
      "SELECT * FROM states WHERE name = '{}' \
      ORDER BY states.id ASC".format(sys.argv[4])
    )

    result = cursor.fetchall()

    for element in result:
        print(element)

    cursor.close()
    db.close()
