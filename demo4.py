from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 微博爬取

# 初始化 Chrome 驱动
driver = webdriver.Chrome()

# 打开微博页面
weibo_url = "https://weibo.com/example"
driver.get(weibo_url)

# 在页面中找到评论区域的元素，通常评论是在iframe中，需要切换到iframe中
comment_frame = driver.find_element_by_xpath('//iframe[contains(@id, "commentIframe")]')
driver.switch_to.frame(comment_frame)

# 等待评论加载完成
wait = WebDriverWait(driver, 10)
comments_loaded = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list_box')))

# 获取评论数据
comments = driver.find_elements_by_css_selector('.list_box .list_ul .list_li')
for comment in comments:
    user_name = comment.find_element_by_css_selector('.WB_text a').text
    comment_text = comment.find_element_by_css_selector('.WB_text .comment_txt').text
    print(f'{user_name}: {comment_text}')

# 关闭浏览器
driver.quit()
