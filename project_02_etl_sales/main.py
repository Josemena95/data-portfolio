from src.etl.extract import extract_data
from src.etl.transform import transform_pipeline
from src.etl.config import FILE_PATH, DB_PATH, SCHEMA_PATH,PROCESSED_DATA_PATH
from src.db.load import (   
    create_connection,
    reset_database,
    execute_schema,
    load_all_tables
)
from src.db.validation import  run_all_validations
from src.db.export import export_all_tables


def main():
    print("🚀 Iniciando pipeline ETL...")

    # -------------------------
    # EXTRACT
    # -------------------------
    print("📥 Extrayendo datos...")
    df = extract_data(FILE_PATH)

    # -------------------------
    # TRANSFORM
    # -------------------------
    print("🔄 Transformando datos...")
    tables = transform_pipeline(df)

    # Validación rápida
    if not tables:
        raise ValueError("No se generaron tablas en la transformación.")

    for name, df_table in tables.items():
        print(f"{name}: {df_table.shape}")
        print(f"{name}: {df_table.info()}")

    # -------------------------
    # LOAD
    # -------------------------
    print("💾 Cargando datos en la base de datos...")

    reset_database(DB_PATH)
    conn = create_connection(DB_PATH)

    try:
        execute_schema(conn, SCHEMA_PATH)
        load_all_tables(conn, tables['dim_customer'],tables['dim_product'],tables['dim_location'],tables['dim_ship_mode'],tables['dim_date'] ,tables['fact_sales'])
        
        # VALIDACIONES 👇
        run_all_validations(conn)

        # Exportar a csv para Power BI

        export_all_tables(conn,PROCESSED_DATA_PATH)


    finally:
        conn.close()

    print("✅ Pipeline ejecutado correctamente. Base de datos generada.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error en el pipeline: {e}")


