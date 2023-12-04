from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# selenium 使用

# 打开指定（chrome）浏览器
browser = webdriver.Chrome()
# 指定加载页面
browser.get("http://www.baidu.com/")
# 通过name属性选择文本框元素，并设置内容
browser.find_element(By.NAME,'wd').send_keys("selenium")
# 通过通过ID属性获取“百度一下”按钮，并执行点击操作
browser.find_element(By.ID,"su").click()
# 提取页面
print(browser.page_source.encode('utf-8'))
# 提取cookie
print(browser.get_cookies())
# 获取当前页面截屏
print(browser.get_screenshot_as_file('123.png'))
# 提取当前请求地址
print(browser.current_url)
# 设置五秒后执行下一步
time.sleep(5)
# 关闭浏览器
browser.quit()
