def printMassage(*args):
    name,family,_,massage=args
    print(f"Dear\t{name} {family},\n{massage}")
def check_Birth_Date(*args):
    list_input=list(args)
    birth_date_year=list_input[2].split("/")[0]

    if int(birth_date_year) <=1340:
        list_input.append("You are now eligible for the COVID-19 vaccine.")
    else:
        list_input.append("You are not eligible for the COVID-19 vaccine now.")
    printMassage(*list_input)

# -----output-----
print(f"output")
print("-----------")
check_Birth_Date("Nazanin","Akbari","1338/12/18")
print("*********************")
check_Birth_Date("Kamran","Mohamadi","1355/12/18")