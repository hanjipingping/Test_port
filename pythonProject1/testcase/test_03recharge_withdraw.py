"""


快捷包导入： alt+ enter
用例设计尽量保持独立性
"""
import os
import unittest

import requests

from common.handle_config import conf
from common.handle_db import db
from common.handle_excel import Excel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common import myddt
from jsonpath import jsonpath
from common.handle_data import replace_data
from testcase import fixture


@myddt.ddt
class TestRecharge(unittest.TestCase):
    excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "recharge")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """写该用例类执行之前的前置
        登录，获取token，和用户id
        """
        fixture.setup_login(cls)

    @myddt.data(*cases)
    def test_recharge(self, item):
        # 第一步：准备数据
        url = conf.get("env", "base_url") + item["url"]
        # 请求参数
        item["data"] = replace_data(item["data"], TestRecharge)
        params = eval(item["data"])
        # 请求头
        headers = eval(conf.get("env", "headers"))
        # 请求头中要添加token
        headers["Authorization"] = self.token
        # 请求方法
        method = item["method"]
        # 预期结果
        expected = eval(item["expected"])
        sql = item["check_sql"]
        if sql:
            s_amount = db.find_data(sql.format(self.member_id))
            s_money = s_amount[0]["leave_amount"]
        # 第二步：请求接口，获取结果
        response = requests.request(url=url, method=method, json=params, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)

        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

            if sql:
                e_amount = db.find_data(sql.format(self.member_id))
                e_money = e_amount[0]["leave_amount"]
                self.assertEqual(float(e_money - s_money), params["amount"])

        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))


@myddt.ddt
class TestWithdraw(unittest.TestCase):
    excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "withdraw")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """写该用例类执行之前的前置
        登录，获取token，和用户id
        """
        fixture.setup_login(cls)

    @myddt.data(*cases)
    def test_withdraw(self, item):
        # 第一步：准备数据
        url = conf.get("env", "base_url") + item["url"]
        # 请求参数
        item["data"] = replace_data(item["data"], TestWithdraw)
        params = eval(item["data"])
        # 请求头
        headers = eval(conf.get("env", "headers"))
        # 请求头中要添加token
        headers["Authorization"] = self.token
        # 请求方法
        method = item["method"]
        # 预期结果
        expected = eval(item["expected"])
        sql = item["check_sql"]
        if sql:
            s_amount = db.find_data(sql.format(self.member_id))
            s_money = s_amount[0]["leave_amount"]
        # 第二步：请求接口，获取结果
        response = requests.request(url=url, method=method, json=params, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)

        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

            if sql:
                e_amount = db.find_data(sql.format(self.member_id))
                e_money = e_amount[0]["leave_amount"]
                self.assertEqual(float(s_money - e_money), params["amount"])

        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))
