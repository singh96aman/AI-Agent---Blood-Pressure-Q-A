from pymongo import MongoClient
from constants import Constants

class MongoDB:
    def __init__(self, host='localhost', port=27017, db_name='patient'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(Constants.MONGODB_URI)
            if self.db_name:
                self.db = self.client[self.db_name]
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    def get_doc(self, collection, doc_id):
        collection = self.client[self.db_name][collection]
        return collection.find_one({'_id': doc_id})
    
    def add_doc(self, collection, doc_id, doc):
        collection = self.client[self.db_name][collection]
        collection.update_one({'_id': doc_id}, {'$set': doc}, upsert=True)
    
    def get_distinct(self, collection, coll_name):
        collection = self.client[self.db_name][collection]
        return collection.distinct(coll_name)

    def get_all(self, collection):
        collection = self.client[self.db_name][collection]
        return collection.find({})
    
    def update_doc(self, collection, doc_id, key, val):
        collection = self.client[self.db_name][collection]
        collection.find_one_and_update({'_id':doc_id},
                        { '$set': {key : val} })

    def doc_exists(self, collection, doc_id) -> bool:
        collection = self.client[self.db_name][collection]
        doc = collection.find_one({'_id': doc_id}, projection={'_id': 1})
        return doc is not None
