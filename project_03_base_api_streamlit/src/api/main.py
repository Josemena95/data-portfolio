from fastapi import FastAPI,HTTPException
from src.services.accident_service import(
     get_total_accidents,
     get_accidents_by_locality,
     get_total_fatal_accidents,
     filter_accidents_by_locality,
     get_accidents_by_severity,
     get_accidents_by_condition,
     get_accidents_by_accident_type,
     get_accidents_by_sex
               )



app = FastAPI()


# Health endpoint

@app.get("/health")
def health_endpoint():
     return{"status":"ok"}

# KPI endpoints

@app.get("/accidents/total")
def get_total_accidents_endpoint(localidad:str|None = None,
                                 condicion:str | None = None,
                                 sexo:str |None = None,
                                 horario:str | None = None):
     
     return get_total_accidents(localidad,
                                condicion,
                                sexo,
                                horario)

@app.get("/accidents/fatal")
def get_total_fatal_accidents_endpoint(localidad:str|None = None,
                                       condicion:str | None = None,
                                        sexo:str |None = None,
                                        horario:str | None = None):
     
     return get_total_fatal_accidents(localidad,
                                      condicion,
                                      sexo,
                                      horario)

# Agregation endpoints

@app.get("/accidents/by-locality")
def get_accidents_by_locality_endpoint(condicion:str | None = None, 
                                       sexo:str |None = None,
                                        horario:str | None = None):
     
     return get_accidents_by_locality(condicion,
                                      sexo,
                                      horario)

@app.get("/accidents/by-severity")
def get_accidents_by_severity_endpoint(
     localidad:str| None = None,
     condicion:str | None = None,
     sexo:str |None = None,
     horario:str | None = None
):
     return get_accidents_by_severity(
          localidad,
          condicion,
          sexo,
          horario
          )

@app.get("/accidents/by-condition")
def get_accidents_by_condition_endpoint(
     localidad:str| None = None,
     sexo:str |None = None,
     horario:str | None = None
):
     return get_accidents_by_condition(
          localidad,
          sexo,
          horario
          )

@app.get("/accidents/by-accident-type")
def get_accidents_by_accident_type_endpoint(
     localidad:str| None = None,
     condicion:str | None = None,
     sexo:str |None = None,
     horario:str | None = None
):
     return get_accidents_by_accident_type(
          localidad,
          condicion,
          sexo,
          horario
     )

@app.get("/accidents/by-sex")
def get_accidents_by_sex_endpoint(
     localidad:str| None = None,
     condicion:str | None = None,
     horario:str | None = None
):
     return get_accidents_by_sex(
          localidad,
          condicion,
          horario
          )

#Dinamic endpoint

@app.get("/accidents/locality/{localidad}")
def filter_accidents_by_locality_endpoint(localidad,
                                          condicion:str|None=None,
                                          sexo:str |None = None,
                                          horario:str | None = None):
     
     result= filter_accidents_by_locality(localidad,
                                          condicion,
                                          sexo,
                                          horario)

     if not result:
          raise HTTPException(
          status_code=404,
          detail=f"No se encontraron registros para la localidad{localidad}"
     )

     return result 