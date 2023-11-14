shoppingList1 = ["Milk","Cheese","Butter","Tomato","Banana","Apple"]
shoppingList2 = ["Orange","Cheese","Kiwi","Tomato","Banana","Butter"]
def similar_Items(x,y):
    if x==y:
        return x
    else:
        return False
def show_Similar_Items():
    list_similar1=list(map(similar_Items , shoppingList1,shoppingList2))
    list_similar2=list(filter(lambda x:x!=False,list_similar1))
    print(list_similar2)

show_Similar_Items()