import unittest
import PythonTest3
class Mytest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(PythonTest3.sum(10,20),30)
        self.assertEqual(PythonTest3.sum(2,20),22)
        self.assertEqual(PythonTest3.sum(-5,30),25)
        self.assertEqual(PythonTest3.sum(8,2),10)
    
    def test_mul(self):
        self.assertEqual(PythonTest3.mul(5,6),30)
        self.assertEqual(PythonTest3.mul(10,30),300)
        self.assertEqual(PythonTest3.mul(0,6),0)
        self.assertEqual(PythonTest3.mul(5,10),50)
    
    def test_div(self):
        self.assertEqual(PythonTest3.div(5,5),1)
        self.assertEqual(PythonTest3.div(30,6),5)
        self.assertEqual(PythonTest3.div(0,10),0)
        self.assertEqual(PythonTest3.div(100,2),50)
        self.assertRaises(ZeroDivisionError,PythonTest3.div,24,0)
    
if __name__=="__main__":
    unittest.main()

# python -m unittest  -v test_PythonTest3.py