import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

# Get MongoDB URL from .env
mongo_url = os.getenv("MONGO_URL")

# Get database name from .env
db_name = os.getenv("DB_NAME")

# Make connection to MongoDB
client = MongoClient(mongo_url)
db = client[db_name]

# Create collection name 'mongo_test'
collection = db["mongo_test"]

# CREATE: Insert one document
def insert_one_document():
    document = {"name": "Pratik Kadam", "is_active": True, "age": 24}
    collection.insert_one(document)
    print("Document Inserted")

# insert_one_document()

# CREATE: Insert many documents
def insert_many_documents():
    documents = [
        {"name": "Alice", "is_active": True, "age": 28},
        {"name": "Bob", "is_active": False, "age": 30},
        {"name": "Charlie", "is_active": True, "age": 22},
    ]
    collection.insert_many(documents)
    print("Multiple Documents Inserted", documents)

# insert_many_documents()

# READ: Find one document by query
def find_one_document():
    output = collection.find_one({"name": "Pratik Kadam"})
    print("One Document Found:", output)

# find_one_document()

# READ: Find all documents in the collection
def find_all_documents():
    documents = collection.find()
    for doc in documents:
        print("Document:", doc)

# find_all_documents()

# Projection: Selecting specific fields 
def projection_example():
    projection = {"name": 1, "age": 1, "_id": 0}  # "_id": 0 excludes the _id field
    result = collection.find_one({"name": "Pratik Kadam"}, projection)
    print("Projection Example Result:", result)

# projection_example()

# UPDATE: Update one document
def update_one_document():
    collection.update_one({"name": "Pratik Kadam"}, {"$set": {"age": 30}})
    print("Document Updated")

# update_one_document()

# UPDATE: Update many documents
def update_many_documents():
    collection.update_many({"is_active": True}, {"$set": {"is_active": False}})
    print("Multiple Documents Updated")

# update_many_documents()

# DELETE: Delete one document
def delete_one_document():
    collection.delete_one({"name": "Pratik Kadam"})
    print("Document Deleted")

# delete_one_document()

# DELETE: Delete many documents
def delete_many_documents():
    collection.delete_many({"is_active": False})
    print("Multiple Documents Deleted")

# delete_many_documents()

# FIND with $eq (Equal to)
def find_eq():
    result = collection.find({"age": {"$eq": 28}})
    for doc in result:
        print("Document matching $eq:", doc)

# find_eq()

# FIND with $ne (Not equal to)
def find_ne():
    result = collection.find({"age": {"$ne": 30}})
    for doc in result:
        print("Document matching $ne:", doc)

# find_ne()

# FIND with $gt (Greater than)
def find_gt():
    result = collection.find({"age": {"$gt": 25}})
    for doc in result:
        print("Document matching $gt:", doc)

# find_gt()

# FIND with $gte (Greater than or equal to)
def find_gte():
    result = collection.find({"age": {"$gte": 28}})
    for doc in result:
        print("Document matching $gte:", doc)

# find_gte()

# FIND with $lt (Less than)
def find_lt():
    result = collection.find({"age": {"$lt": 30}})
    for doc in result:
        print("Document matching $lt:", doc)

# find_lt()

# FIND with $lte (Less than or equal to)
def find_lte():
    result = collection.find({"age": {"$lte": 28}})
    for doc in result:
        print("Document matching $lte:", doc)

# find_lte()

# FIND with $in (Match within an array)
def find_in():
    result = collection.find({"age": {"$in": [22, 30]}})
    for doc in result:
        print("Document matching $in:", doc)

# find_in()

# FIND with $and (Both conditions must match)
def find_and():
    result = collection.find({"$and": [{"age": {"$gte": 25}}, {"is_active": True}]})
    for doc in result:
        print("Document matching $and:", doc)

# find_and()

# FIND with $or (Either condition can match)
def find_or():
    result = collection.find({"$or": [{"age": {"$gte": 25}}, {"is_active": False}]})
    for doc in result:
        print("Document matching $or:", doc)

# find_or()

# FIND with $nor (Neither condition must match)
def find_nor():
    result = collection.find({"$nor": [{"age": {"$lt": 25}}, {"is_active": False}]})
    for doc in result:
        print("Document matching $nor:", doc)

# find_nor()

# FIND with $not (Field value does not match the condition)
def find_not():
    result = collection.find({"age": {"$not": {"$gte": 28}}})
    for doc in result:
        print("Document matching $not:", doc)

# find_not()


# Aggregation Pipeline Example
def aggregation_example():
    pipeline = [
        {"$match": {"is_active": True}},  # Filter active users
        {"$group": {"_id": "$age", "count": {"$sum": 1}}},  # Group by age and count users
        {"$sort": {"count": -1}}  # Sort by count in descending order
    ]
    result = collection.aggregate(pipeline)
    for doc in result:
        print("Aggregation Result:", doc)

# aggregation_example()


# Indexing Example
def indexing_example():
    # Create an index on the 'name' field
    collection.create_index([("name", 1)])  # 1 for ascending order

    print("Index on 'name' field created.")

    #above line allow us to search faster because of indexing
    result = collection.find({"name": "Alice"})
    for doc in result:
        print("Found with index:", doc)

# indexing_example()


