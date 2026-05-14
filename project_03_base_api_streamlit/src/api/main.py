from fastapi import FastAPI,HTTPException
from src.services.accident_service import get_total_accidents,get_accidents_by_locality,get_total_fatal_accidents,filter_accidents_by_locality


app = FastAPI()

@app.get("/")
def home():
     return{"mesange":"API Funcionando"}

@app.get("/total-accidents")
def total_accidents():
     return get_total_accidents()

@app.get("/fatal-accidents")
def fatal_accidents():
     return get_total_fatal_accidents()

@app.get("/accidents-by-locality")
def accidents_by_locality():
     return get_accidents_by_locality()

@app.get("/locality/{localidad}")
def accidents_by_locality(localidad):
     result= filter_accidents_by_locality(localidad)

     if not result:
          raise HTTPException(
          status_code=404,
          detail="No se encontraron registros"
     )

     return result 