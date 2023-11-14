def sum(datatype,*args):
    if (datatype=="int"):
        s=0
    elif(datatype=="str"):
        s=""
    for item in args:
        s+=item
    return s

print(sum("int",2,5,6))
print(sum("str","ali","\tsaeid","\tvahid"))