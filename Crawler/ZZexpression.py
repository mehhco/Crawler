import re
print(re.search(r'hhc', 'i love hhc'))
print(re.search(r'.', 'I love hhc.com'))  # . 代表换行符以外的任何字符
print(re.search(r'\.', 'I love hhc.com'))  # . 代表换行符以外的任何字符,使用\ 表示原本意思
print(re.search(r'\d', 'I love 23 hhc.com'))  # \d代表任何一个数字
print(re.search(r'\d\d', 'I love 23 hhc.com'))  # \d代表任何一个数字
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.000.123'))
print(re.search(r'[aeIou]','i love hhc'))   #[] 表示字符集 任意一个满足都可以
print(re.search(r'[a-z]','i love hhc'))   # - 表示范围
print(re.search(r'[1-19]','i love 12 hhc'))
print(re.search(r'abc{3}s','abccs')) #{}表示重复次数
print(re.search(r'abc{3}s','abcccs'))
print(re.search(r'abc{3,10}s','abcccccs')) #{}表示重复次数的范围

# 查找0-255以内的数字 比如188
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '199'))


# 查找ip地址
print(re.search('([01]{0,1}\d{0,1}\d{0,1}|2[0-4]\d|25[0-5]\.){3}([01]{0,1}\d{0,1}\d{0,1}|2[0-4]\d|25[0-5])','192.168.001.001'))

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配