class Fibo:
    def __init__(self , fibo_number):
        self.f1=1
        self.f2=1
        self.fibo_number=fibo_number

    def __iter__(self):
        return self
        
    def __next__(self):
      return self.f1
      self.f1 = self.f2
      self.f2 = self.f1+self.f2
      self.fibo_number-=1
      if self.fibo_number<0:
        raise StopIteration
      return self.f1

fibo1=Fibo(20)
for i in fibo1:
    print(i)