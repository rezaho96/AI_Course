customer_List = ["Sara Ahmadi","Ali Rezaee","Bahar Sadr","Ahmad Majedpoor","Iman Mohammadi","Mina Bavandpoor","Mohammad Alimoradi","Majid Rafiee","Sima Sefidiyan"]
customer_Special = ["Vahid Abdoli","Ali Rezaee","Bahar Sadr","Sima Sefidiyan"]
def filter_costumer(x):
    for item in customer_Special:
        if x==item:
          return x
print("output")
print("-------------")
print(list(filter(filter_costumer,customer_List)))