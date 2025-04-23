#!/usr/bin/env python3

import os
import random

import MySQLdb


def run(cursor):
    random.seed()
    count = random.randint(10, 30)
    data = [(random.randint(1, 49), random.randint(50, 99)) for _ in range(count)]
    print('inserted')
    for t in data:
        print(t)

    cursor.execute("""DROP TABLE IF EXISTS tete;""")
    cursor.execute("""CREATE TABLE tete
                      (
                          foo int,
                          bar int
                      );""")
    cursor.executemany("""INSERT INTO tete (foo, bar)
                          VALUES (%s, %s)""", data);
    retval = cursor.execute("""SELECT foo
                               FROM tete
                               WHERE foo > %s
                               ORDER BY foo DESC;""", (25,))
    print('selected')
    for _ in range(retval):
        result = cursor.fetchone()
        print(result)


def main():
    host = os.environ['MARIADB_HOST']
    user = os.environ['MARIADB_USER']
    password = os.environ['MARIADB_PASSWORD']
    database = os.environ['MARIADB_DATABASE']

    conn = None
    try:
        conn = MySQLdb.connect(host=host, user=user, password=password, database=database)
        run(conn.cursor())
    finally:
        if conn is not None:
            conn.commit()
            conn.close()


if __name__ == '__main__':
    main()
