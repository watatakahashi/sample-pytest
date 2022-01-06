import pytest
from module.sample import inc, abs_inc


def test_inc_加算():
    assert inc(3) == 4


def test_inc_数値を渡さない場合にTypeErrorとなる():
    with pytest.raises(TypeError):
        inc('aaa')


def test_abs_inc_0より大きい場合は加算():
    assert abs_inc(3) == 4
