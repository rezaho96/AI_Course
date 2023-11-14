import json
class Food_Menu:
    def __init__(self, foodName, foodCode, foodPrice, foodIngredients):
      self.foodName=foodName
      self.foodCode=foodCode
      self.foodPrice=foodPrice
      self.foodIngredients=foodIngredients
    def __str__(self):
       return f"{self.foodName}\t{self.foodCode}\t{self.foodPrice}\t{self.foodIngredients}"

# ---------main--------
# Object definition
foodMenu1=Food_Menu("ghorme",1,120000,["lobia","rob","gosht"])
foodMenu2=Food_Menu("gheime",2,100000,["nokhod","rob","gosht","sibzamini"])
foodMenu3=Food_Menu("abgosht",3,80000,["lape","rob","goshtMorgh","sibzamini","sabzi"])
foodMenu4=Food_Menu("kabab",4,70000,["goje","gosht"])
foodMenu5=Food_Menu("khorak sabzijat",5,60000,["kaho","kalam","lobia sabz"])
foodMenu6=Food_Menu("kobide",6,130000,["gosht gosfand","brenj","goje","somagh"])
foodMenu7=Food_Menu("joje",7,140000,["gosht morgh","brenj","goje"])
foodMenu8=Food_Menu("ratatoy",8,95000,["non pitza","kado","gharch"])
foodMenu9=Food_Menu("shirbrenj",9,50000,["shir","brenj"])
foodMenu10=Food_Menu("sandvich hamber",10,110000,["hamberger","noon","goje","khiarshor","kaho"])
list1=[foodMenu1.__dict__,foodMenu2.__dict__,foodMenu3.__dict__,foodMenu4.__dict__,foodMenu5.__dict__,foodMenu6.__dict__,foodMenu7.__dict__,foodMenu8.__dict__,foodMenu9.__dict__,foodMenu10.__dict__]

# ***Save to file***
with open(r"Homework\foodMenu.json","w") as file1:
    json.dump(list1,file1,indent=2)
    
  