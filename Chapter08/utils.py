from google.appengine.api import memcache
from models import Note
import os


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


def on_appengine():
    return os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine')


def get_notification_client_id(user):
    return 'notify-' + user.user_id()
