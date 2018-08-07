import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
database = client.get_default_database()
customers = database["customers"]
all_customer = customers.find()




references = {"Advertisements" : 0, "Events" : 0, "Word of mouth" : 0}
for customer in all_customer:
    if customer["ref"] == "Events":
        references["Events"] += 1
    elif customer["ref"] == "Advertisements":
        references["Advertisements"] += 1
    else:
        references["Word of mouth"] += 1





for key, value in references.items():
    print("Number of customers by {}: {}".format(key, value))





labels = ["Event", "Advertisements", "Word of mouth"]
colors = ["yellow", "black", "red"]
pyplot.pie(references.values() , labels = references.keys(),colors=colors)
pyplot.axis("equal")
pyplot.show()