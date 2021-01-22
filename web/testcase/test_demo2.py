import pytest

aa = [
    11, 22, 33, 44
]

@pytest.mark.main
@pytest.mark.parametrize('case',aa)
def test_demo2(case):
    print(case)
    assert case == 11


