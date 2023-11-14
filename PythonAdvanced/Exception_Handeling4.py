class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message=message
    def __str__(self) -> str:
        return "Error is : "+self.message+"..."
def avgValid(avg):
    if not isinstance(avg,float ):
        raise MyException("The average is not valid")
    if avg<10 or avg>20:
        raise MyException("Out of range")
    return avg

try:
    avg=avgValid(2.2)
    print(avg)

except MyException as error:
    print(error)