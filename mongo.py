import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# new_doc = {"first": "billy", "last": "munger", "dob": "11/03/1992", "gender": "m", "hair_color": "black", "occupation": "racing_driver", "nationality": "british"}

# coll.insert_one(new_doc)

# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "11/03/1957",
#     "gender": "m",
#     "hair_color": "black",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "11/03/1954",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "british"
# }]

# coll.insert_many(new_docs)

# find something specific
# documents = coll.find({"first": "douglas"})

# remove something specific
# coll.remove_one({"first": "douglas"})

# update the first item with nationality american
# coll.update_one({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

update all items with nationality american
coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

# change geroge rr martin nationality to american
# coll.update_one({"last": "rr martin"}, {"$set": {"nationality": "american"}})

# find everything
# documents = coll.find()

# find any items with nationality = american
documents = coll.find({"nationality": "american"})


for doc in documents:
    print(doc)
