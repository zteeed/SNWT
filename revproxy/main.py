#! /usr/bin/python3

import os
import setup

if __name__ == "__main__":
    ''' Specify custom data '''
    username = 'respoweb'
    password = os.environ['password_db']
    db = 'revproxy'
    ''' Setup config '''
    setup.create_user(username, password)
    setup.grant_user(username)
    setup.create_database(username, db, password)
    setup.create_tables(username, db, password)
    setup.push_data_from_revproxy(username, db, password)
