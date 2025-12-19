# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        #
        # You must edit the password below for your environment. 
        #
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        #
        # Initialize Connection 
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return True if result.acknowledged else False
            except Exception as e:
                print(f"Error inserting document: {e}")
        else:
            return False
    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                cursor = self.collection.find(query)   # returns a cursor
                return list(cursor)                    # convert cursor to list
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            return []
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(
                    query, {"$set": new_values}
                )
                return result.modified_count  # number of docs updated
            except Exception as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            return 0
            
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count  # number of docs deleted
            except Exception as e:
                print(f"Error deleting documents: {e}")
                return 0
        else:
            return 0