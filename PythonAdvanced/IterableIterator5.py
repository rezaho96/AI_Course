class TestIter:
    def __init__(self, list1):
      self.list1=list1
      self.it_list1=iter(self.list1)

    def __iter__(self):
        return self.it_list1
    

    def __call__(self):
       return next(self.it_list1)

t1=TestIter([2,50,60,304,10,5,0,20,40,50,60,80,70])
ittest=iter(t1,80)
for i in ittest:
    print(i)