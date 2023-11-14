class Counter:
    def __init__(self, start , end):
        self.start=start
        self.end=end
    
    def __iter__(self):
      return self

    def __next__(self):
      x = self.start
      if x>self.end:
        raise StopIteration
      self.start += 3
      return x
# -----------main------------
counter1=Counter(10,100)
for i in counter1:
    print(i)