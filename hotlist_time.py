from datetime import datetime
import time
import requests
import mysql
import util

# 热门榜单_小时榜

def get_req(url, headers):
    reqtimes = 0
    while True:
        try:
            reqtimes += 1
            req = requests.get(url=url, headers=headers)
            time.sleep(1)
            if req.status_code == 200:
                return req
        except Exception as e:
            time.sleep(3)
            if reqtimes > 20:
                return None
            if "HTTPSConnectionPool(host='s.weibo.com', port=443)" in str(e):
                continue


def get_plUrl(mid, uid, url):
    count = 1
    pl_url = f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={mid}&is_show_bulletin=2&is_mix=0&count=10&uid={uid}&fetch_level=0&locale=zh-CN'
    while 1:
        # 拿评论, 同时拿到下一页的max_id,
        max_id = get_comment(pl_url, url)
        print(max_id)
        if max_id == 0 or count == 3:
            print('=========爬取完毕==========')
            break
        print(f'第{count}页完成')
        # 构建下一页的url
        count += 1
        pl_url = f"https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={mid}&is_show_bulletin=3&is_mix=0&max_id={max_id}&count=20&uid={uid}&fetch_level=0&locale=zh-CN"
        print(pl_url)
        time.sleep(1)


def get_comment(pl_url, url):
    print("帖子连接：" + pl_url)

    """一级评论"""
    r = get_req(pl_url, headers).json()
    # max_id的值
    max_id = r['max_id']
    # 所有的评论
    data = r['data']

    # 遍历得到每一条评论
    for i in data:
        # 评论内容
        comment = i['text_raw']
        stime = i['created_at']
        # 当前评论的id
        level_id = i['idstr']
        try:
            source = i['source']
        except KeyError:
            source = ""

        # 情感分析=============================================
        emotion = 0

        print("一级评论：" + comment + "   发表时间：" + stime + "     from:" + source + "       url:" + url)

        time = datetime.strptime(stime, '%a %b %d %H:%M:%S %z %Y')
        area = source[2:]

        # 写入数据库
        sql = "insert into comments (content, time, emotion, area, url) values (%s,%s,%s,%s,%s)"
        mysql.cursor.execute(sql, (comment, time, emotion, area, url))
        mysql.conn.commit()

        # 二级评论的url
        level_url = "https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=%s&is_show_bulletin=2&is_mix=1&fetch_level=1&max_id=0&count=20&uid=%s" % (
        level_id, uid)
        level_split_url = "https://weibo.com/ajax/statuses/buildComments?flow=1&is_reload=1&id=%s&is_show_bulletin=2&is_mix=1&fetch_level=1&max_id={}&count=20&uid=%s" % (
        level_id, uid)
        while 1:
            level_max_id = get_level_comment(level_url, url)
            # 二级评论返回结果是0, 就代表抓取二级评论完毕
            if level_max_id == 0:
                break
            level_url = level_split_url.format(level_max_id)

    return max_id


def get_level_comment(level_url, url):
    """二级评论"""
    print(level_url)
    r = get_req(level_url, headers).json()
    # max_id的值
    level_max_id = r['max_id']
    # 所有的评论
    data = r['data']
    for i in data:
        comment = i['text_raw']
        stime = i['created_at']
        try:
            source = i['source']
        except KeyError:
            source = ""

        # 情感分析=============================================
        emotion = 0

        print("二级评论：" + comment + "   发表时间：" + stime + "     from:" + source + "       url:" + url)

        time = datetime.strptime(stime, '%a %b %d %H:%M:%S %z %Y')
        area = source[2:]


        # 写入数据库
        sql = "insert into comments (content, time, emotion, area, url) values (%s,%s,%s,%s,%s)"
        mysql.cursor.execute(sql, (comment,time,emotion,area,url))
        mysql.conn.commit()

    return level_max_id


if __name__ in '__main__':
    # 设置请求头
    headers = {
        'Cookie': util.get_cookie('Cookie'),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    id_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&group_id=1028039999&containerid=102803_ctg1_9999_-_ctg1_9999_home&extparam=discover%7Cnew_feed&max_id=0&count=10'
    while True:
        id_req = get_req(id_url, headers)
        id_json = id_req.json()
        lens = len(id_json['statuses'])
        for i in range(0, lens):
            id = id_json['statuses'][i]['id']
            mid = id_json['statuses'][i]['mid']
            uid = id_json['statuses'][i]['user']['id']
            user_name = id_json['statuses'][i]['user']['screen_name']
            print("username：" + user_name)
            url = f'https://weibo.com/{uid}/{id}'
            get_plUrl(mid, uid, url)
        max_Id = id_json['max_id']
        id_url = f'https://weibo.com/ajax/feed/hottimeline?since_id=0&group_id=1028039999&containerid=102803_ctg1_9999_-_ctg1_9999_home&extparam=discover%7Cnew_feed&max_id={max_Id}&count=10'
