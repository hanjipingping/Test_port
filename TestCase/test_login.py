# _*_coding:utf-8_*_
# @time :2020/11/23 4:45 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :test_login.py
# @software PyCharm
import unittest
import os
from Common import my_ddt
import requests
from Common.handel_path import DATA_DIR
from Common.Excel import Manage_Excel
from Common.get_log import mylog_test
from Common.INI_setting import config
#读取excel数据
test = Manage_Excel(os.path.join(DATA_DIR,'cases.xlsx'),'login')
test_01 = test.get_data()




@my_ddt.ddt
class TestLogin(unittest.TestCase):


    @my_ddt.data(*test_01)
    def test_login(self,case):
        #准备用例数据
        #获取url
        url = case["url"]
        #获取请求参数params
        params = eval(case['data'])
        #获取预期结果
        expected = eval(case['expected'])
        #获取请求方法
        request_method = case['method']
        #获取请求头信息
        headers = eval(config.get('request', 'headers'))
        #发起请求
        response = requests.request(method=request_method,url=url,json = params,headers = headers)
        #获取返回信息
        res = response.json()

        try:
            #断言，预期结果与实际结果比较
            self.assertAlmostEqual(expected['code'],res["code"])
            self.assertAlmostEqual(expected['msg'],res['msg'])
        except AssertionError as e :
            #错误的用例记录在logging日志中
            mylog_test.error(f'用例{case["title"]}出现错误，错误信息为：{e}')
            mylog_test.exception(e)
            raise e
        else:
            mylog_test.info(f'用例运行正常{case["title"]}')








