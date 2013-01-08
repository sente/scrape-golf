import glob
import lxml.html
import requests
import sys


if len(sys.argv) == 2:
    files = [f]
if len(sys.argv) > 2:
    files = sys.argv[1:]





cities ={}
for thefile in files:

    if thefile.startswith('http'):
        htmltext = requests.get(thefile).content
    else:
        htmltext = open(thefile,'r').read()

    root = lxml.html.fromstring(htmltext)

    for alink in root.xpath('//a'):
        if 'course.aspx?course=' in alink.get('href',''):
            p = alink.getparent().getparent()
            course_html = lxml.html.tostring(p)
            courseno = alink.get('href').split('=')[1]
            cities[courseno] = course_html


for k,v in cities.items():
    open('courses/%s.html' %k,'w').write(v)
    print 'wrote %s' %k







