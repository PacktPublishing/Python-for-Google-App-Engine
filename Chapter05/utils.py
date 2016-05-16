from google.appengine.api import memcache
from models import Note

import MySQLdb

import os


class OpTypes(object):
    NOTE_CREATED = 'NCREATED'
    FILE_ADDED = 'FADDED'
    SHRINK_PERFORMED = 'SHRINKED'


def get_note_counter():
    data = memcache.get('note_count')
    if data is None:
        data = Note.query().count()
        memcache.set('note_count', data)

    return data


def inc_note_counter():
    client = memcache.Client()
    retry = 0
    while retry < 10:
        data = client.gets('note_count')
        if client.cas('note_count', data+1):
            break
        retry += 1


def get_cloudsql_db():
    db_user = os.getenv('CLOUD_SQL_USER')
    db_pass = os.getenv('CLOUD_SQL_PASS')

    if on_appengine():
        instance_id = os.getenv('CLOUD_SQL_INSTANCE_ID')
        sock = '/cloudsql/{}'.format(instance_id)
        return MySQLdb.connect(unix_socket=sock, db='notes',
                               user=db_user, passwd=db_pass)
    else:
        db_ip = os.getenv('CLOUD_SQL_IP')
        return MySQLdb.connect(host=db_ip, db='notes',
                               user=db_user, passwd=db_pass)


def on_appengine():
    return os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine')


def log_operation(user, operation_type, opdate):
    db = get_cloudsql_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO notes.ops (user_id, operation, date)'
                   ' VALUES (%s, %s, %s)',
                   (user.user_id(), operation_type, opdate))
    db.commit()
    db.close()