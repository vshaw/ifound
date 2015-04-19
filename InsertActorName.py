#!/usr/local/bin/python2.7

'''Inserts actors and movies into the database and creates a credit for them. 

Written Spring 2014
Vivienne Shaw
Steffi Lee

'''
import sys
import MySQLdb
#to connect to database
from dsn import DSN
import dbconn

#global variable, my staff id
addid = 952

#inserts actor into database     
def insertName(conn, nm, name, actorbd):
    #only executes if form data is entered
    if str(nm)!="None" and str(name)!="None":
        curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
        curs.execute('SELECT * from person where nm=%s', (nm,))  #searches for existing entry with same nm
        row=curs.fetchone()
        if str(row)=="None":  #adds new actor if none exists
            curs.execute('INSERT INTO person(nm,name,birthdate,addedby) VALUES (%s,%s,%s,%s)', (nm,name,actorbd,addid,))
            print(str(name) + ' added.' + '<p></p>')
            conn.commit()
        else:  #updates info for the specified nm
            curs.execute('UPDATE person SET name=%s, birthdate=%s, addedby=%s WHERE nm=%s', (name, actorbd, addid, nm, ))
            print(str(name)+ " updated")

#inserts movie into the database
def insertMovie(conn, tt, title, release, index, nm):
    #only executes if form data is entered
    if str(tt)!="None" or str(title)!="None":
        curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
        curs.execute('SELECT * from movie where title=%s', (title,)) #searches for existing movie with same title
        row=curs.fetchone()
        if str(row)=="None":  #adds new movie 
            if str(tt)!="None": #inserts movie with specified tt
                curs.execute('INSERT INTO movie VALUES (%s,%s,%s,null,%s)', (tt,title,release,addid ))
                insertCredit(conn, tt, nm) #creates credit 
                print(str(title)+ ' added.'+'<p></p>')
                conn.commit()
            else: 
                print("Error with row " + str(index)+"Title not in database. Provide tt.")
        else: 
            insertCredit(conn, row['tt'],nm) #gets existing tt and adds credit

#creates credit for actor and every movie listed
def insertCredit(conn, tt, nm): 
    if str(tt)!="None" and str(nm)!="None":   #only creates if tt and nm are specified
        curs = conn.cursor(MySQLdb.cursors.DictCursor)
        curs.execute('INSERT INTO credit VALUES (%s,%s)', (tt,nm, ))
        conn.commit()

#main, takes two Dictionaries of actor and movie information, and insertactor boolean
def main(actor, movie, insertactor):
    DSN['database'] = 'wmdb'     # the database we want to connect to
    conn = dbconn.connect(DSN)
    if insertactor:    #calls insertactor function 
        insertName(conn,actor['nm'],actor['name'],actor['bd'])
    else:      #calls insertmovie function
        insertMovie(conn, movie['tt'], movie['title'], movie['release'], movie['index'], actor['nm'])
    
 
# ================================================================
# Allows program to be run as a script.

if __name__ == '__main__':
    actorinfo = sys.argv[1]
    movieinfo = sys.argv[2]
    insertactor = sys.argv[3]
    main(actorinfo, movieinfo,insertactor)
