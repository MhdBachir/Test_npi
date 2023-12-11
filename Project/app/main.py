# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List
from app.models import Calculation
from algo import evaluation_recursif
from app.crud import store_operation, retrieve_operations
import csv
from io import BytesIO , StringIO


app = FastAPI(
    title="Your API Title",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json", 
    docs_url="/api/v1/docs",  
)



@app.post("/calculate/", response_model=Calculation)
async def calculate(expression: str):
    try:
        elements = expression.split()
        result = evaluation_recursif(elements.copy())
        store_operation(expression, result)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/operations/", response_model=List[Calculation])
async def get_operations():
    operations = retrieve_operations()
    print("op",operations)
    return JSONResponse(content=operations)

#create a function to retrieve the operations from the database and download them as a csv file
@app.get("/download/")
async def download_operations():
    operations = retrieve_operations()

    # Créer une chaîne pour stocker les données CSV
    csv_data = StringIO()
    
    # Utiliser le module csv pour écrire les données dans la chaîne CSV
    csv_writer = csv.writer(csv_data)
    
    # Écrire l'en-tête du CSV
    csv_writer.writerow(["expression", "result"])
    
    # Écrire chaque opération dans le CSV
    for operation in operations:
        csv_writer.writerow([operation["expression"], operation["result"]])

    # Convertir la chaîne CSV en bytes
    csv_bytes = csv_data.getvalue().encode('utf-8')

    # Renvoyer le fichier CSV comme une réponse de streaming
    return StreamingResponse(BytesIO(csv_bytes), media_type="text/csv", headers={"Content-Disposition": "attachment;filename=operations.csv"})
