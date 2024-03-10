import random
import re


import re

def freedom():
    # 读取文件内容
    with open('URL.txt', 'r') as file:
        content = file.readlines()

    # 随机输出一个列表内容
    random_item = random.choice(content)
    return random_item



def filtered_url(url):
    pattern = r'\[\'(.*?)\'\]'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return url

# url = freedom()

# print(filtered_url())