
import requests
import os
import unittest

from common.handle_config import conf
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
from common import myddt
from common.handle_log import log
from common.handle_data import replace_data

file_path = os.path.join(DATA_DIR, "cases.xlsx")


@myddt.ddt
class TestLogin(unittest.TestCase):
    excel = Excel(file_path, "login")
    cases = excel.read_data()

    @myddt.data(*cases)
    def test_login(self, item):
        # 第一步：准备用例数据
        # 接口地址
        url = conf.get("env", "base_url") + item["url"]
        # 请求头
        headers = eval(conf.get("env", "headers"))
        # 请求参数
        item["data"] = replace_data(item["data"], TestLogin)
        params = eval(item["data"])
        # 预取结果
        expected = eval(item["expected"])
        # 请求方法
        method = item["method"]
        # 第二步：调用接口，获取实际结果
        response = requests.request(method, url=url, json=params, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", response.text)
        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))
