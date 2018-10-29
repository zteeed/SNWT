#! /usr/bin/python3

import sys
import os
import nmap
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists, create_database

class Database():

    def __init__(self):
        self.nmap = nmap.PortScanner()

    def connect(user, password, db, host='localhost', port=5432):
        '''Returns a connection and a metadata object'''
        # postgresql://user:password@host:port/database
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
        #print(url)
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)
        return con, meta
    
    def create_db(user, password, db, host='localhost', port=5432):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
        con = sqlalchemy.create_engine(url)
        if not database_exists(con.url):
            create_database(con.url)
        return

    def create_tables(self):
        return

url = 'postgresql://{}@{}:{}/{}'
url = url.format("postgres", "localhost", 5432, "template1")
con = sqlalchemy.create_engine(url)

"""
cat /ets/hosts
192.168.104.11 hosting_db


MXlf55DdYmURrHDlcbnYXKiGg2O

create role respoweb with login;
"""
