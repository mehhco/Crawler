import re
import time
import urllib.request
import urllib.parse
import json
import os

def get_content(html, str1, title):  # 获得小说的url

    # 获得章节标题
    title = re.findall('.*<h1>(.+?)</h1>.*', html)
    title = str(title).strip('[\'').rstrip('\']')


    # 获得章节内容
    start_content = html.find("<p>&nbsp;&nbsp;&nbsp;&nbsp;")
    end_content = -1
    if start_content != -1:
        start_content = start_content+len("<p>&nbsp;&nbsp;&nbsp;&nbsp;")
        end_content = html.find("</p>", start_content)
        if end_content != -1:
            str1 = html[start_content: end_content]

    str1 = str1.replace("&nbsp;&nbsp;&nbsp;&nbsp;",' ')
    str1 = str1.replace("<br />", ' ')
    str1 = title + '\n'+str1 + '\n' + '*******************' + '\n'
    return str1, title


def url_open(url, head):  # 通用打开网址方法
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_txt(html_url, head):  # 获得网站的网页元素
    html = url_open(html_url, head).decode('utf-8')
    return html


def save_txt(filename, content):
    f = open(filename, 'a+')
    f.write(content)

def download_txt(filename='风流秘史（作者：天一生水）'):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/79.0.3945.130 Safari/537.36 '
    url = "https://www.58utxt.com/read/24437/"
    str1 = []
    title = []

    for i in range(12666926, 12667108):
        html_url = url + str(i) + ".html"  # 获得每个小说章节页的网址
        html = get_txt(html_url, head)  #返回每个网站的网页元素
        content, title = get_content(html, str1, title)
        save_txt(filename, content)

download_txt()
