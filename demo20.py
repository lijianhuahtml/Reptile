import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Chrome()


# 跳过验证码

def loginFoc(url, username, password):
    driver.get(url)
    elem = driver.find_element(By.NAME, "username")
    elem.clear()
    elem.send_keys(username)
    time.sleep(2)
    elem1 = driver.find_element(By.NAME, "password")
    elem1.clear()
    elem1.send_keys(password)
    time.sleep(1)
    elem2 = driver.find_element(By.XPATH, "//div[@class='btn_mod']/input").click()  # 取消“下次自动登录的打勾”
    time.sleep(1)
    # elem1.send_keys(Keys.RETURN)#也可以直接点击回车登录
    # elem3=driver.find_element_by_xpath("//input[@class='W_btn_a btn_34px']").click()   #多种爬取方式
    elem3 = driver.find_element(By.XPATH, "//div[@class='form_mod']/ul/li[7]").click()
    time.sleep(15)
    driver.find_element(By.XPATH, "//div[@class='form_mod']/ul/li[7]").click()
    print("登录成功")
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    username = ("输入用户名")
    password = ("输入密码")
    url = ("https://login.sina.com.cn/")
    loginFoc(url, username, password)
    time.sleep(3)
    keyword = ("输入关键词")
    url_s = ("https://s.weibo.com/")
    # searchFoc(url_s,keyword)
    driver.close()
