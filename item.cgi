#!/usr/local/bin/python2.7

import sys
 
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda
import listItem 
 
if __name__ == '__main__':
    print 'Content-type: text/html\n'
 
    items=listItem.main()
    tmpl = cgi_utils_sda.file_contents('iFoundIndex.html')
    page = tmpl.format(listItems=items)
    print page 
