#! /usr/bin/python3

import re
import sys
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
    print('\nConnexion to: '+url)
    try:
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        #meta = sqlalchemy.MetaData(bind=con, reflect=True)
        return con 
    except sqlalchemy.exc.OperationalError as exception:
        exception = str(exception).split('\n')[0]
        m = re.search('\(psycopg2.OperationalError\) FATAL:  (.*?)$', exception)
        if m: 
            print(m.group(1))
            print('You might need to edit pg_hba.conf file.')
            print('Don\'t forget to restart postgresql service after.')
        sys.exit(0)

def create_user(username, password):
    con = connect('postgres','template1')
    sql = 'CREATE USER {} WITH PASSWORD \'{}\''
    sql = sql.format(username, password)
    try:
        print(sql); con.execute(sql)
        print ('Role {} has been successfully created.'.format(username))
    except sqlalchemy.exc.OperationalError as exception:
        print (exception)
        sys.exit(0)
    except sqlalchemy.exc.ProgrammingError as exception:
        print ('Role {} already exists, keep going...'.format(username))
    return

def grant_user(username):
    con = connect('postgres', 'template1')
    sql = 'ALTER USER {} WITH SUPERUSER CREATEDB CREATEROLE REPLICATION';
    sql = sql.format(username)
    try:
        print(sql); con.execute(sql)
        print ('Role {} has been granted with SUPERUSER, CREATEDB AND REPLICATION attributes.'.format(username))
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
            print ('Database {} has been successfully created'.format(db))
        else:
            print('Database already exists, keep going...')
    except Exception as exception:
        print(exception)
    return

def create_tables(username, db, password):
    con = connect(username, db, password)
    metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    X = [ _t for _t in metadata.tables ]
    Y = ['catégories', 'plages_ip', 'résultat_scan']
    X.sort(); Y.sort()
    if X==Y: 
        print('Tables already created, keep going...'); 
        return
    else:
        sql='DROP SCHEMA public CASCADE;'
        print(sql); con.execute(sql)
        sql='CREATE SCHEMA public;'
        print(sql); con.execute(sql)
        metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    table1 = Table('catégories', metadata, 
		  Column('id', Integer, primary_key=True),
		  Column('name', String))
    table2 = Table('plages_ip', metadata,
		  Column('id', Integer, primary_key=True),
		  Column('id_catégories', Integer, ForeignKey('catégories.id'), nullable=False),
		  Column('ip_mask', String),
		  Column('description', String))
    table3 = Table('résultat_scan', metadata,
		  Column('id', Integer, primary_key=True),
		  Column('id_plages_ip', Integer, ForeignKey('plages_ip.id'), nullable=False),
		  Column('ip', String),
		  Column('nmap_csv', String))
    try:
        metadata.create_all()
        for _t in metadata.tables: print('Table created: ', _t)
    except Exception as exception:
        print (exception)
    return

def get_data_from_file(filename):
    file = open(filename, 'r')
    data = file.read().split('\n')[1:-1]
    return data

def push_categories(con, data):
    catégories=set([line.split(';')[0] for line in data])
    #{'test1', 'test2'}
    '''Optinal delete all from table catégories'''
    sql = 'DELETE FROM {}'.format('catégories')
    print(sql); con.execute(sql)
    for catégorie in catégories:
        sql = 'INSERT INTO {0} (name) SELECT \'{1}\' WHERE NOT EXISTS (SELECT * FROM {0} WHERE name=\'{1}\')';
        sql = sql.format('catégories', catégorie)
        print(sql); con.execute(sql)
    return

def push_plages_ip(con, data):
    plages=set([line.split(';')[1] for line in data])
    print(plages)
    print(plages)
    print(plages)
    return

def push_data_from_file(username, db, password, filename):
    con = connect(username, db, password)
    metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    '''get data from file'''
    data = get_data_from_file(filename)
    '''push data in tables'''
    push_categories(con, data)
    push_plages_ip(con, data)
    return

