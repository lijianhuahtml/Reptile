# document.body.scrollHeight 获取页面高度
import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 页面滚动案例
# 对于某些操作，Selenium API 并没有提供。比如，下拉进度条，它可以直接模拟运行 JavaScript，此时使用 execute_script() 方法即可实现

cookie = {"name": "key-aaaaaaa", "value": "value-aaaaaaa"}

browser = webdriver.Chrome()
browser.add_cookie(cookie)
browser.get('https://weibo.com/')
# scrollTo  不叠加 200 200    scrollBy 叠加  200 300  500操作
# 慢慢的下拉
for i in range(1,3):
    time.sleep(2)
    browser.execute_script('window.scrollTo(0,{})'.format(i * 700)) # scrollTo 不叠加 700 1400 2100

    lis = browser.find_elements(By.CSS_SELECTOR,'.woo-box-flex.woo-box-alignCenter.woo-box-justifyCenter.toolbar_wrap_np6Ug')
    for li in lis:
        li.click()

    html = browser.page_source

    # print(lis)

    print(browser.current_url)

    soup = BeautifulSoup(html, 'html.parser')

    print("===========================================================================================================")

time.sleep(1)
