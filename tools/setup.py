#! /usr/bin/python3

import os
import re
import sys
import nmap
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
import sqlalchemy_utils

def connect(user, db, password='', host='localhost', port=5432):
    '''Returns a connection (and a metadata) object'''
    # postgresql://user:password@host:port/database
    if password:
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
    else:
        url = 'postgresql://{}@/{}'
        url = url.format(user, db)
    print("\nConnexion to: "+url)
    try:
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        #meta = sqlalchemy.MetaData(bind=con, reflect=True)
        return con 
    except sqlalchemy.exc.OperationalError as exception:
        exception = str(exception).split('\n')[0]
        m = re.search('\(psycopg2.OperationalError\) FATAL:  (.*?)$', exception)
        if m: 
            print(m.group(1))
            print("You might need to edit pg_hba.conf file.")
            print("Don't forget to restart postgresql service after.")
        sys.exit(0)

def create_user(username, password):
    con = connect("postgres", "template1")
    sql = 'CREATE USER {} WITH PASSWORD \'{}\''
    sql = sql.format(username, password)
    try:
        con.execute(sql)
        print ("Role {} has been successfully created.".format(username))
    except sqlalchemy.exc.OperationalError as exception:
        print (exception)
        sys.exit(0)
    except sqlalchemy.exc.ProgrammingError as exception:
        print ("Role {} already exists, keep going...".format(username))
    return



username = 'respoweb'
password = 'MXlf55DdYmURrHDlcbnYXKiGg2O'
create_user(username, password)
