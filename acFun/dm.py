    # -*- coding: utf-8 -*-

import os
import sys
import re
import json
import requests
from lxml import html
import  xml.dom.minidom
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')
jsonPath='gaoji.json'
data=[]
with open(jsonPath,'r') as json_file:
    data = json.load(json_file)

print len(data)
damuArr=data[2]
print damuArr[3]
with open("d.json","w") as f:
	f.write(json.dumps(damuArr[3],ensure_ascii=False))


data:image/png;base64,