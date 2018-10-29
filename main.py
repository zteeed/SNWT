#! /usr/bin/python3

import sys
import os
import nmap
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists, create_database

class SCAN():

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

class nmap_scan():
    def x():
        return

url = 'postgresql://{}@{}:{}/{}'
url = url.format("postgres", "localhost", 5432, "template1")
con = sqlalchemy.create_engine(url)

"""
cat /ets/hosts
192.168.104.11 hosting_db


MXlf55DdYmURrHDlcbnYXKiGg2O

create role respoweb with login;

\password respoweb
GRANT SELECT, INSERT, UPDATE, DELETE
ON ALL TABLES IN SCHEMA public 
TO respoweb;

create database nmap

https://xael.org/pages/python-nmap-en.html

ALTER USER myuser WITH SUPERUSER;

      SUPERUSER | NOSUPERUSER
          | CREATEDB | NOCREATEDB

#con.execute("\l")
#if not database_exists(con.url):
#    create_database(con.url)

#DB=nmap_db()
"""
"""
production:                                 157.159.40.0/25
développement:                              157.159.40.128/26
adhérents:
filaire U1                  VLAN 41         157.159.41.0/24
filaire U2                  VLAN 42         157.159.42.0/24
filaire U3                  VLAN 43         157.159.43.0/24
filaire U4                  VLAN 44         157.159.44.0/24
filaire U5                  VLAN 45         157.159.45.0/24
filaire U6                  VLAN 46         157.159.46.0/24
filaire foyer               VLAN 47         157.159.47.0/24
filaire U7 (étages 1/2/3)   VLAN 48         157.159.48.0/24
filaire U7 (étages 4/5/6)   VLAN 49         157.159.49.0/24
"""

"""
nm = nmap.PortScanner()
for ip_mask in ["157.159.45.0/24"]:
    result = nm.scan(hosts=ip_mask, arguments='-T5')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print ('port : %s\tstate : %s\tname : %s' 
                       % (port, 
                          nm[host][proto][port]['state'], 
                          nm[host][proto][port]['name'] )
                      )
"""


if __name__ == "__main__":
    print ("start")
