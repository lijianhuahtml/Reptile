from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

# 初始化浏览器
driver = webdriver.Chrome() # Replace with the correct path

# 打开网页
driver.get('https://weibo.com/')

# 模拟滚动条滚动
for i in range(10):
    # 模拟按键向下滚动
    body = driver.find_element('tag name', 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # 等待加载，你可以根据实际情况进行调整

    # 等待评论图标可见
    comment_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.toolbar_commentIcon_3o7HB'))
    )

    # 使用 ActionChains 移动鼠标到元素并点击
    action = ActionChains(driver)
    action.move_to_element(comment_icon).click().perform()

# 获取滚动后的页面内容
content = driver.page_source

# 关闭浏览器
driver.quit()

# 处理获取到的内容
# 在这里可以使用正则表达式、BeautifulSoup等进行数据提取和处理
print(content)