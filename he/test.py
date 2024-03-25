from hehe import *
import pymongo

client = pymongo.MongoClient('mongodb+srv://dristiroy:gpH8AhvZ8NwnJDHo@dristicluster.86w9fpu.mongodb.net/')
print(client.list_database_names())
db = client['users']
dcOne = db['public']
dbTwo = db['private']


print(db.list_collection_names())
psy  = dcOne.find({'first-name':'Dristi'})
print(psy.next())