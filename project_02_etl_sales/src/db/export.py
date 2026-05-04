import pandas as pd
import os


def export_table_to_csv(conn, table_name, output_dir):
    """
    Exporta una tabla de SQLite a CSV.

    Args:
        conn: conexión SQLite
        table_name (str): nombre de la tabla
        output_dir (str): directorio destino
    """
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)

        file_path = os.path.join(output_dir, f"{table_name}.csv")
        df.to_csv(file_path, index=False, encoding="utf-8")

        print(f"[EXPORT] Tabla '{table_name}' exportada a {file_path}")

    except Exception as e:
        print(f"[ERROR] Error exportando {table_name}: {e}")
        raise


def export_all_tables(conn, output_dir):
    """
    Exporta todas las tablas del modelo estrella a CSV.
    """
    tables = [
        "fact_sales",
        "dim_product",
        "dim_customer",
        "dim_location",
        "dim_ship_mode",
        "dim_date"
    ]

    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)

    for table in tables:
        export_table_to_csv(conn, table, output_dir)