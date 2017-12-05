# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('/Users/l/Desktop/learnPython/guo/image.png')  # send_keys
print upload.get_attribute('value')  # check value

driver.quit()
