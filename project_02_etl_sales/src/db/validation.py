def validate_table_counts(conn):
    """Valida que las tablas tengan registros"""

    tables = [
        "dim_customer",
        "dim_product",
        "dim_location",
        "dim_ship_mode",
        "dim_date",
        "fact_sales"
    ]

    print("\n🔍 Validando conteo de registros...")

    cursor = conn.cursor()

    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]

        print(f"{table}: {count} registros")

        if count == 0:
            raise ValueError(f"La tabla {table} está vacía.")


def validate_foreign_keys(conn):
    """Valida integridad referencial en la tabla de hechos"""

    print("\n🔗 Validando integridad referencial...")

    cursor = conn.cursor()

    checks = checks = checks = [
        ("customer_key", "dim_customer", "customer_key"),
        ("product_key", "dim_product", "product_key"),
        ("location_key", "dim_location", "location_key"),
        ("ship_mode_key", "dim_ship_mode", "ship_mode_key"),
        ("order_date_key", "dim_date", "date_key"),
        ("ship_date_key", "dim_date", "date_key")
]

    for fk, dim, dim_pk in checks:
        query = f"""
         SELECT COUNT(*)
         FROM fact_sales f
         LEFT JOIN {dim} d
         ON f.{fk} = d.{dim_pk}
         WHERE d.{dim_pk} IS NULL
            """

        cursor.execute(query)
        missing = cursor.fetchone()[0]

        if missing > 0:
            raise ValueError(
                f"Integridad rota: {missing} registros en fact_sales sin correspondencia en {dim}"
            )

        print(f"{fk} OK")


def run_all_validations(conn):
    """Ejecuta todas las validaciones"""

    print("\n🧪 Ejecutando validaciones de calidad de datos...")

    validate_table_counts(conn)
    validate_foreign_keys(conn)

    print("\n✅ Todas las validaciones pasaron correctamente.")