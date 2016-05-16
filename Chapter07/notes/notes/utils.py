# -*- coding: utf-8 -*-
import os


def on_appengine():
    return os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine')
