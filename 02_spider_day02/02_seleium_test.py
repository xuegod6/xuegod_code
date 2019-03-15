# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 16:17
# @Author  : for 
# @File    : 02_seleium_test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import requests
import time
browser = webdriver.Chrome()
browser.set_window_size(1366,768)
wait = WebDriverWait(browser,10)
browser.get('http://jandan.net/ooxx')
def get_content():
    try:
        wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="comments"]/ol'))
        )
        #
        print("正在爬取{}".format(browser.current_url))
        page_source = browser.page_source  # 获取网页源码
        html = etree.HTML(page_source)  # 解析源码
        imgs = html.xpath("//li[contains(@id,'comment')]//img/@src")  # 匹配图片
        print(imgs)
        download(imgs)
    except Exception as e:
        print("错误")
        print(e)
    finally:
        browser.close()
def download(imgs):
    path = "./xxoo/{}"  # 路径我写死了
    for img in imgs:
        try:
            res = requests.get(img)
            content = res.content
        except Exception as e:
            print(e)
            continue
        file_name = img.split("/")[-1] # 获取文件名

        with open(path.format(file_name),"wb") as f:
            f.write(content)
            print(file_name,"成功下载文件")
            time.sleep(0.3)

    # 循环下载完毕，进行翻页操作 previous-comment-page
    next = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="comments"]//a[@class="previous-comment-page"]'))
    )
    next.click()
    return get_content()  # 继续调用上面的网页源码分析流程
if __name__ == '__main__':
    get_content()