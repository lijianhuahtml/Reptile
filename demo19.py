from selenium import webdriver
import time
import random
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WeiPin():

    def __init__(self):
        self.client = MongoClient(host='127.0.0.1', port=27017)
        self.col = self.client['spiders']['weipinhui']
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()

    def base(self):
        self.browser.get('https://www.vip.com/')
        wait = WebDriverWait(self.browser, 10)
        input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="c-search-input  J-search-input"]')))
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="c-search-button  J-search-button  J_fake_a"]')))
        input.send_keys('口红')
        time.sleep(random.randint(3000, 3400) / 1000)
        button.click()
        time.sleep(random.randint(1000, 1400) / 1000)

    def spider(self):
        self.drop_down()
        # print(self.browser.page_source)
        node_list = self.browser.find_elements(By.XPATH,
                                               '//section[@id="J_searchCatList"]/div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]')
        # print(node_list)
        for node in node_list:
            price = node.find_element(By.XPATH,
                                      './/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]').text
            title = node.find_element(By.XPATH, './/div[2]/div[2]').text
            try:
                discount = node.find_element(By.XPATH,
                                             './/div[@class="c-goods-item__main-price     J-goods-item__main-price"]/div[@class="c-goods-item__discount  J-goods-item__discount"]').text
            except Exception as e:
                print('数据为空')
                discount = '空'
            try:
                market_price = node.find_element(By.XPATH,
                                                 './/div[@class="c-goods-item__market-price  J-goods-item__market-price"]').text
            except Exception as e:
                print('数据为空')
                market_price = '空'

            item = {
                'title': title,
                'price': price,
                'discount': discount,
                'market_price': market_price
            }
            print(item)
            self.save_mongo(item)
        self.page_next()

    def save_mongo(self, item):
        if isinstance(item, dict):
            self.col.insert_one(item)

    def page_next(self):
        try:
            next_button = self.browser.find_element(By.XPATH, '//*[@id="J_nextPage_link"]')
            if next_button:
                next_button.click()
                self.spider()
            else:
                self.browser.close()

        except Exception as e:
            self.browser.close()

    def drop_down(self):
        for x in range(1, 10):
            js = f"document.documentElement.scrollTop = {x * 1000}"
            self.browser.execute_script(js)
            time.sleep(random.randint(500, 800) / 1000)


if __name__ == '__main__':
    weipin = WeiPin()
    weipin.base()
    weipin.spider()
