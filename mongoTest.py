import pymongo

client = pymongo.MongoClient("mongodb+srv://kaysnow343:Viradha123@cluster0.nrxoquk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "Kanishka",
     "surname" : "kumar",
    "mob":"3897983793"
}

db1 = client['mongoTest']
coll = db1['test']
coll.insert_one(d)