from bs4 import BeautifulSoup  # 网页解析  获取数据
import re  # 正则表达式 进行文字匹配
import urllib.request, urllib.error  # 制定url 获取网页数据

def main():
    baseurl = "https://wallhaven.cc/toplist"
    # 1爬取网页
    # datalist = getData(baseurl)
    output = getData(baseurl)
    print(output)
    # 创建并写入文件
    with open('URL.txt', 'w') as file:
        for item in output:
            item = str(item)
            file.write(item + '\n')

# def getData():

# re.compile的作用是将正则表达式的字符串形式编译成正则表达式对象，以便在后续的匹配中重复使用。
# r在这里是"原始字符串"的意思。它告诉Python解释器不要对字符串中的反斜杠进行转义处理，而是将字符串按照原样进行处理。


pattern = r'<a class="preview".*?</a>'
pattern2 = r'href="(.*?)"'


def askURL(baseurl):
    # 我的初始访问user agent
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息 伪装用的
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }
    # 用户代理表示告诉豆瓣服务器我们是什么类型的机器--浏览器  本质是告诉浏览器我们可以接受什么水平的文件内容
    request = urllib.request.Request(baseurl, headers=head)  # 携带头部信息访问url
    # 用request对象访问
    html = ""
    try:
        response = urllib.request.urlopen(request)  # 用urlopen传递封装好的request对象
        html = response.read().decode("utf-8")  # read 读取 可以解码 防治乱码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)  # 打印错误代码
        if hasattr(e, "reason"):
            print(e.reason)  # 打印错误原因
    return html

# 爬取网页
def getData(baseurl):
    datalist = [] # 保存图片url的所有信息
    html = askURL(baseurl)  # 保存获取到的网页源码
    # print(html)
    #【逐一】解析数据  （一个网页就解析一次）
    soup = BeautifulSoup(html, "html.parser")  # soup是解析后的树形结构对象
    for item in soup.find_all('a'):  # 查找符合要求的字符串形成列表
        # print(item)    #测试查看item全部
        item = str(item)
        url2 = re.findall(pattern, item)  # re正则表达式查找指定字符串 0表示只要第一个 前面是标准后面是找的范围
        # print(url2)
        result = ''.join(url2)
        # print("result",result)
        url3 = re.findall(pattern2,result)
        # print("url3",url3)
        datalist.append(url3)
    filtered_list = [x for x in datalist if x]
    # print("datalist",filtered_list)
    return filtered_list
if __name__ == "__main__":
    main()