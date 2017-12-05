#-*-coding:utf-8 -*-

import time
from selenium import webdriver
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)
showNextBtn=driver.find_element_by_xpath('//*[@id="u1"]/a[1]')
print showNextBtn
print showNextBtn.text
# chain=ActionChains(driver)     
# chain.move_to_element(showNextBtn).perform()     #鼠标移到悬停元素上
# # time.sleep(3)

# nextBtn=driver.find_elements_by_class_name('setpref')
# print (len(nextBtn))
# nextBtn[0].click()
# time.sleep(2)
showNextBtn.click()