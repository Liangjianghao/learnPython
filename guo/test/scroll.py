#-*-coding:utf-8 -*-

import time
from selenium import webdriver
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# driver=webdriver.Chrome()
# driver.get('https://www.douban.com')
# js="var q=document.documentElement.scrollTop=10000"  
# driver.execute_script(js)
# time.sleep(1)
# showNextBtn=driver.find_element_by_xpath('//*[@id="u1"]/a[7]')
# print showNextBtn.location
# print showNextBtn.size
# actions = ActionChains(driver);
# actions.move_by_offset(1038, 19).click().perform()
# time.sleep(10)

from selenium import webdriver
dr=webdriver.Chrome()
dr.get('file:///Users/l/Desktop/learnPython/guo/test/sroll.html')
js='document.getElementsByClassName("scroll")[0].scrollTop=10000' 
# 就是这么简单，修改这个元素的scrollTop就可以
dr.execute_script(js)