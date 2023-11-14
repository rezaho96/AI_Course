import PythonTest5
import pytest

@pytest.mark.A
def test_sum():
    assert PythonTest5.sum(8,2)==10

@pytest.mark.B
def test_mul():
    assert PythonTest5.mul(4,100)==400
  
@pytest.mark.A
def test_search_to_list():
    assert PythonTest5.search_to_list([5,6,40],40)==True
    assert PythonTest5.search_to_list([5,6,40],4)==False

# if __name__=="__main__":
#     pytest.main()    

# pytest test_PythonTest5.py -m A
# pytest test_PythonTest5.py :: test_sum