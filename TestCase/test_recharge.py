# _*_coding:utf-8_*_
# @time :2020/11/29 6:02 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :test_recharge.py
# @software PyCharm
import unittest
import requests
import jsonpath
import os
from Common import my_ddt
from Common.Excel import Manage_Excel
from Common.INI_setting import config
from Common.get_log import mylog_test
from Common.handel_path import INI_PATH,DATA_DIR
from Common.handel_sql import sql_data
@my_ddt.ddt
class TestRecharge(unittest.TestCase):

    excel = Manage_Excel(os.path.join(DATA_DIR,config.get('excel','workbook')),config.get('excel','sheet_recharge'))
    # excel_data = Manage_Excel(os.path.join(DATA_DIR, config.get('excel', 'workbook')),
    #                           config.get('excel', 'sheet_register'))
    excel_data = excel.get_data()

    @classmethod
    def setUpClass(cls):

        url = config.get('login_test','url')

        params = {

            "mobile_phone":config.get('login_test','mobile_phone'),
            "pwd":config.get('login_test','password')
        }
        headers = eval(config.get('request','headers'))
        reponse = requests.request(url=url,method='post',json = params,headers=headers)
        res = reponse.json()
        cls.token = 'Bearer ' + jsonpath.jsonpath(res,"$..token")[0]
        cls.id = res['data']['id']


    @my_ddt.data(*excel_data)
    def test_register(self,case):
        #获取请求url地址
        URL = config.get('request','url')  + case['url']
        #获取请求头
        headers = eval(config.get('request','headers'))
        headers["Authorization"] = self.token
        #获取data

        params = eval(case['data'])
        if "#member#" in case['data']:
            params['member_id'] = params['member_id'].replace("#member#",str(self.id))

        #预期结果
        excpted = eval(case['expected'])
        #获取请求方法
        mothed = case['method']



        sql = case["check_sql"]

        if sql :
            start_money = sql_data.find_data(sql.format(self.id))
            s_money = start_money[0]['leave_amount']
        #发送请求
        request = requests.request(method=mothed,json= params,headers=headers,url=URL)
        res = request.json()

        if sql :
            end_money = sql_data.find_data(sql.format(self.id))
            e_money = end_money[0]['leave_amount']

        try:
            #比对预期结果与实际结果
            self.assertEqual(excpted['code'],res['code'])
            if sql:
                self.assertEqual(float(e_money-s_money),params["amount"])
            mylog_test.info(f"{case['title']}这条用例通过")


        except AssertionError as e:
            mylog_test.info(f'{case["title"]}这条用例未通过')

            raise e
