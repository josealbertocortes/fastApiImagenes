

import pymongo
# Replace the uri string with your MongoDB deployment's connection string.
conn_str = 'mongodb+srv://mern_user:S7tNE4ahVRZqr8Lu@cluster0.cl3ku.mongodb.net/'
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")