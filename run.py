# _*_coding:utf-8_*_
# @time :2020/11/23 5:23 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :run.py
# @software PyCharm
import unittest
import os
from Common.handel_path import CASE_DIR,REPORT_DIR
from unittestreport import TestRunner


suite = unittest.defaultTestLoader.discover(CASE_DIR)


runner = TestRunner(
    suite,
    filename='接口测试报告',
    report_dir= REPORT_DIR,
    title= '韩继平测试报告',
    tester= 'jiping han',
    desc= "jiping 执行的测试报告",
    templates=2
)
runner.run()