#!/usr/bin/python3
"""Script lists all states with a name starting with N from database
Takes three arguments:
    mysql username
    mysql password
    mysql password
    Connects to default host (localhost) and port (3306)
    """

    if __name__ == "__main__":
        from sys import argv
        import MySQLdb
        db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
        c = db.cursor()
        c.execute("""SELECT * FROM states WHERE name like "N%"\
                ORDER BY states.id ASC""")
        for row in rows:
            if row[1][0] == 'N':
                print(row)
                c.close()
                db.close()
