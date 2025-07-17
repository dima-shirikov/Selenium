import pytest

@pytest.mark.parametrize('num', range(-100, 101))
def test_square(num):
    res = 0
    for k in range(num):
        res += num
    assert res == num**2