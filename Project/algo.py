from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from API.config import mongodb_url



def estOperateur(c):
    """Vérifie si le caractère c est un opérateur."""
    operateurs = {'+', '-', '*', '/'}
    return c in operateurs

def calcul(op, n, m):
    """Effectue le calcul n op m."""
    if op == '+':
        print(n + m)
        return n + m
    elif op == '-':
        return n - m
    elif op == '*':
        return n * m
    elif op == '/':
        return n / m

def evaluation_recursif(elements):
    #elements = elements.split()
    """Évalue une expression en notation polonaise inversée (NPI) de manière récursive."""
    if not elements:
        raise ValueError("Expression invalide - liste d'éléments vide")
    #if element is str turn it into a list
    if isinstance(elements, str):
        elements = elements.split()
        
    element = elements.pop()

    if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
        return int(element)
    elif estOperateur(element):
        if len(elements) < 2:
            raise ValueError("Expression invalide - opérandes insuffisantes")
        m = evaluation_recursif(elements)
        n = evaluation_recursif(elements)
        return calcul(element, n, m)
    else:
        raise ValueError(f"Caractère invalide dans l'expression : {element}")




