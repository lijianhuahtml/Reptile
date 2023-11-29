from selenium import webdriver

# 初始化 Chrome 驱动，没有 --headless 参数
driver = webdriver.Chrome()

# 打开网页
url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1"
driver.get(url)

# 等待页面加载完成，可以根据需要进行调整
driver.implicitly_wait(10)

# 获取渲染后的页面内容
rendered_content = driver.page_source

# 关闭浏览器
driver.quit()

# 处理渲染后的内容
print(rendered_content)
