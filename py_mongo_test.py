import pymongo
import random
rand_index=random.random()
connection=pymongo.MongoClient()
proxy_db=connection.proxy_db
xici_tb=proxy_db.xici_tb
cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$lt':rand_index}}]})
if(cursor):
    pass
else:
    cursor=xici_tb.find_one({"$and":[{'speed':{"$lt":0.5}},{'time':{"$lt":0.5}},{'rand_value':{'$gt':rand_index}}]})    

