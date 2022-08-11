import pymongo
client = pymongo.MongoClient("mongodb+srv://kaysnow343:Viradha123@cluster0.nrxoquk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db= client['mongoTest']
collection = db["Json"]

record = collection.find({"name" : "Old Fashioned"})
for i in record:
    print(i)