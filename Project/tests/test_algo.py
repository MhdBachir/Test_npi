from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from API.config import mongodb_url
from algo import estOperateur, calcul, evaluation_recursif



# redige tous les tests unitaires

def test_estOperateur():
    """Test the estOperateur function."""
    assert estOperateur('+') == True
    assert estOperateur('-') == True
    assert estOperateur('*') == True
    assert estOperateur('/') == True
    assert estOperateur('2') == False
    assert estOperateur('a') == False
    
def test_calcul():
    """Test the calcul function."""
    assert calcul('+', 1, 2) == 3
    assert calcul('-', 1, 2) == -1
    assert calcul('*', 1, 2) == 2
    assert calcul('/', 1, 2) == 0.5
    
    
def test_evaluation_recursif():
    """Test the evaluation_recursif function."""
    assert evaluation_recursif('1 2 +') == 3
    assert evaluation_recursif('1 2 -') == -1
    assert evaluation_recursif('1 2 *') == 2
    assert evaluation_recursif('1 2 /') == 0.5
    assert evaluation_recursif('1 2 + 3 *') == 9
    
    

        
    
    
    
            



        



