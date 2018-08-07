from pymongo import MongoClient

mongo_uri = "mongodb://admin:adminc4e@ds049925.mlab.com:49925/c4e"


# 1. Connect yo database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db["games"]

# 4. Create a document
new_game = {
    "title":"LOL",
    "description":"league of legend"
}

# 5. Insert doc into collection
games.insert_one(new_game)



#  6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game["title"])