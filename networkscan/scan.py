#! /usr/bin/python3

import time
import re
import sys
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
import sqlalchemy_utils
import nmap
import setup
from socket import inet_aton
import struct

def update_db(username, db, password, fast=False):
    nm = nmap.PortScanner()
    con = setup.connect(username, db, password)
    L, args_nmap = config_scan(con, fast)
    for elem in L:
        update_db_elem(con, elem, args_nmap, nm)
    return

def config_scan(con, fast):
    sql = 'SELECT * FROM plages_ip'
    result_sql = con.execute(sql)
    L = [ eval(str(row)) for row in result_sql ]
    args_nmap = '-T5 '
    if fast: args_nmap+='-F '
    return L, args_nmap

def update_db_elem(con, elem, args_nmap, nm):
    (id, id_catégorie, host_line, description) = elem
    print ('\nScanning: nmap {0}{1} '.format(args_nmap, host_line))
    result_scan = nm.scan(hosts=host_line, arguments=args_nmap)
    display_update_result(con, nm, id)

def display_update_result(con, nm, id):
    list_of_ips = nm.all_hosts()
    list_of_ips = sorted(list_of_ips, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
    for host in list_of_ips:
        print('\n[*] Host : %s -- ' % (host)) # add name adh6 api
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                #time.sleep(0.2)
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                if state=='open': state+='\t'
                print ('\tport : %s\t\tstate : %s\t\tname : %s' % (port, state, name))
            for port in sorted(lport):
                #time.sleep(0.2)
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                push_query(con, nm, id, host, port, state, name) 
    return

def push_query(con, nm, id, ip, port, state, name):
    sql = 'INSERT INTO {0} ({1}, {2}, {3}, {4}, {5}) VALUES (\'{6}\', \'{7}\',\'{8}\', \'{9}\', \'{10}\')'
    sql = sql.format('résultat_scan', 'id_plages_ip', 'ip', 'port', 'state', 'name', id, ip, port, state, name)
    print('\t[+] '+sql); con.execute(sql)
    return
