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
import cgi_utils_sda
# ================================================================
# The functions that do most of the work.  
def getItems(conn):
    '''Returns a string of LI elements, listing all actors and birthdates'''
    curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
    curs.execute('select * from item;')
    lines = ""
 
    for row in curs.fetchall():
        lines += '<li><a href="#profile1" class="ui-link-inherit">\n'
        lines += '<img src="'
        if row['category'] == 'clothing':
            lines += 'clothing.png">\n'
        if row['category'] == 'containers':
            lines += 'bottle.png">\n'
        if row['category'] == 'devices':
            lines += 'device.png">\n'
        if row['category'] == 'books':
            lines += 'book.png">\n'
        if row['category'] == 'other': 
            lines += 'other.png">\n'
	name = row['name'] if row['name'] is not None else ""
        description = row['description'] if row['description'] is not None else ""
        lines += '<h3 class="ui-li-heading">'+name+'</h3>\n'
        lines += '<p class="ui-li-desc">'+description+'</p>\n'
        lines += '</a></li>\n'
    return lines
       # lines.append('{name} - {description} - {location} - {category} - {contact}'.format(**row))


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
