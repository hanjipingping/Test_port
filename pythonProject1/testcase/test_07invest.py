"""

投资：
    前置：需要有一个状态处于竞标中的项目（登录-->添加项目--->审核通过）
        登录--->投资

    借款人：添加项目
    管理员：审核项目
    投资人：投资
    普通用户：既可以借款，又可以投资


用户登录：setupclass:
添加项目：setupclass:
审核项目：setupclass:

用例逻辑中：投资


用例执行完之后，如果数据库中涉及到多张表的数据变动，如何去进行校验
那些表，那字段发送了变化
1、投资表中新增一条数据？--->用例执行前后 根据用户和标id查询投资记录的条数
2、用户表中可用余额减少？--->用例执行前后查数据库中的余额进行比对？
3、流水记录表中新增一条数据？  --->用例执行前后 根据用户id查询流水记录的条数




"""
import os
import unittest

import requests

from common.handle_config import conf
from common.handle_data import replace_data
from common.handle_db import db
from common.handle_excel import Excel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common.myddt import ddt, data
from testcase import fixture


@ddt
class TestInvest(unittest.TestCase):
    """投资项目的接口"""
    excel = Excel(os.path.join(DATA_DIR, "cases.xlsx"), "invest")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """投资接口的前置条件"""
        # 1、登录(三个用户)
        # 管理员
        fixture.setup_login_admin(cls)
        # 借款人
        fixture.setup_login(cls)
        # 投资人
        fixture.setup_login_invest(cls)
        # 2、添加项目(借款人)
        """添加项目，提取项目id"""
        fixture.setup_add(cls)
        # 3、审核项目(管理员)
        aduit_url = conf.get("env", "base_url") + "/loan/audit"
        params = {"loan_id": cls.loan_id,
                  "approved_or_not": True
                  }
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = cls.admin_token
        response = requests.request(url=aduit_url, method="patch", json=params, headers=headers)
        # print("审核的结果：", response.json())

    @data(*cases)
    def test_invest(self, item):
        """执行投资的用例"""
        # 第一步：准备用例数据
        url = conf.get("env", "base_url") + item["url"]
        params = eval(replace_data(item["data"], TestInvest))
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.invest_token
        method = item["method"]
        expected = eval(item["expected"])
        # 用例执行之前查询sql
        if item["check_sql"]:
            # 查询投资表记录
            sql1 = "SELECT * FROM futureloan.invest WHERE member_id={} and loan_id={}".format(self.invest_member_id,
                                                                                              self.loan_id)
            # 查询用户余额
            sql2 = "SELECT leave_amount FROM futureloan.member where id={}".format(self.invest_member_id)
            # 查询流水记录
            sql3 = "SELECT * FROM futureloan.financelog WHERE pay_member_id={}".format(self.invest_member_id)
            # 查询
            # 用例执行之前投资记录的条数
            s_invest = len(db.find_data(sql1))
            # 用例执行之前投资用户的余额
            s_amount = db.find_data(sql2)[0]["leave_amount"]
            # 用例执行之前流水记录表用户的的流水记录条数
            s_financelog = len(db.find_data(sql3))

        # 第二步：请求接口，获取实际结果
        response = requests.request(url=url, method=method, headers=headers, json=params)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", response.text)
        # 第三步：断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            # 用例执行之前查询sql
            if item["check_sql"]:
                # 查询投资表记录
                sql1 = "SELECT * FROM futureloan.invest WHERE member_id={} and loan_id={}".format(self.invest_member_id,
                                                                                          self.loan_id)
                # 查询用户余额
                sql2 = "SELECT leave_amount FROM futureloan.member where id={}".format(self.invest_member_id)
                # 查询流水记录
                sql3 = "SELECT * FROM futureloan.financelog WHERE pay_member_id={}".format(self.invest_member_id)
                # 查询
                # 用例执行之后投资记录的条数
                e_invest = len(db.find_data(sql1))
                # 用例执行之后投资用户的余额
                e_amount = db.find_data(sql2)[0]["leave_amount"]
                # 用例执行之后流水记录表用户的的流水记录条数
                e_financelog = len(db.find_data(sql3))
                # 断言比对
                # 1、比对执行前后投资表记录数量是否+1
                self.assertEqual(1, e_invest - s_invest)
                # 2、对比用户余额
                self.assertEqual(params["amount"], s_amount - e_amount)
                # 3、比对执行前后流水记录表记录数量是否+1
                self.assertEqual(1, e_financelog - s_financelog)

        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))



