import pandas as pd
from src.etl.config import *

df = pd.read_csv(FILE_PATH, encoding='latin-1')


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza limpieza básica del DataFrame:
    - Elimina columnas innecesarias
    - Convierte columnas de fecha a datetime
    - Ajusta tipos de datos
    - Limpia strings (espacios en blanco)

    Args:
        df (pd.DataFrame): DataFrame proveniente de extract_data

    Returns:
        pd.DataFrame: DataFrame limpio
    """

    def standardize_columm_names(df: pd.DataFrame)-> pd.DataFrame:
        """
        estandariza los encabezados o nombres de cada columna en formato mmm_mmm
        
        argumento
        df:dataframe
        
        return
        df: df con titulos de campos normalizados

        """
        df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        )

    # 1. Eliminar columnas innecesarias
    df = df.drop(columns=["Row ID"])

    # 2. Normalizacion de titulos de campos
    standardize_columm_names(df)

    # 3. Convertir fechas a datetime
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    # 4. Convertir postal_code a string
    df["postal_code"] = df["postal_code"].astype(str)

    # 5. Limpieza básica de strings


    for col in df.select_dtypes(include="object").columns:
        if col in ['order_id','customer_id','postal_code','product_id']:
            continue
        else:
            df[col] = df[col].str.strip()
            df[col]= df[col].str.title()

    return df


def create_dim_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la dimensión de productos (dim_product) a partir del DataFrame limpio.

    Incluye:
    - Clave surrogate (product_key)
    - Clave natural (product_id)
    - Atributos del producto

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data

    Returns:
        pd.DataFrame: Dimensión de productos sin duplicados
    """

    # 1. Seleccionar columnas relevantes
    cols = ["product_id", "category", "sub_category", "product_name"]
    df_product = df[cols].drop_duplicates().reset_index(drop=True)

    # 2. Crear surrogate key
    df_product["product_key"] = (df_product.index + 1).astype(str)

    # 3. Ordenar columnas (SK primero)
    df_product = df_product[
        ["product_key", "product_id", "product_name", "sub_category", "category"]
    ]

    return df_product


def create_dim_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la dimensión de clientes (dim_customer) a partir del DataFrame limpio.

    Incluye:
    - Clave surrogate (customer_key)
    - Clave natural (customer_id)
    - Atributos del cliente

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data

    Returns:
        pd.DataFrame: Dimensión de clientes sin duplicados
    """

    # 1. Seleccionar columnas relevantes
    cols = ["customer_id", "customer_name", "segment"]
    df_customer = df[cols].drop_duplicates().reset_index(drop=True)

     # Estandarización 
    df_customer["customer_name"] = df_customer["customer_name"].str.title()
    df_customer["segment"] = df_customer["segment"].str.title()

    # 2. Crear surrogate key
    df_customer["customer_key"] = (df_customer.index + 1).astype(str)

    # 3. Ordenar columnas (SK primero)
    df_customer = df_customer[
        ["customer_key", "customer_id", "customer_name", "segment"]]

    return df_customer

import pandas as pd

def create_dim_location(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la dimensión de ubicaciones (dim_location) a partir del DataFrame limpio.

    Incluye:
    - Clave surrogate (location_key)
    - Atributos geográficos

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data

    Returns:
        pd.DataFrame: Dimensión de ubicaciones sin duplicados
    """

    # 1. Seleccionar columnas relevantes
    cols = ["country", "state", "city", "postal_code", "region"]
    df_location = df[cols].drop_duplicates().reset_index(drop=True)

    # 2. Estandarización
    for col in ["country", "state", "city", "region"]:
        df_location[col] = df_location[col].str.title()

    df_location["postal_code"] = df_location["postal_code"].astype(str).str.strip()

    # 3. Crear surrogate key
    df_location["location_key"] = (df_location.index + 1).astype(str)

    # 4. Ordenar columnas (SK primero)
    df_location = df_location[
        ["location_key","postal_code", "country", "region", "state", "city"]
    ]

    return df_location



def create_dim_ship_mode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la dimensión de modos de envío (dim_ship_mode) a partir del DataFrame limpio.

    Incluye:
    - Clave surrogate (ship_mode_key)
    - Atributo de modo de envío

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data

    Returns:
        pd.DataFrame: Dimensión de modos de envío sin duplicados
    """

    # 1. Seleccionar columna relevante
    cols = ["ship_mode"]
    df_ship_mode = df[cols].drop_duplicates().reset_index(drop=True)

    # 2. Estandarización 
    df_ship_mode["ship_mode"] = df_ship_mode["ship_mode"].str.title()

    # 3. Crear surrogate key
    df_ship_mode["ship_mode_key"] = (df_ship_mode.index + 1).astype(str)

    # 4. Ordenar columnas
    df_ship_mode = df_ship_mode[["ship_mode_key", "ship_mode"]]

    return df_ship_mode



def create_dim_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la dimensión de fechas (dim_date) a partir del DataFrame limpio.

    Incluye:
    - Clave surrogate (date_key) en formato YYYYMMDD
    - Atributos de fecha (año, mes, día)

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data

    Returns:
        pd.DataFrame: Dimensión de fechas completa
    """

    # 1. Obtener rango de fechas
    fecha_min = min(df["order_date"].min(), df["ship_date"].min())
    fecha_max = max(df["order_date"].max(), df["ship_date"].max())

    # 2. Crear rango continuo de fechas
    date_range = pd.date_range(start=fecha_min, end=fecha_max)

    # 3. Crear DataFrame
    df_date = pd.DataFrame({
        "full_date": date_range
    })

    # 4. Crear atributos
    df_date["year"] = df_date["full_date"].dt.year
    df_date["month"] = df_date["full_date"].dt.month
    df_date["day"] = df_date["full_date"].dt.day
    df_date["quarter"] = df_date["full_date"].dt.quarter
    # 5. Crear date_key (YYYYMMDD)
    df_date["date_key"] = df_date["full_date"].dt.strftime("%Y%m%d").astype(str)

    # 6. Ordenar columnas
    df_date = df_date[
        ["date_key", "full_date", "year", "month", "day","quarter"]
    ]

    return df_date




def create_fact_table(
    df: pd.DataFrame,
    dim_customer: pd.DataFrame,
    dim_product: pd.DataFrame,
    dim_location: pd.DataFrame,
    dim_ship_mode: pd.DataFrame,
    dim_date: pd.DataFrame
) -> pd.DataFrame:
    """
    Construye la tabla de hechos (fact_sales) a partir del DataFrame limpio
    y las dimensiones previamente generadas.

    El proceso incluye:
    - Integración con dimensiones mediante operaciones de merge
    - Asignación de claves foráneas (surrogate keys)
    - Reemplazo de claves naturales por claves surrogate
    - Eliminación de columnas descriptivas
    - Conservación de métricas de negocio

    Granularidad:
    - Nivel de línea de pedido (order line)

    Args:
        df (pd.DataFrame): DataFrame limpio proveniente de clean_data
        dim_customer (pd.DataFrame): Dimensión de clientes
        dim_product (pd.DataFrame): Dimensión de productos
        dim_location (pd.DataFrame): Dimensión de ubicaciones
        dim_ship_mode (pd.DataFrame): Dimensión de modos de envío
        dim_date (pd.DataFrame): Dimensión de fechas

    Returns:
        pd.DataFrame: Tabla de hechos lista para carga en SQL
    """

    # 🔹 Copia del dataframe base
    df_fact = df.copy()

    # . Crear surrogate key
    df_fact["order_key"] = (df_fact.index + 1).astype(str)

    # 🔹 Merge con dimensión Customer
    df_fact = df_fact.merge(
        dim_customer[['customer_id', 'customer_key']],
        on='customer_id',
        how='left'
    )

    # 🔹 Merge con dimensión Product
    df_fact = df_fact.merge(
        dim_product[['product_id', 'product_key', 'product_name']],
        on=['product_id','product_name'],
        how='left'
    )

    # 🔹 Merge con dimensión ship_mode
    df_fact = df_fact.merge(
        dim_ship_mode[['ship_mode', 'ship_mode_key']],
        on='ship_mode',
        how='left'
    )

    # 🔹 Merge con dimensión Location
    df_fact = df_fact.merge(
        dim_location[['country', 'state', 'city', 'postal_code', 'region', 'location_key']],
        on=['country', 'state', 'city', 'postal_code', 'region'],
        how='left'
    )

    # 🔹 Merge con dimensión Date (order_date)
    df_fact = df_fact.merge(
        dim_date[['date_key', 'full_date']],
        left_on='order_date',
        right_on='full_date',
        how='left'
    ).rename(columns={'date_key': 'order_date_key'})

    df_fact = df_fact.drop(columns=['full_date'])

    # 🔹 Merge con dimensión Date (ship_date)
    df_fact = df_fact.merge(
        dim_date[['date_key', 'full_date']],
        left_on='ship_date',
        right_on='full_date',
        how='left'
    ).rename(columns={'date_key': 'ship_date_key'})

    df_fact = df_fact.drop(columns=['full_date'])



    # 🔹 Selección final de columnas
    df_fact = df_fact[
       #toca corregir las key y toca ver si creamos una key surrogada para la tabla fact
        [ 'order_key',
            'order_id',
            'product_key',
            'customer_key',
            'order_date_key',
            'ship_date_key',
            'location_key',
            'ship_mode_key',
            'sales',
            'quantity',
            'profit',
            'discount'  
            ]
        ]

    # 🔥 Validación crítica: no deben existir claves nulas
    key_columns = [
        'order_key',
        'order_id',
        'order_date_key',
        'ship_date_key',
        'customer_key',
        'product_key',
        'ship_mode_key',
        'location_key'
    ]

    if df_fact[key_columns].isnull().any().any():
        raise ValueError("Hay claves nulas en la tabla de hechos")

    return df_fact

import pandas as pd


def transform_pipeline(df: pd.DataFrame) -> dict:
    """
    Ejecuta el proceso completo de transformación de datos:
    - Limpieza de datos
    - Construcción de dimensiones
    - Construcción de la tabla de hechos

    Args:
        df (pd.DataFrame): DataFrame resultante de la fase de extracción.

    Returns:
        dict: Diccionario con las tablas del modelo estrella:
            - dim_customer
            - dim_product
            - dim_location
            - dim_ship_mode
            - dim_date
            - fact_sales
    """

    # -------------------------
    # 1. Limpieza
    # -------------------------
    df_clean = clean_data(df)

    if df_clean.empty:
        raise ValueError("El DataFrame después de la limpieza está vacío.")

    # -------------------------
    # 2. Dimensiones
    # -------------------------
    dim_customer = create_dim_customer(df_clean)
    dim_product = create_dim_product(df_clean)
    dim_location = create_dim_location(df_clean)
    dim_ship_mode = create_dim_ship_mode(df_clean)
    dim_date = create_dim_date(df_clean)

    # -------------------------
    # 3. Tabla de hechos
    # -------------------------
    fact_sales = create_fact_table(
        df_clean,
        dim_customer,
        dim_product,
        dim_location,
        dim_ship_mode,
        dim_date
    )

    # -------------------------
    # 4. Validaciones básicas
    # -------------------------
    tables = {
        "dim_customer": dim_customer,
        "dim_product": dim_product,
        "dim_location": dim_location,
        "dim_ship_mode": dim_ship_mode,
        "dim_date": dim_date,
        "fact_sales": fact_sales
    }

    for name, df_table in tables.items():
        if df_table.empty:
            raise ValueError(f"La tabla {name} está vacía.")

    # -------------------------
    # 5. Output estructurado
    # -------------------------
    return tables