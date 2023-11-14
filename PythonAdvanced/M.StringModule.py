import string
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable)
print(string.capwords("ali hasan hosein moHamAd"))
str1="gon vay hay hoMa"
print(str1.title())
template1=string.Template("Answer is: $x > $y")
print(template1.substitute(x=7,y=2))