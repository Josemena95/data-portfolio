# 📊 Proyecto: Pipeline ETL + Modelo Estrella + Dashboard en Power BI

## 🚀 Descripción

Este proyecto implementa un flujo completo de analítica de datos, desde la ingestión y transformación hasta la visualización, aplicando buenas prácticas de ingeniería de datos.

Se construye un pipeline ETL en Python, se modelan los datos en un esquema estrella en SQL y se desarrolla un dashboard en Power BI para el análisis del negocio.

---

## 🎯 Objetivos

* Construir un proceso ETL modular y reproducible
* Diseñar un modelo dimensional (esquema estrella)
* Implementar una base de datos en SQLite
* Crear un dashboard interactivo en Power BI
* Generar insights a partir de los datos

---

## 🏗️ Arquitectura del Proyecto

```text
data/raw → ETL (Python) → SQLite (modelo estrella) → Export CSV → Power BI
```

---

## 🛠️ Tecnologías utilizadas

* **Python** (Pandas, SQLite3)
* **SQL (SQLite)**
* **Power BI**
* **Git & GitHub**

---

## 📂 Estructura del Proyecto

```text
project/
│
├── data/
│   └── raw/                  
│       └── Superstore.csv       # Dataset original
│
├── src/
│   ├── etl/
│   │   ├── config.py         # Rutas del pipeline ETL
│   │   ├── extract.py        
│   │   └── transform.py      
│   │
│   └── db/
│       ├── load.py           
│       ├── export.py         
│       └── validation.py     
│
├── sql/
│   └── schema.sql            
│
├── dashboard/
│   └── sales_dashboard.pbix  
│
├── notebooks/
│   ├── eda.ipynb             
│   └── config.py             # Ruta para el análisis exploratorio
│
├── main.py                   
└── README.md
```

---

## 🔄 Proceso ETL

### 1. Extracción

* Lectura del dataset desde CSV
* Validación inicial

---

### 2. Transformación

* Limpieza (`clean_data`)
* Normalización de columnas (snake_case)
* Construcción de dimensiones:

  * `dim_product`
  * `dim_customer`
  * `dim_location`
  * `dim_ship_mode`
  * `dim_date`
* Generación de claves sustitutas
* Construcción de `fact_sales`

---

### 3. Modelo de datos

Definido en `sql/schema.sql`:

* Tabla de hechos: `fact_sales`
* Dimensiones: producto, cliente, ubicación, envío y fecha

Incluye:

* `order_date_key`
* `ship_date_key`

---

### 4. Carga (Load)

* Creación dinámica de la base de datos SQLite
* Ejecución del schema SQL
* Inserción de datos desde DataFrames

---

### 5. Exportación

* Exportación de tablas a CSV
* Archivos consumidos por Power BI

---

## ⚙️ Configuración del Proyecto

Este proyecto requiere configurar rutas antes de su ejecución.

---

### 🔹 1. Configuración del ETL (`src/etl/config.py`)

Debes actualizar las siguientes variables:

```python
FILE_PATH = "ruta/al/dataset.csv"
DB_PATH = "ruta/donde/se/creara/sales.db"
SCHEMA_PATH = "ruta/al/schema.sql"
PROCESSED_DATA_PATH = "ruta/salida/csv/"
```

---

### 🔹 2. Configuración del EDA (`notebooks/config.py`)

Para ejecutar el notebook:

```python
FILE_PATH = "ruta/al/dataset.csv"
```

---

## ▶️ Cómo ejecutar el proyecto

---

### 🔹 1. Configurar rutas

Antes de ejecutar, asegúrate de modificar:

* `src/etl/config.py`
* `notebooks/config.py`

---

### 🔹 2. Ejecutar pipeline ETL

```bash
python main.py
```

Esto ejecuta:

* Extracción
* Transformación
* Creación de base de datos SQLite
* Carga de datos
* Exportación a CSV

---

### 🔹 3. Análisis exploratorio (opcional)

Abrir:

```text
notebooks/eda.ipynb
```

Y ejecutar las celdas después de configurar la ruta.

---

### 🔹 4. Dashboard

Abrir el archivo:

```text
dashboard/sales_dashboard.pbix
```

---

## ✅ Validaciones de calidad de datos

* Conteo de registros
* Integridad referencial
* Validación de claves
* Consistencia entre origen y modelo

---

## 📊 Dashboard en Power BI

### 🔹 Overview

* KPIs principales
* Tendencia temporal
* Análisis por categoría y región

---

### 🔹 Productos

* Ventas vs rentabilidad
* Identificación de pérdidas
* Evaluación del portafolio

---

### 🔹 Región y Clientes

* Desempeño geográfico
* Segmentación de clientes
* Análisis de concentración

---

## 💡 Principales Insights

* Margen de ganancia ~12%
* Estacionalidad en fin de año
* Portafolio diversificado
* Subcategorías con problemas de rentabilidad (Tables)
* Baja dependencia de clientes o regiones

---

## ⚠️ Retos encontrados

* Problemas de formato decimal en Power BI
* Validación del modelo estrella
* Manejo de múltiples fechas

---

## 📌 Mejoras futuras

* Logging del pipeline
* Automatización
* Pruebas de calidad más robustas
* Escalabilidad

---

## 👤 Autor

Proyecto desarrollado como parte de portafolio en analítica e ingeniería de datos.
