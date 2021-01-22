'''



正则表达式
'''

import re
#匹配任意一个字符
res = re.findall('.','123edfrtg')
print(res)
#列举可以匹配的字符[]
res1 = re.findall("[a-z]",'qasdvfd4554646456')
res2 = re.findall("[0-9]",'123456tgbhh')
res3 = re.findall("[0-9a-zA-Z]","qwertg45678HJKIU")
print(res1)
print(res2)
print(res3)
#\d匹配任意一个数字
res4 = re.findall('\d','123456thb')
res5 = re.findall('\D','1234edfr')
print(res4)
print(res5)
#\s匹配任意一个空白字符
res6 = re.findall('\s','     11222')
res7 = re.findall('\S','   dddddd')
print(res6)

#匹配任意一个单词字符：w(数字字母下划线)
res8 = re.findall('\w','1234erdfgfg')
print(res8)

