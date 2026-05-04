-- =========================================
-- DIMENSIONES
-- =========================================

-- Dimensión: dim_product
-- Descripción:
-- Contiene la información descriptiva de los productos vendidos.
-- Cada registro representa un producto único identificado por su clave sustituta (product_key).
-- Incluye atributos de categorización como subcategoría y categoría, útiles para análisis jerárquico.
-- Fuente: datos originales del dataset (productos).
-- Uso: Permite analizar ventas por producto, subcategoría y categoría.

CREATE TABLE dim_product (
    product_key INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    sub_category VARCHAR(100),
    category VARCHAR(100)
);


-- Dimensión: dim_customer
-- Descripción:
-- Contiene la información de los clientes.
-- Cada registro representa un cliente único.
-- Incluye atributos como nombre y segmento de cliente.
-- Fuente: datos originales del dataset (clientes).
-- Uso: Permite segmentar el análisis de ventas por tipo de cliente.

CREATE TABLE dim_customer (
    customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    segment VARCHAR(100)
);


-- Dimensión: dim_date
-- Descripción:
-- Dimensión de tiempo generada en el proceso ETL.
-- Contiene un rango completo de fechas, independientemente de si existen o no en el dataset.
-- Incluye atributos derivados como año, mes, día y trimestre.
-- Fuente: generada artificialmente en Python (ETL).
-- Uso: Permite análisis temporal consistente (por año, mes, tendencias, etc.).

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    quarter INTEGER NOT NULL
);


-- Dimensión: dim_location
-- Descripción:
-- Contiene la información geográfica asociada a las ventas.
-- Cada registro representa una ubicación única.
-- Incluye atributos como ciudad, estado, país y código postal.
-- Fuente: datos originales del dataset (ubicación de pedidos).
-- Uso: Permite análisis geográfico de ventas.

CREATE TABLE dim_location (
    location_key INTEGER PRIMARY KEY AUTOINCREMENT,
    postal_code VARCHAR(20),
    country VARCHAR(100),
    region VARCHAR(100),
    "state" VARCHAR(100),
    city VARCHAR(100)
    
    
);


-- Dimensión: dim_ship_mode
-- Descripción:
-- Contiene los tipos de envío disponibles en las órdenes.
-- Cada registro representa un modo de envío único.
-- Fuente: datos originales del dataset (modo de envío).
-- Uso: Permite analizar el impacto del tipo de envío en las ventas.

CREATE TABLE dim_ship_mode (
    ship_mode_key INTEGER PRIMARY KEY AUTOINCREMENT,
    ship_mode VARCHAR(50)
);


-- =========================================
-- TABLA DE HECHOS
-- =========================================

-- Tabla: fact_sales
-- Descripción:
-- Tabla central del modelo estrella que contiene las métricas de ventas.
-- Cada registro representa una línea de pedido (venta de un producto específico dentro de una orden).
-- Incluye claves foráneas hacia las dimensiones para proporcionar contexto.
-- Métricas: ventas, cantidad, ganancia y descuento.
-- Fuente: datos transformados en el proceso ETL en Python.
-- Uso: Permite análisis multidimensional de las ventas.

CREATE TABLE fact_sales (
    order_key INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id VARCHAR(15) NOT NULL,

    product_key INTEGER,
    customer_key INTEGER,
    order_date_key INTEGER,
    ship_date_key INTEGER,
    location_key INTEGER,
    ship_mode_key INTEGER,

    sales REAL NOT NULL,
    quantity INTEGER NOT NULL,
    profit REAL NOT NULL,
    discount REAL NOT NULL,

    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (order_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (ship_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (location_key) REFERENCES dim_location(location_key),
    FOREIGN KEY (ship_mode_key) REFERENCES dim_ship_mode(ship_mode_key)
);