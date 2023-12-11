# Import FastAPI classes and necessary modules
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List
from app.models import Calculation
from algo import evaluation_recursif
from app.crud import store_operation, retrieve_operations
import csv
from io import BytesIO, StringIO

# Create a FastAPI app instance
app = FastAPI(
    title="Your API Title",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json", 
    docs_url="/api/v1/docs",
)

# Define a POST endpoint for calculating expressions
@app.post("/calculate/", response_model=Calculation)
async def calculate(expression: str):
    try:
        # Split the expression into elements and evaluate
        elements = expression.split()
        result = evaluation_recursif(elements.copy())

        # Store the operation in the database
        store_operation(expression, result)

        # Return the result in the response
        return {"result": result}
    except ValueError as e:
        # Handle the case where an invalid expression is provided
        raise HTTPException(status_code=400, detail=str(e))

# Define a GET endpoint for retrieving all operations
@app.get("/operations/", response_model=List[Calculation])
async def get_operations():
    # Retrieve all stored operations from the database
    operations = retrieve_operations()
    
    # Print operations for debugging purposes
    print("op", operations)

    # Return operations in the response
    return JSONResponse(content=operations)

# Define a GET endpoint for downloading operations as a CSV file
@app.get("/download/")
async def download_operations():
    # Retrieve all stored operations from the database
    operations = retrieve_operations()

    # Create a string to store CSV data
    csv_data = StringIO()

    # Use the csv module to write data to the CSV string
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(["expression", "result"])  # Write CSV header

    # Write each operation to the CSV string
    for operation in operations:
        csv_writer.writerow([operation["expression"], operation["result"]])

    # Convert the CSV string to bytes
    csv_bytes = csv_data.getvalue().encode('utf-8')

    # Return the CSV file as a streaming response
    return StreamingResponse(BytesIO(csv_bytes), media_type="text/csv", headers={"Content-Disposition": "attachment;filename=operations.csv"})
