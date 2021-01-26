"""


"""
# import os
# import unittest
#
# import requests
#
# from common.handle_config import conf
# from common.handle_db import db
# from common.handle_excel import Excel
# from common.handle_log import log
# from common.handle_path import DATA_DIR
# from common import myddt
# from jsonpath import jsonpath
# from common.handle_data import replace_data
#
#
# @myddt.ddt
# class TestWithdraw02(unittest.TestCase):
#     excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "withdraw02")
#     cases = excel.read_data()
#
#     @myddt.data(*cases)
#     def test_withdraw(self, item):
#         # 第一步：准备数据
#         url = conf.get("env", "base_url") + item["url"]
#         # 判断是否有数据需要替换
#         item["data"] = replace_data(item["data"], TestWithdraw02)
#         # 参数
#         params = eval(item["data"])
#         # 请求方法
#         method = item["method"]
#         # 请求头
#         headers = eval(conf.get("env", "headers"))
#         # 注意点：要区分用例是否要在请求头中加token
#         if item["interface"] == "withdraw":
#             headers["Authorization"] = self.token
#         # 预期结果
#         expected = eval(item["expected"])
#         sql = item["check_sql"]
#
#         if sql:
#             s_amount = db.find_data(sql.format(self.member_id))
#             s_money = s_amount[0]["leave_amount"]
#
#         # 第二步：发送请求
#         response = requests.request(url=url, method=method, json=params, headers=headers)
#         res = response.json()
#         if item["interface"] == "login":
#             # 提取token和用户id保存为类属性
#             TestWithdraw02.token = "Bearer" + " " + jsonpath(res, "$..token")[0]
#             TestWithdraw02.member_id = jsonpath(res, "$..id")[0]
#
#         print("预期结果：", expected)
#         print("实际结果：", res)
#
#         # 第三步：断言
#         try:
#             self.assertEqual(expected["code"], res["code"])
#             self.assertEqual(expected["msg"], res["msg"])
#             if sql:
#                 e_amount = db.find_data(sql.format(self.member_id))
#                 e_money = e_amount[0]["leave_amount"]
#                 self.assertEqual(float(s_money - e_money), params["amount"])
#
#         except AssertionError as e:
#             log.error("用例{}，执行未通过".format(item["title"]))
#             log.exception(e)
#             raise e
#         else:
#             log.info("用例{}，执行通过".format(item["title"]))
