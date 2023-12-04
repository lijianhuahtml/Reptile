from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# 切换IFrame
# 网页中有一种节点叫作 iframe，也就是子 Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。
# Selenium 打开页面后，它默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，它是不能获取到子 Frame 里面的节点的。
# 这时就需要使用 switch_to.frame() 方法来切换 Frame。

browser = webdriver.Chrome()
browser.get('https://www.douban.com/')
login_iframe = browser.find_element(By.XPATH,'//div[@class="login"]/iframe')
browser.switch_to.frame(login_iframe)
browser.find_element(By.CLASS_NAME,'account-tab-account').click()
browser.find_element(By.ID,'username').send_keys('123123123')
