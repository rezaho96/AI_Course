from datetime import date
from khayyam import JalaliDate

def dateConversion():
    jalaliDate1=input("Enter Date (For Example: 1399-06-20):")
    list1=jalaliDate1.split("-") #Separation of date string values
    jalaliDate2=JalaliDate(*list1)
    conversion_jalalidate_to_ADdate=jalaliDate2.todate()
    dateNow=date.today()
    
    yield conversion_jalalidate_to_ADdate
    # Date difference
    yield abs(dateNow-conversion_jalalidate_to_ADdate).total_seconds()/(60*60*24)

# ------------------main---------------
dateConversion1=dateConversion()
print(next(dateConversion1))
print(next(dateConversion1))
    
    