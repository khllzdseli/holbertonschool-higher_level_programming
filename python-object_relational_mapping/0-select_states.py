#!/usr/bin/python3
"""
0-select_states.py
This script lists all states from a MySQL database hbtn_0e_0_usa.
It takes 3 arguments: MySQL username, password, and database name.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

def main():
    """Connects to the database and prints all states sorted by id."""
    if len(sys.argv) != 4:
        return  # No validation required as per instructions

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=password, db=db_name,
                           charset="utf8")
    cur = conn.cursor()
    # Execute query to fetch all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
