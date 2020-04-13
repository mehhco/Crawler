import time
import urllib.request
import urllib.parse
import json


while True:

    content = input('请输入需要翻译的内容(输入q!退出程序)')
    if content == 'q!':
        break

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = content
    data['from']= 'AUTO'
    data['to']='AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']='15799507550928'
    data['sign']= '2bd2cfc12b84cc6d136b04420864eb96'
    data['ts']= '1579950755092'
    data['bv']= '901200199a98c590144a961dac532964'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data, head)
    # or req.add_header(head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print(type(target))
    print(target["translateResult"])
    time.sleep(5)