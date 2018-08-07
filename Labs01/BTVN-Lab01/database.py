from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
database = client.get_default_database()
posts = database["posts"]
new_posts = {
    "title" : "Deep",
    "author" : "Huyqh",
    "content" : "The people came out from the storm, they became stronger, but heartless."
}
posts.insert_one(new_posts)