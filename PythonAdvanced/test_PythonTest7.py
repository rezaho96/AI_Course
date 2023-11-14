import PythonTest7
import pytest

@pytest.fixture
def input_value():
    list1=[5,6,10,4,80,20,45]
    return list1

def test_sum(input_value):
    assert PythonTest7.sum(2,3)==input_value[2]
    assert PythonTest7.sum(8,10) in input_value
    assert PythonTest7.sum(1,6)==len(input_value)
# pytest test_PythonTest7.py