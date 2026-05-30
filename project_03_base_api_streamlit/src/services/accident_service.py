import pandas as pd
from src.database.connection import get_connection

def load_accidents_data():
    """
    Carga la tabla de SQLite y crea un DataFrame.

    """

    connection = get_connection()
    query = "SELECT * FROM accidents"
    df = pd.read_sql_query(query,connection)
    connection.close()
    return df

def apply_filters(df, filters: dict | None = None):
    """
    Aplica filtros dinámicos sobre el DataFrame.
    """

    if not filters:

        return df

    valid_columns = set(df.columns)

    for column, value in filters.items():

        if value is None:

            continue

        if column not in valid_columns:

            continue

        df = df[df[column] == value]

    return df


def get_total_accidents(localidad:str |None = None,
                         condicion:str | None = None,
                         sexo:str | None = None,
                         horario:str | None = None):
    """
    Devuelve el total de accidentes.
    """
    df=load_accidents_data()
    
    filters = {}

    if localidad:
        filters['Localidad'] = localidad
    if condicion:
        filters['Condicion'] = condicion
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)
    
    total_accidents = df["Codigo_Accidente"].nunique()

    return {

        "total_accidents":total_accidents
    }

def get_total_fatal_accidents(localidad:str | None = None,
                              condicion:str | None = None,
                              sexo:str | None = None,
                            horario:str | None = None):
    """
    Calcula la cantidad de accidentes con muertes

    """

    df = load_accidents_data()

    filters = {}

    if localidad:
        filters['Localidad'] = localidad
    if condicion:    
        filters['Condicion'] = condicion
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)

    total_fatal_accidentes = df[df["Gravedad_Indicador_Tradicional_y"]=="MUERTO"]["Codigo_Accidente"].nunique()

    return {

        "total_fatal_accidents":total_fatal_accidentes
    }

def get_accidents_by_locality(condicion:str | None = None,
                              sexo:str | None = None,
                            horario:str | None = None):

    """
    Calcula la cantidad de accidentes por localidad.
    """

    df = load_accidents_data()

    filters = {}
    if condicion :
        filters["Condicion"] = condicion
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df=apply_filters(df,filters)


    total_accidents= df.groupby("Localidad").agg({
                                "Codigo_Accidente":"nunique"}).rename(columns={
                                "Codigo_Accidente":"total_accidentes"}).reset_index().sort_values( 
                                by="total_accidentes",ascending=False)

    return total_accidents.to_dict(orient="records")


def filter_accidents_by_locality(localidad: str, 
                                 condicion:str | None = None,
                                 sexo:str | None = None,
                                horario:str | None = None) -> list[dict]:
    """
    Filtra registros por localidad.
    """

    localidad = localidad.upper()

    df = load_accidents_data()

    filters={}
    if condicion:
        filters["Condicion"] = condicion
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)

    df_locality = (
        df[df["Localidad"] == localidad]
        
    )

    if df_locality.empty:

       return []

    return df_locality.to_dict(orient="records")

def get_accidents_by_severity(localidad:str | None = None,
                              condicion:str | None = None,
                              sexo:str | None = None,
                            horario:str | None = None):
    """
    Calcula la cantidad de personas involucradas por nivel de gravedad
    utilizando la granularidad del dataset (1 fila = 1 persona)
    """

    df = load_accidents_data()

    filters = {}
    if localidad:
        filters["Localidad"] = localidad
    if condicion:
        filters["Condicion"] = condicion
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)

    severity_data = (
        df
        .groupby("Gravedad_Indicador_Tradicional_y")
        .size().reset_index(name = "cantidad")
        .rename(
            columns={"Gravedad_Indicador_Tradicional_y": "gravedad"
        }
        )
        .sort_values("cantidad", ascending=False)
    )

    return severity_data.to_dict(orient="records")

def get_accidents_by_condition(localidad:str|None = None,
                               sexo:str | None = None,
                            horario:str | None = None):
    """
    Calcula la cantidad de personas involucradas agrupadas por condición.
    """

    df = load_accidents_data()

    filters ={}
    if localidad:
        filters["Localidad"] = localidad
    if sexo:
        filters['Sexo'] = sexo
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df, filters)

    condition_data = (
        df
        .groupby("Condicion")
        .size()
        .reset_index(name="cantidad")
        .rename(
            columns={
                "Condicion": "condicion"
            }
        )
        .sort_values("cantidad", ascending=False)
    )

    return condition_data.to_dict(orient="records")

def get_accidents_by_accident_type(
        localidad:str | None = None,
        condicion:str | None = None,
        sexo:str | None = None,
        horario:str | None = None
):
    """
    Calcula la cantidad de personas involucradas agrupadas
    por tipo de accidente.
    """

    df = load_accidents_data()
    
    filters = {}

    if localidad:
        filters["Localidad"] = localidad
    
    if condicion:
        filters["Condicion"] = condicion
    
    if sexo:
        filters['Sexo'] = sexo

    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)

    accident_type_data = (
        df
        .groupby("Clase_Acc")
        .size()
        .reset_index(name="cantidad")
        .rename(
            columns={
                "Clase_Acc": "tipo_accidente"
            }
        )
        .sort_values("cantidad", ascending=False)
    )

    return accident_type_data.to_dict(orient="records")

def get_accidents_by_sex(localidad:str |None = None,
                         condicion:str | None = None,
                         horario:str | None = None):
    """
    Calcula la cantidad de personas involucradas agrupadas por sexo.
    """

    df = load_accidents_data()

    filters = {}

    if localidad:
        filters["Localidad"]=localidad
    if condicion:
        filters["Condicion"]=condicion
    if horario:
        filters['clasificacion_Horario'] = horario

    df = apply_filters(df,filters)

    sex_data = (
        df
        .groupby("Sexo")
        .size()
        .reset_index(name="cantidad")
        .rename(
            columns={
                "Sexo": "sexo"
            }
        )
        .sort_values("cantidad", ascending=False)
    )

    return sex_data.to_dict(orient="records")




if __name__ == "__main__":

    result1 = get_total_accidents()
    result2 = get_total_fatal_accidents()
    result3 = get_accidents_by_locality()
    result4 = filter_accidents_by_locality("X")
    result5 = get_accidents_by_severity()
    result6 = get_accidents_by_condition()
    result7 = get_accidents_by_accident_type()
    result8 = get_accidents_by_sex()
    result9 = apply_filters(load_accidents_data(),{"Localidad":"KENNEDY"})
    print(f' el resultado es {result1,result2}')
    print(f'accidentes por localidad {result3}')
    print(f'filtro por localidad {result4}')
    print(f'accidentes por severidad{result5}')
    print(f'accidente por condicion{result6}')
    print(f'tipo de accidente{result7}')
    print(f'accidentes por sexo{result8}')
    print(f'dataframe{result9}')
