import pymongo

client = pymongo.MongoClient("mongodb+srv://kaysnow343:Viradha123@cluster0.nrxoquk.mongodb.net/?retryWrites=true&w=majority")
db= client.test

d =[
    {
        "item" : "Computer",
        "qty" : 86,
        "size" : {"l" : 96, "b" : 43, "uom" : "cm"},
        "status" : "A"
    },
{
        "item" : "Printer",
        "qty" : 25,
        "size" : {"l" : 100, "b" : 25, "uom" : "cm"},
        "status" : "B"
    },
{
        "item" : "Camera",
        "qty" : 67,
        "size" : {"l" : 20, "b" : 43, "uom" : "cm"},
        "status" : "A"
    },
{
        "item" : "Fax",
        "qty" : 10,
        "size" : {"l" : 1000, "b" : 800, "uom" : "cm"},
        "status" : "B"
    },
{
        "item" : "mic",
        "qty" : 1020,
        "size" : {"l" : 21, "b" : 19, "uom" : "cm"},
        "status" : "C"
    },
{
        "item" : "keyboard",
        "qty" : 1700,
        "size" : {"l" : 40, "b" : 23, "uom" : "cm"},
        "status" : "A"
    },
{
        "item" : "mouse",
        "qty" : 1234,
        "size" : {"l" : 10, "b" : 8, "uom" : "cm"},
        "status" : "C"
    },
{
        "item" : "tablet",
        "qty" : 56,
        "size" : {"l" : 63, "b" : 18, "uom" : "cm"},
        "status" : "A"
    }
]

database = client['inventory']
collection = database["table"]
#collection.insert_many(d)
e = collection.find()
#f = collection.find({"status" : {'$in':["A","B"]}})
#g = collection.find({"status" : {"$gt" : "B"}}
#h= collection.find({"qty": {"$gt" : 100}})
#j= collection.find({"item":"Fax"},{"qty":10})
#k=collection.find({"$or": [{"item":"Fax"},{"qty":{"$gte" : 95}}]})
#collection.update_one({"item":"Fax"},{"$set":{"item":"refrigretor"}})
collection.delete_one({"item":"refrigretor"})
for i in e:
    print(i)
