from fastapi import FastAPI,HTTPException
from src.services.accident_service import(
     get_total_accidents,
     get_accidents_by_locality,
     get_total_fatal_accidents,
     filter_accidents_by_locality
     )


app = FastAPI()


# Health endpoint
@app.get("/")
def home():
     return{"mesange":"API Funcionando"}

# KPI endpoints

@app.get("/accidents/total")
def get_total_accidents_endpoint():
     return get_total_accidents()

@app.get("/accidents/fatal")
def get_total_fatal_accidents_endpoint():
     return get_total_fatal_accidents()

# Agregation endpoints
@app.get("/accidents/by-locality")
def get_accidents_by_locality_endpoint():
     return get_accidents_by_locality()

#Dinamic endpoint
@app.get("/accidents/locality/{localidad}")
def filter_accidents_by_locality_endpoint(localidad):
     result= filter_accidents_by_locality(localidad)

     if not result:
          raise HTTPException(
          status_code=404,
          detail=f"No se encontraron registros para la localidad{localidad}"
     )

     return result 