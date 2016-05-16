# -*- coding: utf-8 -*-
import sys
import MySQLdb


CLOUD_SQL_IP = '173.194.241.187'
CLOUD_SQL_USER = 'notes'
CLOUD_SQL_PASS = 'notes_password'


def main():
    db = MySQLdb.connect(host=CLOUD_SQL_IP, db='notes',
                         user=CLOUD_SQL_USER, passwd=CLOUD_SQL_PASS)
    cursor = db.cursor()

    cursor.execute('SELECT COUNT(DISTINCT user_id) FROM ops '
                   'WHERE date > (DATE_SUB(CURDATE(), '
                   'INTERVAL 1 MONTH));')
    users = cursor.fetchone()[0]
    sys.stdout.write("Number of active users: {}\n".format(users))

    cursor.execute('SELECT COUNT(*) FROM ops WHERE date > (DATE_SUB(CURDATE(), INTERVAL 1 HOUR))')
    ops = cursor.fetchone()[0]
    sys.stdout.write("Number of ops in the last hour: {}\n".format(ops))

    cursor.execute('SELECT COUNT(*) FROM ops WHERE operation = "SHRINKED"')
    ops = cursor.fetchone()[0]
    sys.stdout.write("Total shrinking ops: {}\n".format(ops))

    return 0

if __name__ == '__main__':
    sys.exit(main())