import urllib.request

url = "http://www.whatismyip.com"

proxy_support = urllib.request.ProxyHandler({'http':'79.190.145.141:3128'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders= [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)