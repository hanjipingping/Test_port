
import unittest
import requests
import jsonpath
import os
from Common import my_ddt
from Common.Excel import Manage_Excel
from Common.handel_path import DATA_DIR
from Common.INI_setting import config
from Common.get_log import mylog_test
from Common.handel_sql import sql_data

@my_ddt.ddt
class TestWithDraw(unittest.TestCase):

    #读取excel数据
    excel = Manage_Excel(os.path.join(DATA_DIR,config.get('excel','workbook')),config.get('excel','sheet_withdraw'))
    excel_data = excel.get_data()

    @classmethod
    def setUpClass(cls):
        #前置登陆
        login_url = config.get('login_test','url')
        params = {

            "mobile_phone": config.get('login_test', 'mobile_phone'),
            "pwd": config.get('login_test', 'password')
        }
        headers = eval(config.get('request','headers'))
        response = requests.request(method='post',json = params,headers=headers,url=login_url)
        res = response.json()

        cls.token = 'Bearer ' + jsonpath.jsonpath(res,"$..token")[0]
        cls.id = jsonpath.jsonpath(res,"$..id")[0]



    @my_ddt.data(*excel_data)
    def test_withdraw(self,case):
        #请求url
        url = config.get('request','url') + case['url']
        #请求方法
        method = case['method']
        #请求data
        params = eval(case['data'])
        if "#member_id#" in case['data']:
            params['member_id'] = params['member_id'].replace('#member_id#',str(self.id))
        #请求头
        headers = eval(config.get('request','headers'))
        headers["Authorization"] = self.token

        expected = eval(case['expected'])
        sql = case['check_sql']
        if sql :
            start_money = sql_data.find_data(sql.format(self.id))
            s_money = start_money[0]['leave_amount']
        reponse = requests.request(method = method,json = params,headers =headers,url = url)
        res = reponse.json()

        try :
            if sql :
                end_money = sql_data.find_data(sql.format(self.id))
                e_money = end_money[0]['leave_amount']
                self.assertEqual(float(s_money-e_money),params['amount'])
            self.assertEqual(expected['code'],res['code'])
            mylog_test.info(f'用力执行通过{case["title"]}')

        except AssertionError as e :
            mylog_test.info(f'{case["title"]}执行失败')
            raise e






        pass
