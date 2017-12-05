#-*-coding:utf-8 -*-

import time
from selenium import webdriver
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)
showNextBtn=driver.find_element_by_xpath('//*[@id="u1"]/a[7]')
print showNextBtn.location
print showNextBtn.size
actions = ActionChains(driver);
actions.move_by_offset(1038, 19).click().perform()
time.sleep(10)
