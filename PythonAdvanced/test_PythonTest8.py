import PythonTest8
import pytest

# @pytest.mark.parametrize('num1,num2,res',[
#     (2,5,7),
#     (6,8,14),
#     (10,20,30),
#     (45,-2,43),
#     (5,60,65)
# ])
# def test_sum(num1,num2,res):
#     assert num1+num2==res

class Person:
    def __init__(self, name,family, age):
      self.name = name
      self.family=family
      self.age = age

@pytest.mark.parametrize("person,l,a",[
    (Person("ali","hoseini",12),2,12),
    (Person("saeid","karami",20),3,17)
])
def test_fun(person,l,a):
    assert len(person.name)>l and person.age>=a
# pytest test_PythonTest8.py