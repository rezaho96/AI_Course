class Company:
    def __init__(self, managerName , address , numberEmployees , income, companyName="XYZ"):
      self.companyName=companyName
      self.managerName=managerName
      self.address=address
      self.numberEmployees=numberEmployees
      self.income=income
    
    def productivity(self):
        return self.income/self.numberEmployees
    
    def __str__(self):
        return f'''CompanyName:{self.companyName}\tManagerName: {self.managerName}\t
        Address: {self.address}\tNumber of emplyees:{self.numberEmployees}\tIncome: {self.income}'''

company1=Company("Saeid","shiraz/kazeron",150,600)
print(company1)
print("................................................")
print(company1.productivity())
      