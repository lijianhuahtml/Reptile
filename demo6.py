# name：ljh
# time：2023/12/3 22:18

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()


# 获取主要代码
def request_douban(url):
    driver.get(url)
    driver.implicitly_wait(10)
    rendered_content = driver.page_source
    return rendered_content


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    # url = "https://zhuanlan.zhihu.com/p/625667742?utm_id=0&wd=&eqid=d70166a10000c148000000026486c9f1"
    html = request_douban(url)

    soup = BeautifulSoup(html, 'lxml')

    movie_list = soup.find(class_='grid_view').find_all('li')

    # Create workbook and sheet outside the loop
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')

    for item in movie_list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')

        # Fix the issue with item_index
        item_index = item.find('em').string

        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        item_intr = item.find(class_='inq').string

        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)

        # Write data to the sheet
        sheet.write(int(item_index), 0, item_name)
        sheet.write(int(item_index), 1, item_img)
        sheet.write(int(item_index), 2, item_index)
        sheet.write(int(item_index), 3, item_score)
        sheet.write(int(item_index), 4, item_author)
        sheet.write(int(item_index), 5, item_intr)

    book.save('豆瓣电影Top250.xls')



if __name__ == '__main__':
    for i in range(0, 10):
        main(i)
