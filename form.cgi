#!/usr/local/bin/python2.7
 
import sys 
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda
 
if __name__ == '__main__':
    print 'Content-type: text/html\n'
 
    form_data = cgi.FieldStorage()
    if 'category' in form_data or 'search' in form_data :
        tmpl = cgi_utils_sda.file_contents('form.html')
	
	if 'category' in form_data:
	    category = form_data.getfirst('category')
            page = tmpl.format(name=category)
	elif 'general' in form_data:
	    general = form_data.getfirst('general')
    	    page = tmpl.format(name=general)

        print page
	
    else:
        print '''Error: This script, {script}, should be given form data
that includes a "username" input'''.format(script=sys.argv[1])
