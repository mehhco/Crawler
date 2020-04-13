import urllib.request
req = urllib.request.Request("http://placekitten.com/g/1024/600")
response = urllib.request.urlopen(req)
cat_img = response.read()

with open("cat_download.jpg", 'wb') as f:
    f.write(cat_img)

print(response.geturl())
print(response.info())
print(response.getcode())