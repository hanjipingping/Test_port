import pytest

@pytest.fixture()
def test_01():
    print('测试的前置条件')
    a = 11
    b = 22
    c = 33
    yield a,b,c
    print('后置')


#
@pytest.fixture(scope='class')
def test_02():
    print('类级别的前置')
    yield
    print('类的后置')
