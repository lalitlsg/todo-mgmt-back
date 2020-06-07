from pymongo import MongoClient

# database configuration
client = MongoClient('0.0.0.0:27017')

# db name
db = client['todo']

#collections
tasks = db['tasks']


