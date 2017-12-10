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

def login():
	option=webdriver.ChromeOptions()
	option.add_argument('--user-data-dir=/Users/l/Library/Application Support/Google/Chrome/Default')
	driver = webdriver.Chrome(chrome_options=option)
	# driver = webdriver.Chrome()

	driver.get("http://www.acfun.cn/login/")
	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys('1084933098@qq.com')

	elemMM = driver.find_element_by_id("ipt-pwd-login")
	elemMM.send_keys("l31415926")

	# time.sleep(3)
	loginBtn = driver.find_element_by_class_name("btn-login")
	loginBtn.click()
	time.sleep(5)

	return driver