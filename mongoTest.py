import pymongo

client = pymongo.MongoClient("mongodb+srv://kaysnow343:Viradha123@cluster0.nrxoquk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "Kanishka",
     "surname" : "kumar",
    "mob":"3897983793"
}

e = {
"name" : "Raj",
     "surname" : "kumar",
    "mob":"3897983793"
},
{
"name" : "Hitesh",
     "surname" : "kumar",
    "mob":"3897983793"
},
{
"name" : "Kanishka",
     "surname" : "kumar",
    "mob":"3897983793"
}

data1={
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}

db1 = client['mongoTest']
coll = db1['test']
coll.insert_one(d)
coll.insert_many(e)
coll.insert_many(data1)