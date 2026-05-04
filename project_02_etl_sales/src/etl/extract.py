import pandas as pd

def extract_data(path: str, encoding: str = "latin-1") -> pd.DataFrame:
    """
    Lee un archivo CSV desde la ruta especificada y lo carga en un DataFrame de pandas.

    Args:
        path (str): Ruta del archivo CSV.
        encoding (str, optional): Codificación del archivo. Por defecto 'latin-1'.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.

    Raises:
        Exception: Si ocurre un error durante la lectura del archivo.
    """
    try:
        df = pd.read_csv(path, encoding=encoding)
        return df

    except Exception as e:
        raise Exception(f"Error al cargar el archivo: {e}")
    



def validate_raw_data(df: pd.DataFrame) -> None:
    """
    Valida la estructura básica del DataFrame extraído desde el archivo fuente.

    Verifica que:
    - El DataFrame no esté vacío
    - Contenga todas las columnas esperadas

    Args:
        df (pd.DataFrame): DataFrame a validar

    Raises:
        ValueError: Si el DataFrame está vacío, faltan columnas o tiene columnas no esperadas
    """

    if df.empty:
        raise ValueError("El DataFrame está vacío")

    expected_columns = [
        'Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
        'Customer ID', 'Customer Name', 'Segment', 'Country', 'City',
        'State', 'Postal Code', 'Region', 'Product ID', 'Category',
        'Sub-Category', 'Product Name', 'Sales', 'Quantity',
        'Discount', 'Profit'
    ]

    missing_columns = set(expected_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas: {missing_columns}")

    # Validación columnas no esperadas
    extra_columns = set(df.columns) - set(expected_columns)

    if extra_columns:
        print(f"Advertencia: columnas no esperadas: {extra_columns}")
 

 