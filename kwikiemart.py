import pymongo
mongo = pymongo.Connection('localhost')
mongo_db = mongo['kwik-e-mart']
mongo_coll = mongo_db['locations']
cursor = mongo_coll.find()
records = dict([record['_id'], record) for record in cursor)

db = conn.tutorial
db.test