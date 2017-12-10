#coding=utf-8
import urllib
import urllib.request 
import re
url='http://www.ranzhi.org/sitemap.xml'
html=urllib.request.urlopen(url).read()
html=html.decode('utf-8')
r=re.compile(r'(http://www.ranzhi.org.*?\.html)')
big=re.findall(r,html)
for i in big:
 print(i)
 op_xml_txt=open('xml.txt','a')
 op_xml_txt.write('%s\n'%i)