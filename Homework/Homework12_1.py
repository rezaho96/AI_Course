import json
from pymongo import MongoClient
from pprint import pprint



with open("Homework/score_information.json","r") as file1:
    list_information=json.load(file1)

client=MongoClient("mongodb://localhost:27017/")
dbstudent=client['student']
score=dbstudent["score"]

score.delete_many({})
x = score.insert_many(list_information)

# The exam score is more than 50
for doc in score.find({'scores':{"$elemMatch":{'type': "exam"  ,"score":{'$gt':50}}}}):
    pprint(doc)
print("*"*50)
# course code =16
for doc in score.find({'course_Code': 16}):
    pprint(doc)
print("*"*50)
# The homework score lower than 20 and course code =28
for doc in score.find({"$and":[{'scores':{"$elemMatch":{'type': "homework"  ,"score":{'$lt':20}}} , 'course_Code': 28}]}):
    pprint(doc)
print("*"*50)
 
#  replace exam score = 0 with exam score=10
score.update_one({'scores':{"$elemMatch":{'type': "exam"  ,"score":0}}},{'$set':{'scores.$.score':10}})  
for doc in score.find({'scores':{"$elemMatch":{'type': "exam"  ,"score":10}}}):
    pprint(doc)
print("*"*50)

# add "grade" field to exam score more than 90
score.update_many({'scores':{"$elemMatch":{'type': "exam"  ,"score":{"$gt":90}}}},{'$set':{'grade':'A'}}, upsert=False, array_filters=None)
for doc in score.find({'scores':{"$elemMatch":{'type': "exam"  ,"score":{"$gt":90}}}},{"_id":False}):
    pprint(doc)
print("*"*50)

# create json file
with open("Homework/grade_A.json","w") as file1:
    for doc in score.find({'scores':{"$elemMatch":{'type': "exam"  ,"score":{"$gt":90}}}},{"_id":False}):
        json.dump(doc,file1,indent=4)

client.close()

