from selenium import webdriver
from time import sleep
import json


def browser_initial():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(
        'https://weibo.com/login')
    return browser


def log_csdn(browser):
    browser.add_cookie({'name': 'selenium3', 'value': 'valuenmn'})

    sleep(3)
    browser.refresh()  # 刷新网页,cookies才成功
    sleep(10)

if __name__ == "__main__":
    browser = browser_initial()
    log_csdn(browser)