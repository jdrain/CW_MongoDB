__author__ = 'jason'

from mongoengine import connect
import mongoengine

DB_ALIAS='db_alias'

def db_connect(db):
    c = connect(db, alias='default')
    return c

def db_shutdown(db):
    mongoengine.connection.disconnect(alias=db)