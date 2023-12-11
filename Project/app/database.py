# app/database.py

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from API.config import mongodb_url

client = MongoClient(mongodb_url, server_api=ServerApi('1'))


# Function that store  operations and the result in the database
def store_operation(expression, result):
    """Stores the operation and result in the database."""
    # Create a new document to be inserted
    document = {
        'expression': expression,
        'result': result
    }
    # Insert the document into the database
    client['NPI']['Calculation'].insert_one(document)
    print("Successfully inserted a document into the database.")


# Function that retrieve the operations from the database
def retrieve_operations():
    """Retrieves the operations from the database."""
    # Retrieve the documents from the database
    documents = client['calculator']['operations'].find()
    # Print each document
    for document in documents:
        print(document)