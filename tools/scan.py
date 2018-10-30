#! /usr/bin/python3

import re
import sys
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
import sqlalchemy_utils
import nmap
import setup

def start():
    nm = nmap.PortScanner()
    result = nm.scan(hosts="157.159.45.91", arguments='-T5')
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
    print (nm.csv())
