import pytest
from tetrika_test.task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_sum_two_ok():
    assert sum_two(1, 2) == 3

def test_sum_two_wrong_type():
    with pytest.raises(TypeError):
        sum_two(1, 2.5)

@strict
def concat(a: str, b: str) -> str:
    return a + b

def test_concat_ok():
    assert concat("foo", "bar") == "foobar"

def test_concat_wrong_type():
    with pytest.raises(TypeError):
        concat("foo", 7)
