#!/usr/local/bin/python2.7

import sys
 
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda
import insertItem 
#import listItem
 
if __name__ == '__main__':
    print 'Content-type: text/html\n'
 
    form_data = cgi.FieldStorage()
    name = form_data.getfirst('name')
    description = form_data.getfirst('description')
    location = form_data.getfirst('location')
    category = form_data.getfirst('category')
    contact = form_data.getfirst('contactInfo')
    imgpath = form_data.getfirst('imgpath')
    
    print insertItem.main(name, description, location, category, contact, imgpath)
    
    #result=listItem.main()
    #tmpl = cgi_utils_sda.file_contents('iFoundIndex.html')
    #page = tmpl.format(listItems=result)
    #print page
