"""

"""
import os
import unittest

import requests
from jsonpath import jsonpath
from common.handle_config import conf
from common.handle_db import db
from common.handle_excel import Excel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common.myddt import data, ddt
from common.handle_data import replace_data
from testcase import fixture

@ddt
class TestAdd(unittest.TestCase):
    excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "add")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """写该用例类执行之前的前置
        登录，获取token，和用户id
        """
        fixture.setup_login(cls)


    @data(*cases)
    def test_add(self, item):

        # 第一步：准备用例数据
        url = conf.get("env", "base_url") + item["url"]
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.token
        # 替换用例参数
        item["data"] = replace_data(item["data"], TestAdd)
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
            # 进行数据库校验
            if item["check_sql"]:
                loan_id = jsonpath(res, "$..id")[0]
                sql = item["check_sql"].format(loan_id)
                result = db.find_data(sql)
                self.assertTrue(result)

        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))
