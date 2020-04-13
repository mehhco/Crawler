import urllib.request
response = urllib.request.urlopen("https://www.baidu.com")
html = response.read()
html = html.decode("UTF-8")
print(html)