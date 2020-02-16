import pymongo
import datetime
from random import randint
import time

client = pymongo.MongoClient("mongodb+srv://Edmund:iamhere10@cluster0-nkp9x.mongodb.net/PowerBoi") # defaults to port 27017

db = client.PowerBoi.Usage

x = db.delete_many({})

    # print the number of documents in a collection
print(db.estimated_document_count())
print(x.deleted_count, " documents deleted.")
