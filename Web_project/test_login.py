import unittest
import ddt
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from page import logIn_page
from page import index_page


data = [
    {"phone": "", "password": "python", "excepted": "请输入手机号"},
    {"phone": "18684720553", "password": "", "excepted": "请输入密码"},

]


@ddt.ddt()
class TestLodin(unittest.TestCase):
    def setUp(self):
        '''登录前的前置，启动浏览器'''
        self.driver = Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.login = logIn_page.Login_page(self.driver)
        self.index = index_page.Index_page(self.driver)

    def test_login(self):
        self.login.login('18684720553', 'python')
        self.assertTrue(self.index.is_login())

    @ddt.data(*data)
    def test_login_phone_none(self, case):
        self.login.login(case['phone'], case['password'])
        res = self.login.get_page_erroe_info()
        self.assertEqual(case['excepted'], res)

    def tearDown(self):
        self.driver.quit()
