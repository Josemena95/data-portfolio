import sqlite3
import pandas as pd
import os

def create_connection(db_path: str) -> sqlite3.Connection:
    """
    Crea una conexión a una base de datos SQLite.

    Si la base de datos no existe en la ruta especificada,
    SQLite la crea automáticamente.

    Argumentos:
        db_path (str): Ruta donde se encuentra o se creará la base de datos.

    Retorna:
        sqlite3.Connection: Objeto de conexión a la base de datos.

    Raises:
        Exception: Si ocurre un error al intentar conectar con la base de datos.
    """
    try:
        conn = sqlite3.connect(db_path)
        print("✅ Conexión exitosa")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        raise


def reset_database(db_path: str):
    """
    Elimina la base de datos si existe en la ruta especificada.

    Esta función se utiliza para implementar una estrategia de carga
    tipo 'full reload', asegurando que la base de datos se recree
    desde cero en cada ejecución del pipeline.

    Argumentos:
        db_path (str): Ruta de la base de datos a eliminar.
    """
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️ Base de datos eliminada")
    else:
        print(f"ℹ️ No existe base de datos en: {db_path}")



def execute_schema(conn: sqlite3.Connection, schema_path: str):
    """
    Ejecuta un script SQL para crear la estructura de la base de datos.

    Lee el archivo .sql que contiene las instrucciones de creación
    de tablas (dimensiones y tabla de hechos) y las ejecuta en la
    base de datos SQLite.

    Argumentos:
        conn (sqlite3.Connection): Conexión activa a la base de datos.
        schema_path (str): Ruta al archivo .sql que contiene el schema.

    Raises:
        FileNotFoundError: Si el archivo schema.sql no existe en la ruta indicada.
        Exception: Si ocurre un error durante la ejecución del script SQL.
    """
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"No se encontró el archivo: {schema_path}")

    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()

        print("📦 Schema creado correctamente")

    except Exception as e:
        print(f"❌ Error al ejecutar el schema: {e}")
        raise



def load_table(df: pd.DataFrame, table_name: str, conn: sqlite3.Connection):
    """
    Carga un DataFrame en una tabla existente de la base de datos.

    Inserta los datos del DataFrame en la tabla especificada
    utilizando la conexión activa a SQLite.

    Argumentos:
        df (pd.DataFrame): DataFrame con los datos a cargar.
        table_name (str): Nombre de la tabla destino en la base de datos.
        conn (sqlite3.Connection): Conexión activa a la base de datos.

    Raises:
        ValueError: Si el DataFrame está vacío.
        Exception: Si ocurre un error durante la carga de datos.
    """

    # Validación: DataFrame vacío
    if df.empty:
        raise ValueError(f"El DataFrame para la tabla '{table_name}' está vacío")

    try:
        print(f"⏳ Cargando datos en la tabla '{table_name}'...")
        print(f"📊 Filas a insertar: {len(df)}")

        df.to_sql(
            name=table_name,
            con=conn,
            if_exists="append",
            index=False
        )

        print(f"✅ Tabla '{table_name}' cargada correctamente ({len(df)} filas)")

    except Exception as e:
        print(f"❌ Error al cargar la tabla '{table_name}': {e}")
        raise


def load_all_tables(
    conn: sqlite3.Connection,
    dim_customer: pd.DataFrame,
    dim_product: pd.DataFrame,
    dim_location: pd.DataFrame,
    dim_ship_mode: pd.DataFrame,
    dim_date: pd.DataFrame,
    fact_sales: pd.DataFrame
):
    """
    Carga todas las tablas del modelo estrella en la base de datos.

    Primero carga las tablas de dimensiones y posteriormente la tabla
    de hechos, garantizando la integridad referencial.

    Argumentos:
        conn (sqlite3.Connection): Conexión activa a la base de datos.
        dim_customer (pd.DataFrame): Dimensión de clientes.
        dim_product (pd.DataFrame): Dimensión de productos.
        dim_location (pd.DataFrame): Dimensión de ubicación.
        dim_ship_mode (pd.DataFrame): Dimensión de modo de envío.
        dim_date (pd.DataFrame): Dimensión de fechas.
        fact_sales (pd.DataFrame): Tabla de hechos de ventas.
    """

    try:
        print("🚀 Iniciando carga de tablas...")

        # 🔹 Dimensiones
        tables = {
            "dim_customer": dim_customer,
            "dim_product": dim_product,
            "dim_location": dim_location,
            "dim_ship_mode": dim_ship_mode,
            "dim_date": dim_date
        }

        for table_name, df in tables.items():
            load_table(df, table_name, conn)

        # 🔹 Tabla de hechos (SIEMPRE AL FINAL)
        load_table(fact_sales, "fact_sales", conn)

        print("✅ Todas las tablas cargadas correctamente")

    except Exception as e:
        print(f"❌ Error en la carga de tablas: {e}")
        raise