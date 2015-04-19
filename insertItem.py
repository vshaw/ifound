#!/usr/local/bin/python2.7

import sys
import MySQLdb
from dsn import DSN
import dbconn
import cgi_utils_sda

#global variable, my staff id
#addid = 952

#inserts actor into database     
def insertItem(conn, name, description, location, category, contact, imgpath):
    #only executes if form data is entered
    if str(name)!="None" and str(contact)!="None":
        curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
        curs.execute('INSERT INTO item(name, description, location, category, contact, imgpath) VALUES (%s,%s,%s,%s,%s,%s)', (name,description, location, category, contact, imgpath,))
        #print(str(name) + ' added.' + '<p></p>')
        conn.commit()

def main(name, description, location, category, contact, imgpath):
    if name is None:
        name = ""
    if description is None:
        description = ""
    if location is None:
        location = ""
    if category is None:
        category = "other"
    if contact is None:
        contact = ""
    if imgpath is None:
        imgpath = ""
    DSN['database'] = 'vshaw_db'     # the database we want to connect to

    conn = dbconn.connect(DSN)
    result = insertItem(conn, name, description, location, category, contact, imgpath)
    return result     

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
