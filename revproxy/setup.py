#! /usr/bin/python3

import os
import re
import sys
import subprocess
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
    sql='DROP SCHEMA public CASCADE;'
    print(sql); con.execute(sql)
    sql='CREATE SCHEMA public;'
    print(sql); con.execute(sql)
    metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    table1 = Table('data', metadata, 
		  Column('id', Integer, primary_key=True),
		  Column('categorie', String),
		  Column('nom_domaine', String),
		  Column('ip', String),
		  Column('port', String))
    table2 = Table('filename', metadata, 
		  Column('id', Integer, primary_key=True),
		  Column('nom_domaine', String))
    try:
        metadata.create_all()
        for _t in metadata.tables: print('Table created: ', _t)
    except Exception as exception:
        print (exception)
    return

def push_data_from_revproxy(username, db, password):
    con = connect(username, db, password)
    metadata = sqlalchemy.MetaData(bind=con, reflect=True)
    #sql = 'DELETE FROM data';
    #con.execute(sql); print('[*] '+sql)
    L_catégorie = ['public', 'developpement', 'production']
    L_catégorie_ip = [40, 103, 102]
    for root, dirs, files in os.walk("/etc/nginx/sites-enabled/"):
        for file in files:
            try:
                filename=os.path.join(root, file);
                command = 'cat {0} | grep proxy_pass'.format(filename)
                process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                process_stdout = process.communicate()[0]
                line = process_stdout.decode('utf8').strip()
                ip=re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', line)[0]
                catégorie_ip = int(ip.split('.')[2])
                catégorie = L_catégorie[L_catégorie_ip.index(catégorie_ip)]
                p = '(.*?)http://(.*?)$'
                try:
                    m = re.findall(p, line)[0][-1].split(':')[-1][:-2]
                    port = int(m)
                except Exception as exception:
                    #print(exception)
                    port = 80
                sql = 'INSERT INTO data (categorie, nom_domaine, ip, port) VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\')'
                sql = sql.format(catégorie, file, ip, port)
                con.execute(sql); print('[*] '+sql)
                sql = 'INSERT INTO filename (nom_domaine) VALUES (\'{0}\')'
                sql = sql.format(file)
                con.execute(sql); print('[*] '+sql)
            except Exception as exception:
                #print(exception)
                continue
    return
