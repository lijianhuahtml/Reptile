import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='weibo',
    charset='utf8mb4'  # 指定编码为 utf8
)

cursor = conn.cursor()

def main():
        sql = "insert into comments (comment) values (%s)"
        cursor.execute(sql, ("2222"))
        conn.commit()

        # 关闭游标和连接
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()
