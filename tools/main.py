#! /usr/bin/python3

import setup
import scan

if __name__ == "__main__":
    ''' Specify custom data '''
    username = 'respoweb'
    password = 'MXlf55DdYmURrHDlcbnYXKiGg2O'
    db = 'nmap'
    ''' Setup config '''
    setup.create_user(username, password)
    setup.grant_user(username)
    setup.create_database(username, db, password)
    setup.create_tables(username, db, password)
    ''' Scan push to db '''
    #scan_push_in db  
