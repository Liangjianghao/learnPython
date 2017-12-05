#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('GB2312') 
from selenium import webdriver

print sys.getdefaultencoding()

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
# upload.send_keys('/Users/l/Desktop/learnPython/guo/test.mp3')  # send_keys
upload.send_keys('/Volumes/my/你要/你得娶我.mp3')  # send_keys
print (upload.get_attribute('value'))  # check value

driver.quit()
