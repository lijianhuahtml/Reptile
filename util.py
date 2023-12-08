
def get_cookie(item):
    # 指定文本文件路径
    file_path = 'config.txt'
    res = ""
    item = item+"="
    # 打开文本文件并读取内容
    with open(file_path, 'r') as file:
        # 逐行读取文件内容
        for line in file:
            # 检查每一行是否包含 'Cookie='
            if item in line:
                # 提取 Cookie 内容
                res = line.split(item)[1].strip()
                break  # 如果找到第一个包含 'Cookie=' 的行，可以选择终止循环
    return res

if __name__ == '__main__':
    print(get_cookie('Cookie'))