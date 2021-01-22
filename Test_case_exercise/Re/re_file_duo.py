

'''


'''
import re
#{n}:表示前一个字符出现n次
res = re.findall('\d{3}','123456err45rrrff567hhh67890')
print(res)
#{n,m}表示一个字符连续出现n-m次
res1 = re.findall('\d{3,5}','111k1111k11111kkkkk11111111')
print(res1)
#{n,}表示一个字符至少连续出现3次
res2 = re.findall("\d{3,}","123r4567890")
print(res2)
#贪婪模式：python默认是贪婪模式
#非贪婪模式：在表示数量后面加个？，就可以关闭贪婪模式
res3 = re.findall("\d{3,}?","123r4567890")
print(res3)
#+:表示前一个字符最少出现一次
res4 = re.findall("\d+",'123tg456k6k6')
print(res4)
#*表示前一个字符至少出现0次以上
res5 = re.findall("\d*",'asdfgh6j7j8')
print(res5)
