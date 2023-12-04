import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 模拟键盘操作
from selenium.webdriver.common.by import By

# 查找节点
# Selenium 可以驱动浏览器完成各种操作，比如填充表单、模拟点击等。比如，我们想要完成向某个输入框输入文字的操作或者抓取数据，
# 而 Selenium 提供了一系列查找节点的方法，我们可以用这些方法来获取想要的节点，以便下一步执行一些动作或者提取信息。



# 启动并打开指定页面
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
# 通过name属性选择文本框元素，并设置内容
s = browser.find_element(By.NAME,'wd')
s.send_keys('衣服')
s.send_keys(Keys.ENTER)   # 回车 确定的意思
# 设置五秒后执行下一步
time.sleep(5)



# 各种节点提取演示
# browser.get("http://www.baidu.com")
# # ID选择器定位
# input_text = browser.find_element(By.ID, "kw")
# input_text.send_keys("selenium")
# # CSS 选择器定位
# s =browser.find_element(By.CSS_SELECTOR,'input.s_ipt')
# s.send_keys('衣服')
# # xpath 选择器定位
# s = browser.find_element(By.XPATH,'//input[@id="kw"]')
# s.send_keys('衣服')
