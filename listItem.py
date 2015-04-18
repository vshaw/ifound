#!/usr/local/bin/python2.7

'''Lists all the actors in the database

Written Spring 2014
Scott D. Anderson
'''

import sys
import MySQLdb
#to connect to database
from dsn import DSN
import dbconn

# ================================================================
# The functions that do most of the work.  
def getItems(conn):
    '''Returns a string of LI elements, listing all actors and birthdates'''
    curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
    curs.execute('select * from item')
    lines = []
    while True:
        row = curs.fetchone()
        if row == None:
            return "\n".join(lines)
        lines.append('{name} - {description} - {location} - {category} - {contact}'.format(**row))

def main():
    '''Returns a listing all actors and birthdates'''
    DSN['database'] = 'vshaw_db'     # the database we want to connect to
    conn = dbconn.connect(DSN)
    actorlist = getItems(conn)
    return actorlist

# ================================================================
# This starts the ball rolling, *if* the script is run as a script,
# rather than just being imported.    

if __name__ == '__main__':
    print main()
