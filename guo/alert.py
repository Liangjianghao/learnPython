#-*-coding:utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/hunk/Desktop/alter.html')
'''获取alert对话框的按钮,点击按钮,弹出alert对话框'''
driver.find_element_by_xpath('/html/body/div/input[2]').click()
'''获取alert对话框'''
alert = driver.switch_to_alert()
'''添加等待时间'''
time.sleep(2)
'''获取警告对话框的内容'''
print (alert.text)  #打印警告对话框内容
alert.accept()   #alert对话框属于警告对话框，我们这里只能接受弹窗
'''添加等待时间'''
time.sleep(2)
driver.quit()