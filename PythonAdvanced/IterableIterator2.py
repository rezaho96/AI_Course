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
      self.start += 1
      return x

c1=Counter(1,5)
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))