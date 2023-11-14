def ageValid(age):
    if not isinstance(age,int):
        raise RuntimeError("The age is not valid...")
    if age<1 or age>120:
        raise RuntimeError("Out of range...")
    return age

try:
    age=ageValid(2)
    print(age)

except RuntimeError as error:
    print(error)