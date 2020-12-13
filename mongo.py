import os
import pymongo
if os.path.exists("env.py"):
    import env


# const in python written in CAPITALS
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


# function to call the connection to mongodb
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB %s") % e


# call connection function
conn = mongo_connect(MONGO_URI)

# set collection name to a variable
coll = conn[DATABASE][COLLECTION]

# find all items in the celebrities collection, it will return a mongodb object called "Cursor"
coll.update_many({"nationality": "british"}, {"$set": {"hair_color": "maroon"}})

documents = coll.find({"nationality": "british"})

# iterate through data
for doc in documents:
    print(doc)
