import PythonTest4
def test_sum():
    assert PythonTest4.sum(8,2)==10
    assert PythonTest4.sum(80,4)==84
    assert PythonTest4.sum(5,7)==12
def test_mul():
    assert PythonTest4.mul(5,2)==10
    assert PythonTest4.mul(4,100)==400
    assert PythonTest4.mul(0,500)==0

def test_search_to_list():
    assert PythonTest4.search_to_list([5,6,40],40)==True
    assert PythonTest4.search_to_list([5,6,40],4)==False
    
# pytest  test_PythonTest4.py
# pytest  -v test_PythonTest4.py
# pytest  -m show