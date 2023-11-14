def sum(num1,num2,num3):
    """
    >>> assert sum(1,2,1) == 6
    
    >>> sum(4,8,6)
    18
    >>> sum(-2,5,10)
    13
     
    """
    
    return num1+num2+num3

def fun(list1):
    """_summary_

    Args:
        list1 (_type_): _description_

    Returns:
        _type_: _description_
    >>> fun([2,5,6])
    60
    >>> fun([4,10,20])
    800
    >>> fun([1,0,80])
    0
    >>> fun([1,-1,2])
    -2
    """
    f=1
    for i in list1:
       f*=i
    return f 
import doctest
if __name__=="__main__":
    doctest.testmod()