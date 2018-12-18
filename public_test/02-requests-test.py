# -*- coding: utf-8 -*-
# @Time : 2018/12/7 21:02 
# @Author : for 
# @File : 02-requests-test.py 
# @Software: PyCharm
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# o#pt = webdriver.ChromeOptions()
#opt.set_headless()

driver = webdriver.Chrome('D:/chromedriver/chromedriver')

driver.get('https://www.baidu.com')
import time

driver.refresh()

# driver.set_window_size(1400,800)
print('befor seratch')

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

driver.find_element_by_id('kw').send_keys('哈士奇图片')
driver.find_element_by_id('su').click()
time.sleep(1)
driver.refresh()
now_url = driver.find_elements_by_xpath('//div/h3/a')
num = 0
for t in now_url:
    try:
        print(t.text)
        element = driver.find_element_by_partial_link_text(t.text)
        element.click()
        time.sleep(3)
        num += 1
    except:
        print('错误了')
    else:
        if num >5:
            driver.quit()
            break
            # sys.exit()
# if num > 5:
#     driver.quit()
