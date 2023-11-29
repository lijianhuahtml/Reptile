from selenium import webdriver

# 使用无头浏览器

url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1"

def main():
    # 使用 Chrome 无头浏览器
    options = webdriver.ChromeOptions()
    options.headless = True

    # 创建浏览器对象
    browser = webdriver.Chrome(options=options)

    # 打开网页
    browser.get(url)

    # 获取渲染后的页面内容
    rendered_content = browser.page_source

    # 关闭浏览器
    browser.quit()

    print(rendered_content)


if __name__ == '__main__':
    main()
