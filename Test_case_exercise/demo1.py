# _*_coding:utf-8_*_
# @time :2020/11/18 5:01 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo1.py
# @software PyCharm
import unittest

import ddt
data = [1,2,3,4,5]
@ddt.ddt()
class Test_case():
    pass
    # @ddt.data(*data)
    # def test_demo1(self,case):
    #     print(f'-------case{case}-------')
print(Test_case.__dict__.items())

# if __name__ =="__main__":
#     unittest.main()
#     print(Test_case.__dict__.items())
