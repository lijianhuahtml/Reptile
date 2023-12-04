from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取节点信息
# 我们可以使用 get_attribute() 方法来获取节点的属性，但是其前提是先选中这个节点

browser = webdriver.Chrome()

url = 'https://pic.netbian.com/4kmeinv/index.html'
browser.get(url)
src = browser.find_elements(By.XPATH,'//ul[@class="clearfix"]/li/a/img')
for i in src:
    url = i.get_attribute('src')
    print(url)
