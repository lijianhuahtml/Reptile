from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 延时等待
# 在 Selenium 中，get() 方法会在网页框架加载结束后结束执行，此时如果获取 page_source，
# 可能并不是浏览器完全加载完成的页面，如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不一定能成功获取到。
# 所以，这里需要延时等待一定时间，确保节点已经加载出来

# 使用方法
# 指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，
# 就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常。

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
button = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
print(input, button)


# 补充解释
# 这样可以做到的效果就是，在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。
#
# 对于按钮，可以更改一下等待条件，比如改为 element_to_be_clickable，也就是可点击，
# 所以查找按钮时查找 CSS 选择器为.btn-search 的按钮，如果 10 秒内它是可点击的，也就是成功加载出来了，
# 就返回这个按钮节点；如果超过 10 秒还不可点击，也就是没有加载出来，就抛出异常。
