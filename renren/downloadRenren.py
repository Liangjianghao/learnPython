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
import time
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')
# https://zimuzuustv.ctfile.com/downhtml/1939455/228422415/1512716066/975614920/f038d3038f0449da6659e2bfd51cc012.html
# https://zimuzuustv.ctfile.com/downhtml/1939455/230403836/1512716233/975614920/f0a5020dfbfdedac7976158a269f9440.html
with open("gdg.json",'r') as load_f:
	load_dict = json.load(load_f)
	# print(load_dict)
for url in load_dict:
	print url
	driver=webdriver.Chrome()
	# url='https://zimuzuustv.ctfile.com/fs/1939455-228422415'
	driver.get(url)
	time.sleep(5)
	downLoadBtn=driver.find_element_by_id("free_down_link")
	downLoadBtn.click()
	time.sleep(5)
	print driver.current_url
	downLoadBtn2=driver.find_element_by_id("free_down_link")
	downLoadBtn2.click()
	time.sleep(600)
time