# ETL Traffic Accidents in Bogotá (2023)

## 📌 Descripción del proyecto

Este proyecto desarrolla un análisis estadístico exploratorio a partir de datos públicos de accidentalidad vial en la ciudad de Bogotá durante el año 2023.

El objetivo principal es caracterizar el comportamiento de la accidentalidad desde una perspectiva descriptiva y temporal, identificando patrones relevantes en términos territoriales, demográficos y estructurales. Para ello se realiza:

* Análisis de variables categóricas (localidad, tipo de accidente, actor vial, gravedad).
* Análisis de variables numéricas (edad, frecuencia diaria de personas accidentadas).
* Evaluación de la distribución estadística y variabilidad de la serie.
* Análisis de autocorrelación y estacionalidad semanal.
* Identificación de anomalías y picos atípicos

El enfoque del proyecto es interpretativo y analítico, orientado a comprender la dinámica del fenómeno.

El proyecto fue desarrollado en el contexto de una especialización en Analítica y Ciencia de Datos y posteriormente adaptado como caso práctico para portafolio profesional.


---


## 📁 Estructura del proyecto

```text
etl-traffic-accidents-bogota-2023/
├── data/
│   ├── raw/        # Datos originales sin transformación
│   └── processed/ # Datos procesados listos para análisis 
├── notebooks/     # Exploración, ETL y análisis
└── README.md
```


## 🗂️ Origen de los datos

Los datos provienen del **Observatorio de Movilidad de Bogotá**, administrado por la **Secretaría Distrital de Movilidad**.  
Se trata de un conjunto de datos de acceso público que registra las características de los siniestros viales ocurridos en las 20 localidades de la ciudad durante el año 2023.

- **Formato original:** Archivo Excel (.xlsx)
- **Tamaño:** ~14 MB
- **Número de siniestros:** 14.106
- **Cobertura geográfica:** 20 localidades de Bogotá
- **Periodo:** Año 2023

El archivo original está organizado en tres tablas:

### 📄 Tablas de origen
- **Siniestros:** Información general del accidente (fecha, hora, ubicación, tipo y condiciones).
- **Vehículos:** Características de los vehículos involucrados.
- **Actor vial:** Información de las personas involucradas (edad, sexo, condición y gravedad).

Los campos originales y los campos seleccionados para el análisis pueden consultarse en el **diccionario de datos** proporcionado por la fuente.

Los datos crudos se mantienen sin modificaciones en la carpeta `data/raw`, siguiendo buenas prácticas de ingeniería de datos.

---

## ⚙️ Proceso ETL

### 1. Extracción
- Lectura directa del archivo Excel desde un repositorio público en GitHub.
- Importación de las tres tablas originales usando `pandas.read_excel()`.

### 2. Transformación
Las principales transformaciones realizadas incluyen:

- **Selección de variables relevantes** para análisis y modelación.
- **Unión de tablas** mediante llaves (`Codigo_Accidente` y `Codigo_Vehiculo`).
- **Tratamiento de valores faltantes**, siguiendo las definiciones del diccionario de datos.
- **Eliminación de registros incompletos y duplicados**.
- **Reducción de cardinalidad** en variables categóricas mediante agrupación de categorías poco frecuentes.


### 3. Carga
- Construcción de DataFrames finales listos para:
  - Modelos de clasificación de gravedad del accidente.
  - Análisis de series de tiempo sobre la frecuencia diaria de accidentes.

---

## 📊 Análisis estadístico

### Análisis descriptivo
- Estudio de la distribución de la edad de las personas involucradas.
- Identificación de outliers mediante IQR.
- Evaluación de normalidad (Q-Q Plot, Shapiro-Wilk y Kolmogorov-Smirnov).
- Análisis de frecuencias para variables categóricas clave como:
  - Localidad
  - Tipo de accidente
  - Tipo de vehículo
  - Gravedad del accidente

### Series de tiempo
Se analiza la frecuencia diaria de personas accidentadas mediante:
- Tendencia (media móvil de 30 días).
- Estacionalidad semanal.
- Variabilidad y volatilidad.
- Autocorrelación (ACF y PACF).
- Identificación de anomalías y picos.

---

## 🛠️ Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels

---


