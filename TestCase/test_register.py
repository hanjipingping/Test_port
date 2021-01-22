# _*_coding:utf-8_*_
# @time :2020/11/23 8:37 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :test_register.py
# @software PyCharm
import unittest

import os
import requests
import random

from Common.Excel import Manage_Excel
from Common.handel_path import DATA_DIR
from Common.INI_setting import config
from Common.get_log import mylog_test
from Common.handel_sql import sql_data
from Common import my_ddt

#读取excel数据
excel_data = Manage_Excel(os.path.join(DATA_DIR,config.get('excel','workbook')),config.get('excel','sheet_register'))
case_data = excel_data.get_data()


@my_ddt.ddt
class TestRegister(unittest.TestCase):
    @my_ddt.data(*case_data)
    def test_register(self,case):

        #获取url地址
        url = config.get('request','url') + case["url"]
        #获取请求方法
        method = case["method"]
        #获取头部信息
        headers = eval(config.get('request','headers'))
        #判断手机号是否需要替换
        if "*phone*" in case['data']:
            phone = self.get_phone()
            case['data'] = case['data'].replace("*phone*",phone)
        #获取注册信息
        params = eval(case['data'])
        #获取预期结果
        expected = eval(case["expected"])
        #发送请求
        response = requests.request(method=method,url=url,headers= headers,json= params)
        res = response.json()

        try:
            self.assertAlmostEqual(expected['code'],res['code'])
            #用例校验的sql写在excel中，获取sql
            sql = case["check_sql"]
            if sql :


                res1 = sql_data.find_data(sql.format(params['mobile_phone']))
                
                self.assertTrue(res1)







        except AssertionError as e:
            mylog_test.error(f'{case["title"]}该条测试用例未通过')
            mylog_test.exception(e)
            raise e
        else:
            mylog_test.info(f'{case["title"]}该条用例通过')

    @staticmethod    #生成一个随机手机号
    def get_phone():
        while True:
            phone = '152'
            for i in range(8):
                res = random.randint(0, 9)
                phone += str(res)
            sql = f"select * from futureloan.member where mobile_phone = {phone}"
            sql_phone = sql_data.find_data(sql)
            if not sql_phone:
                return phone













