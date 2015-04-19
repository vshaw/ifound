#!/usr/local/bin/python2.7

import sys
import MySQLdb

from dsn import DSN

import dbconn
import cgi_utils_sda

def getRows(conn, choice, searchType):
    curs = conn.cursor(MySQLdb.cursors.DictCursor)

    if searchType == 'keyword':
        curs.execute('select * from item where name like \'%'+choice+'%\' or description like \'%' + choice + '%\';')
    if searchType == 'category':
        curs.execute('select * from item where category=\''+choice+'\';')
    lines = ""

    for row in curs.fetchall():
        lines += '<li><a href=#profile1" class="ui-link-inherit">\n'
        lines += '<img src="'
        if row['category'] == 'clothing':
            lines += 'clothing.png">\n'
        if row['category'] == 'containers':
            lines += 'bottle.png">\n'
        if row['category'] == 'books':
            lines += 'book.png">\n'
        if row['category'] == 'other':
            lines += 'other.png">\n'
        lines += '<h3 class="ui-li-heading">'+row['name']+'</h3>\n'
        lines += '<p class="ui-li-desc">'+row['description']+'</p>\n'
        lines += '</a></li>\n'
    return lines

def main(choice, searchType):
    DSN['database'] = 'vshaw_db'
    conn = dbconn.connect(DSN)
    items = getRows(conn,choice,searchType)
    return items

if __name__ == '__main__':
    print main('clothing')
