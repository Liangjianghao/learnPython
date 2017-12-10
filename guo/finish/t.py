# https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Fhome%3Ft%3Dhome%2Findex%26lang%3Dzh_CN%26token%3D1785036581
# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import math
from lxml import html
# import urllib2
import re


from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import sys
from selenium import webdriver
def cutStr(name):
	resultStr=''
	d={}  
	for c in name:   
	    d[c] = (d[c] + 1) if (c in d) else (1)   
	print d[' '] 
	if ' ' in name :
		if d[' ']>1:
			for index,NameStr in enumerate(name.split(' ')):
				if index==0:
					continue
				else:
					resultStr+=NameStr
		else:
			for index,NameStr in enumerate(name.split(' ')):
				resultStr+=NameStr
	else:
		resultStr=name
	resultStr=resultStr.split('.')[0]
	resultStr=resultStr.replace('（','').replace('）','').replace('《','').replace('》',' ').replace('高清',' ')
	resultStr=re.sub(r"[\t,^\d{n}]",'',resultStr)
	return resultStr
print cutStr('2008高清《戏剧与方言》（郭德纲 于谦）.mp3')