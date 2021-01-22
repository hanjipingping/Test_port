import pytest


#
# def setup():
#     print("-----函数用列的前置setup-----")
#
#
# def teardown():
#     """用例基本的前置"""
#     print("----------函数用列的后置-----------------")
#
#
# def test_demo1_func():
#     print("测试用例：test_demo1_fun")
#     assert 100 == 100
#
#
# def test_func_test():
#     print("测试用例：test_demo1_fun")
#     assert 100 == 100


class TestDome2:

    # def setup(self):
    #     """用例基本的前置"""
    #     print("----------用例级别的前置-----------------")
    #
    # def teardown(self):
    #     """用例基本的前置"""
    #     print("----------用例级别的后置-----------------")

    # def setup_class(self):
    #     """用例基本的前置"""
    #     print("----------测试类级别的前置-----------------")
    #
    # def teardown_class(self):
    #     """用例基本的前置"""
    #     print("----------测试类级别的后置-----------------")

    def test_demo2_method01(self):

        print("测试用例：test_demo2_method01")
        assert 100 == 100

    def test_demo2_method03(self):
        print("测试用例：test_demo2_method03")
        assert 10 in [10, 22, 33]


class Test_Demo2:
    @pytest.mark.main
    def test_00002(self,test_02):
        print('第二个测试用例类')
