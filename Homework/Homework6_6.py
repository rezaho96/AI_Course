import collections
MobileStore=collections.namedtuple("MobileStore","brand model price colors")
mobile1=MobileStore("Apple","iphon14",20000,["red","blue"])
mobile2=MobileStore("Apple","iphon14 pro",22000,["black","blue"])
mobile3=MobileStore("Apple","ipad Air 2022",25000,["red","blue","green","yelow"])
mobile4=MobileStore("Apple","ipad 2022",24000,["red","blue","green","yelow"])
mobile5=MobileStore("samsung","j7",6000,["black"])
mobile6=MobileStore("samsung","A10",8000,["brown","white"])
mobile7=MobileStore("samsung","A12",9000,["black","white"])
mobile8=MobileStore("samsung","A21",12000,["black","white","brown"])
mobile9=MobileStore("nokia","G60",10000,["green","white","red"])
mobile10=MobileStore("nokia","X30",9000,["black","red","blue"])

mobile_list=[mobile1,mobile2,mobile3,mobile4,mobile5,mobile6,mobile7,mobile8,mobile9,mobile10]

for item in mobile_list:
    print(item._asdict())
