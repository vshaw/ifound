#!/usr/local/bin/python2.7

import sys
 
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda
import searchItem
 
if __name__ == '__main__':
    print 'Content-type: text/html\n'
 
    form_data = cgi.FieldStorage()

    category = form_data.getfirst('categorySelect')
    keyword = form_data.getfirst('keyword')
    if not category:
       items=searchItem.main(keyword, 'keyword')
    else:
       items=searchItem.main(category, 'category')
    tmpl = cgi_utils_sda.file_contents('iFoundIndex.html')
    page = tmpl.format(listItems=items)
    print page 
