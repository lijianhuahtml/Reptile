from selenium import webdriver
from time import sleep
import json

from selenium.webdriver.common.by import By

# 获取cookie

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/login.php')
    sleep(6)
    # driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')) # 切换浏览器标签定位的作用域
    driver.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
    sleep(20)
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('微博_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
    driver.close()
    driver.quit()
