"""

审核的前置条件

管理员-->审核:前置管理员登录 （setUpClass）

审核（项目：每次审核之前需要添加一个项目：setup
        添加项目：普通用户登录-->再去添加）



setupclass:
    普通用户登录
    管理员登录
setup:
    使用普通用户添加项目




"""
import os
import random
import unittest

import requests
from jsonpath import jsonpath

from common.handle_data import replace_data
from common.handle_db import db
from common.handle_excel import Excel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common.myddt import ddt, data

from common.handle_config import conf
from testcase import fixture


@ddt
class TestAudit(unittest.TestCase):
    excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "audit")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """审核项目的前置：管理员和普通用户登录"""
        # ----------------普通用户登录----------------
        fixture.setup_login(cls)
        # ----------------管理员用户登录---------------
        fixture.setup_login_admin(cls)

    def setUp(self):
        """添加项目，提取项目id"""
        url = conf.get("env", "base_url") + "/loan/add"
        params = {"member_id": self.member_id,
                  "title": "借钱找对象过七夕",
                  "amount": 2000,
                  "loan_rate": 12.0,
                  "loan_term": 3,
                  "loan_date_type": 1,
                  "bidding_days": 5}
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.token
        response = requests.request(url=url, method="post", json=params, headers=headers)
        res = response.json()
        # 将项目id保存为类属性
        TestAudit.loan_id = jsonpath(res, "$..id")[0]

    @data(*cases)
    def test_audit(self, item):
        # 第一步：准备用例数据
        url = conf.get("env", "base_url") + item["url"]
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.admin_token
        # 替换用例参数
        item["data"] = replace_data(item["data"], TestAudit)
        params = eval(item["data"])
        # 请求方法
        method = item["method"]
        # 预期结果
        expected = eval(item["expected"])
        # 第二步：请求接口，获取实际返回的结果
        response = requests.request(url=url, method=method, json=params, headers=headers)
        res = response.json()
        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            if item["title"] == "审核通过":
                TestAudit.pass_loan_id = params["loan_id"]
            # 进行数据库校验
            if item["check_sql"]:
                sql = item["check_sql"].format(params["loan_id"])
                result = db.find_data(sql)[0]
                self.assertEqual(expected["status"], result["status"])


        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))
