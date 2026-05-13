import sqlite3
from pathlib import Path

# Ruta raiz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Ruta hacia la base de datos accidents.db
DB_PATH = BASE_DIR/"data"/"accidents.db"


def get_connection():
    """
    Crea y devuelve una conexion SQLite."
    
    """

    connection = sqlite3.connect(DB_PATH)

    return connection

if __name__ =="__main__":

    connection = get_connection()

    print("Conexión SQLite exitosa.")

    connection.close()

    