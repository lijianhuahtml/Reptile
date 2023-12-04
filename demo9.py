from selenium import webdriver
from selenium.webdriver.common.by import By

# 多个节点
# 如果要查找所有满足条件的节点，需要用 find_elements() 这样的方法。注意，在这个方法的名称中，element 多了一个 s，注意区分。

browser = webdriver.Chrome()
browser.get('https://www.icswb.com/channel-list-channel-161.html')
lis = browser.find_elements(By.CSS_SELECTOR,'#NewsListContainer li')
print(lis)
