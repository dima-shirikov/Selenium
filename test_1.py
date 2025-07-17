import pytest

@pytest.mark.parametrize('x', [1, 2, 4, 7, 9, 11])
def test_a(x):
    assert x < 10

@pytest.mark.parametrize('x', [1, 2, 4, 7, 9, 11])
@pytest.mark.parametrize('y', [1, 2, 4, 7, 9, 11])
def test_b(x, y):
    assert x < 10
    assert y < 9