import glob
import lxml.html
import sys

#thefile = 'Foley+AL'



#time.sleep(1)

#print root

files = glob.glob('*+*')
print files


cities ={}
for thefile in files:

    #print thefile
    #print len(cities)

    htmltext = open(thefile,'r').read()
    root = lxml.html.fromstring(htmltext)

    for alink in root.xpath('//a'):
        if 'course.aspx?course=' in alink.get('href',''):
            p = alink.getparent().getparent()
            course_html = lxml.html.tostring(p)
            courseno= alink.get('href').split('=')[1]
            #print courseno
            #open('courses/%s.html' %courseno,'w').write(course_html)
            cities[courseno] = course_html

#    if len(cities) > 10000:
#        break

for k,v in cities.items():
    open('courses/%s.html' %k,'w').write(v)
    print 'wrote %s' %k







