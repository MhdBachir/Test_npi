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
    """Store a calculation operation in the database."""
    document = {
        'expression': expression,
        'result': result
    }
    # Insert the document into the 'Calculation' collection in the 'NPI' database
    client['NPI']['Calculation'].insert_one(document)

def retrieve_operations():
    """Retrieve all stored operations from the database."""
    # Query all documents in the 'Calculation' collection in the 'NPI' database
    documents = client['NPI']['Calculation'].find()

    # Convert ObjectId to string for each document
    # This is done to make the '_id' field more user-friendly
    operations = [
        {
            'expression': doc['expression'],
            'result': doc['result'],
            '_id': str(doc['_id'])  # Convert ObjectId to string
        }
        for doc in documents
    ]

    return operations
