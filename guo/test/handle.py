#-*-coding:utf-8 -*-
from selenium import webdriver
import time
 
browser = webdriver.Chrome()
first_url='http://www.baidu.com'
browser.get(first_url)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="jgwab"]').click()
# browser.find_element_by_xpath('//div/div/div/ul/li[1]/strong/a').click()


# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# time.sleep(3)
# showNextBtn=driver.find_element_by_xpath('//*[@id="u1"]/a[1]')

# browser.switch_to_window(browser.window_handles[0])
print browser.title  #第一个页面
browser.switch_to_window(browser.window_handles[1])
print browser.title  #最后一个页面
print browser.window_handles

browser.close()
# driver.back()
# browser.quit()