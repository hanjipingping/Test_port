
import unittest
from unittestreport import TestRunner
from common.handle_path import CASE_DIR, REPORT_DIR
from common.handle_config import conf
from tools.tools import init_env_data

# 加载套件
suite = unittest.defaultTestLoader.discover(CASE_DIR)

# 准备一些测试的环境数据
init_env_data()

# 执行用例
runner = TestRunner(suite,
                    filename=conf.get('report', "filename"),
                    report_dir=REPORT_DIR,
                    title='测试报告',
                    tester='韩继平',
                    desc="韩继平执行测试生产的报告",
                    templates=1
                    )
runner.run()


# 发送测试报告到邮箱
runner.send_email(host="smtp.163.com",
                  port=465,
                  user="han0801@163.com",
                  password="IFTLJTCEVOUVBGDM",
                  to_addrs=["hanjiping@300.cn"])
