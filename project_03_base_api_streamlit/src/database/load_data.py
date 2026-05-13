import pandas as pd
from pathlib import Path

from connection import get_connection


# Ruta raiz del proyecto 
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Ruta hacia al CSV del proyecto
CSV_PATH = BASE_DIR/"data"/"processed"/"accidentes_bogota_2023_dataset_limpio.csv"


def load_data():

    """ Carga los datos csv en la base de datos SQLite  
    
    
    """

    #Leer archivo csv
    df= pd.read_csv(CSV_PATH)

    #cambio de tipo de datos 
    df["Codigo_Accidente"] = df["Codigo_Accidente"].astype(str)
    df["Longitud"] = df["Longitud"].astype(float)
    df["Latitud"] = df["Latitud"].astype(float)
    df["Fecha_Acc"] = pd.to_datetime(df["Fecha_Acc"])

    #obtener la conexion SQLite
    connection = get_connection()

    # cargar los datos a SQLite
    df.to_sql(
        name="accidents",
        con=connection,
        if_exists="replace",
        index= False

    )

    # Cerrar conexion
    connection.close()

    print("Datos cargados correctamente en SQLite.")

if __name__ =="__main__":
    load_data()
