from pydantic import BaseModel

class Calculation(BaseModel):
    expression: str
    result: float
    
    
    
    
    