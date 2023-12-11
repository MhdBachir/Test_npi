from app import crud
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from  API import config


client = MongoClient(config.mongodb_url, server_api=ServerApi('1'))
    
def test_connection():
    """Test the connection to the database."""
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        assert False


def test_store_operation():
    #purge the database
    """Test the store_operation function."""
    # Store an operation in the database
    crud.store_operation('1 2 +', 3)
    
    # Retrieve the operation from the database
    operations = crud.retrieve_operations()
    
    # Check that the operation is in the database
    result_attend = {'expression': '1 2 +', 'result': 3}
    assert result_attend in [{'expression': op['expression'], 'result': op['result']} for op in operations]
    
    # Delete the operation from the database
    client['NPI']['Calculation'].delete_one({'expression': '1 2 +'})
    
    # Retrieve the operation from the database
    operations = crud.retrieve_operations()
    
    # Check that the operation is no longer in the database
    assert {'expression': '1 2 +', 'result': 3} not in operations 