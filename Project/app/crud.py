# app/crud.py

from app.models import Calculation
from app.database import client


def connection():
    """Test the connection to the database."""
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        
    

def store_operation(expression: str, result: float):
    document = {
        'expression': expression,
        'result': result
    }
    client['NPI']['Calculation'].insert_one(document)

def retrieve_operations():
    documents = client['NPI']['Calculation'].find()

    # Convert ObjectId to string for each document
    operations = [
        {
            'expression': doc['expression'],
            'result': doc['result'],
            '_id': str(doc['_id'])  # Convert ObjectId to string
        }
        for doc in documents
    ]

    return operations
