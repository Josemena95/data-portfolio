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

def get_total_accidents():
    """
    Devuelve el total de accidentes.
    """
    df=load_accidents_data()
    
    total_accidents = df["Codigo_Accidente"].nunique()

    return {

        "total_accidents":total_accidents
    }

def get_total_fatal_accidents():
    """
    Calcula la cantidad de accidentes con muertes

    """

    df = load_accidents_data()

    total_fatal_accidentes = df[df["Gravedad_Indicador_Tradicional_y"]=="MUERTO"]["Codigo_Accidente"].nunique()

    return {

        "total_fatal_accidents":total_fatal_accidentes
    }

def get_accidents_by_locality():

    """
    Calcula la cantidad de accidentes por localidad.
    """

    df = load_accidents_data()

    total_accidents= df.groupby("Localidad").agg({
                                "Codigo_Accidente":"nunique"}).rename(columns={
                                "Codigo_Accidente":"total_accidentes"}).reset_index().sort_values( 
                                by="total_accidentes",ascending=False)

    return total_accidents.to_dict(orient="records")


def filter_accidents_by_locality(localidad: str) -> list[dict]:
    """
    Filtra registros por localidad.
    """

    localidad = localidad.upper()

    df = load_accidents_data()

    df_locality = (
        df[df["Localidad"] == localidad]
        .head(10)
    )

    if df_locality.empty:

       return []

    return df_locality.to_dict(orient="records")

if __name__ == "__main__":

    result1 = get_total_accidents()
    result2 = get_total_fatal_accidents()
    result3 = get_accidents_by_locality()
    result4 = filter_accidents_by_locality("X")
    print(f' el resultado es {result1,result2}')
    print(f'accidentes por localidad {result3}')
    print(f'filtro por localidad {result4}')

