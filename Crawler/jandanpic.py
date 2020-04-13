import re
import time
import urllib.request
import urllib.parse
import json
import os


def get_url(html, list1):  # 获得图片的url
    # p = r'{"img":"([^"]+\.jpg)'
    # imglist = re.findall(p, html)
    # for each in imglist:
    #     print(each)               获得图片地址

    p = r'(?:(?:[0,1]?\d?\d|2[0,4]\d|23[0,5])\.){3}(?:[0,1]?\d?\d|2[0,4]\d|23[0,5]\.)'

    a = html.find('var imgList = [[')
    b = -1
    if a != -1:
        a = a + 16
        b = html.find('];', a)
        if b != -1:
            String1 = html[a:b]
            String1 = String1.split(',')
            for i in range(len(String1)):
                end = String1[i].find('.jpg')
                stt = String1[i][17:end + 4]
                stt1 = stt.strip('/')
                stt2 = stt1.replace('\\', '')
                stt3 = "http://" + stt2
                print(stt3)
                list1.append(stt3)
        else:
            pass
    else:
        pass
    return list1


def url_open(url, head):  # 通用打开网址方法
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_pic(html_url, head):  # 获得网站的网页元素
    html = url_open(html_url, head).decode('utf-8')
    return html


def save_img(url_pic, head, name):
    page = url_open(url_pic, head)
    with open("plmm" + str(name) + ".jpg", 'wb') as f:
        f.write(page)


def download_mm(folder='XXOO2', pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/79.0.3945.130 Safari/537.36 '
    url = "http://www.meinvtu.site/detail-id-"

    for i in range(3000, 3005):
        list1 = []
        html_url = url + str(i) + ".html"
        html = get_pic(html_url, head)
        list2 = get_url(html, list1)
        for j in range(len(list2)):
            save_img(list2[j], head, str(i) + '--' + str(j))


download_mm()
