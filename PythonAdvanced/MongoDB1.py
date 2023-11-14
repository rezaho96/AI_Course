from pymongo import MongoClient
from pprint import pprint,PrettyPrinter

client=MongoClient("mongodb://localhost:27017/")
print(client)

dbtest=client['test']
print(dbtest)

people=dbtest["people"]
print(people)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
people.delete_many({})
x = people.insert_many(mylist)
print(x.inserted_ids)
print(100*"-")
for db in client.list_database_names():
    print(db)
    
    
print(100*"-")
for collections in dbtest.list_collection_names():
    print(collections)
    
print(100*"-")

for doc in people.find():
    print(doc)
    
print(100*"-")
print(people.count_documents({}))

print(100*"-")
for doc in people.find().limit(2):
    pprint(doc)
    

print(100*"-")
for doc in people.find({"name":"Amy"}):
    pprint(doc)    


people.update_one({"name":"Amy"},{'$set':{"address":"shirza"}})
print(100*"-")
for doc in people.find({"name":"Amy"}):
    pprint(doc) 
    
client.close()