#! /usr/bin/python3

import re
import sys
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
import sqlalchemy_utils
import nmap
import setup

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
    (id, id_plage, host_line, description) = elem
    print ('\nScanning: nmap {0}{1} '.format(args_nmap, host_line))
    result_scan = nm.scan(hosts=host_line, arguments=args_nmap)
    display_result(nm)
    #print (nm.csv())
    sql = 'DELETE FROM {0} WHERE id_plage_ip=\'{1}\''
    sql = sql.format('résultat_nmap', id)
    #print(sql)
    #con.execute(sql)

def display_result(nm):
    for host in nm.all_hosts():
        print('[*] Host : %s -- ' % (host)) # add name adh6 api
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print ('\tport : %s\tstate : %s\tname : %s' 
                       % (port, 
                          nm[host][proto][port]['state'], 
                          nm[host][proto][port]['name'] )
                      )
    return
