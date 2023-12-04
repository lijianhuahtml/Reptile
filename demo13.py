from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 页面滚动

# # 浏览器滚动到底部 10000位置
# document.documentElement.scrollTop = 10000
# # 滚动到顶部
# document.documentElement.scrollTop = 0
#
# # 移动到页面最底部
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#
# # 移动到指定的坐标(相对当前的坐标移动)
# driver.execute_script("window.scrollBy(0, 700)")
# # 结合上面的scrollBy语句，相当于移动到700+800=1600像素位置
# driver.execute_script("window.scrollBy(0, 800)")
#
# # 移动到窗口绝对位置坐标，如下移动到纵坐标1600像素位置
# driver.execute_script("window.scrollTo(0, 1600)")
# # 结合上面的scrollTo语句，仍然移动到纵坐标1200像素位置
# driver.execute_script("window.scrollTo(0, 1200)")
