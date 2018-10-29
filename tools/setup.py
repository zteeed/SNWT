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

def grant_user(username):
    con = connect("postgres", "template1")
    sql = 'ALTER USER {} WITH SUPERUSER CREATEDB CREATEROLE REPLICATION';
    sql = sql.format(username)
    try:
        con.execute(sql)
        print ("Role {} has been granted with SUPERUSER, CREATEDB AND REPLICATION attributes.".format(username))
    except sqlalchemy.exc.OperationalError as exception:
        print (exception)
        sys.exit(0)
    except sqlalchemy.exc.ProgrammingError as exception:
        print (exception)
        sys.exit(0)
    return

def create_database(username, db, password):
    con = connect(username, db, password)
    try:
        if not sqlalchemy_utils.database_exists(con.url):
            sqlalchemy_utils.create_database(con.url)
            print ("Database {} has been successfully created".format(db))
        else:
            print("Database already exists, keep going...")
    except Exception as exception:
        print(exception)
    return

def create_tables(username, db, password):
    con = connect(username, db, password)
    metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    print (metadata.tables)
    table1 = Table('catégories', metadata, 
		  Column('id', Integer, primary_key=True),
		  Column('name', String))
    table2 = Table('plages_ip', metadata,
		  Column('id', Integer, primary_key=True),
		  Column('id_catégories', Integer, ForeignKey("catégories.id"), nullable=False),
		  Column('IP/mask', String))
    table3 = Table('résultat_scan', metadata,
		  Column('id', Integer, primary_key=True),
		  Column('id_plages_ip', Integer, ForeignKey("plages_ip.id"), nullable=False),
		  Column('IP', String),
		  Column('nmap_csv', String))
    try:
        metadata.create_all()
        for _t in metadata.tables: print("Table created: ", _t)
    except Exception as exception:
        print (exception)
    return

username = 'respoweb'
password = 'MXlf55DdYmURrHDlcbnYXKiGg2O'
db = 'nmap'
create_user(username, password)
grant_user(username)
create_database(username, db, password)
create_tables(username, db, password)
