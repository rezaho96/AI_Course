#کلاس  : وقتی کلاس دارای نمونه های کمی باشد از این نوع کلاس استفاده میکنیم مثل روزهای هفتهEnum

import enum
from turtle import color
 
class Color(enum.Enum):
    blue=1
    red=2
    black=3
    brown=4


print(Color.blue.value)

class Animals(enum.Enum):
    dog=50
    cat=20
    doncy=100


print(Animals.dog.valuue)