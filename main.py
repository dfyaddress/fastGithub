import time
import os
from urllib import request
from bs4 import BeautifulSoup


def getAdder(site, select):
    url = "https://www.ipaddress.com/site/" + site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode('utf-8')
    # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(page_info, 'html.parser')
    x = soup.select(select)
    adder = x[0].string
    return adder


if __name__ == '__main__':
    hosts = ["github.com", "assets-cdn.github.com", "github.global.ssl.fastly.net"]
    selects = ['body > div.resp.main > main > section:nth-child(7) > table > tbody > tr:nth-child(8) > td > ul > li',
               'body > div.resp.main > main > section:nth-child(8) > div:nth-child(8) > table > tbody > tr:nth-child(6) > td > ul > li',
               'body > div.resp.main > main > section:nth-child(8) > div > table > tbody > tr:nth-child(6) > td > ul > li:nth-child(1)']
    result = ""
    print("开始查询.....")
    for i in range(len(hosts)):
        print("开始查询" + hosts[i])
        string = getAdder(hosts[i], selects[i]) + "  " + hosts[i]
        print(hosts[i] + "查询成功，结果为：" + string)
        result = result + string + "\n"
        if i < len(hosts) - 1:
            print("开始睡眠...")
            time.sleep(5)
            print("睡眠结束")

    print("写入host文件")
    host_file = open('C:\Windows\System32\drivers\etc\hosts', 'w')
    host_file.writelines(result)
    host_file.close()
    print("写入成功")

    print("开始刷新缓存...")
    os.system('ipconfig /flushdns')
    print("刷新完成")
