from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json



uri = "mongodb+srv://scarlett:hackathon2023@cluster1.gmttnh0.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["hackathon_2023"]
# Send a ping to confirm a successful connection


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

### Colby's data
f = open('/Users/scarlett/PycharmProjects/hackathon_2023/data/queryStats_transformed.json')
data = json.load(f)
mycol1 = mydb["querystats_transformed"]
for i in data:
    try:
        x = mycol1.insert_one(i)
        #print list of the _id values of the inserted documents:
        # print(x.inserted_id)
    except:
        print('failed for',i['_id'])

### John's data
import bson
mycol2 = mydb["out_querystats"]
with open('/Users/scarlett/PycharmProjects/hackathon_2023/data/querystats/out.bson','rb') as f:
    data = bson.decode_all(f.read())
for i in data:
    try:
        x = mycol2.insert_one(i)
        # print list of the _id values of the inserted documents:
        # print(x.inserted_id)
    except:
        print('failed for', i['_id'])

# failed for 6511dc7ef7fb5266cffa193b
# failed for 6511dc7ef7fb5266cffa1b6a
