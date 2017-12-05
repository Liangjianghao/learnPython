#-*-coding:utf-8 -*-

import time
from selenium import webdriver
import sys
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///Users/l/Desktop/learnPython/guo/test/alert.html')
'''获取alert对话框的按钮,点击按钮,弹出alert对话框'''
driver.find_element_by_xpath('/html/body/div/input[1]').click()
'''获取alert对话框'''
alert = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
print (alert.text)  #打印警告对话框内容
result=EC.alert_is_present()(driver)
if result:
	print ('弹窗')
	time.sleep(3)
	result.accept()
else:
	print ('未出现提示框')
time.sleep(10)
'''获取警告对话框的内容'''

# alert.accept()   #alert对话框属于警告对话框，我们这里只能接受弹窗
'''添加等待时间'''
time.sleep(2)
# driver.quit()