import PythonTest6
import pytest

class TestCode:
    @pytest.mark.A
    def test_sum(self):
        assert PythonTest6.sum(8,2)==10

    @pytest.mark.B
    def test_mul(self):
        assert PythonTest6.mul(4,100)==400
    
    @pytest.mark.A
    def test_search_to_list(self):
        assert PythonTest6.search_to_list([5,6,40],40)==True
        assert PythonTest6.search_to_list([5,6,40],4)==False
class TestCode1:
    @pytest.mark.B
    def test_mul(self):
        assert PythonTest6.mul(6,5)==30

# pytest test_PythonTest6.py -m B
# pytest test_PythonTest6.py::TestCode1::test_mul
# pytest test_PythonTest6.py::TestCode::test_sum
# pytest test_PythonTest6.py::TestCode -m A
# pytest -vv test_PythonTest6.py --durations=4 --durations-min=1
