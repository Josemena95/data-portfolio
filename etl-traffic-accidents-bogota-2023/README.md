# ETL Traffic Accidents in Bogotá (2023)

## 📌 Descripción del proyecto
Este proyecto desarrolla un proceso **ETL (Extract, Transform, Load)** y un **análisis estadístico descriptivo** a partir de datos públicos de accidentalidad vial en la ciudad de Bogotá durante el año 2023.  

El objetivo principal es **preparar los datos para tareas de modelación predictiva**, particularmente:
- Clasificación de la gravedad de los accidentes.
- Análisis y preparación de series de tiempo sobre la frecuencia diaria de personas accidentadas.

El proyecto se desarrolló en el contexto de una especialización en Analítica y Ciencia de Datos y fue adaptado para su presentación como caso práctico en un portafolio profesional.


---


## 📁 Estructura del proyecto

```text
etl-traffic-accidents-bogota-2023/
├── data/
│   ├── raw/        # Datos originales sin transformación
│   └── processed/ # Datos procesados listos para análisis y modelado
├── notebooks/     # Exploración, ETL y análisis
└── README.md
```text

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
- **Separación de variables categóricas y numéricas** para análisis descriptivo.
- **Codificación de variables categóricas** mediante One-Hot Encoding.
- **Estandarización de la variable Edad** para su uso en modelos predictivos.

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

## 🧠 Preparación para modelación

El dataset final se prepara para dos enfoques:

### 1. Clasificación de la gravedad del accidente
- Codificación de la variable objetivo.
- División del dataset en conjuntos de entrenamiento y prueba (80/20).

### 2. Análisis de series de tiempo
- Agregación diaria por localidad.
- Separación de datos en entrenamiento y prueba usando ventanas temporales.
- Identificación de patrones semanales y anomalías.

---

## 🛠️ Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SciPy
- Statsmodels

---

## 📌 Nota
Este proyecto se enfoca principalmente en la **preparación y exploración de datos**, sirviendo como base para modelos predictivos que pueden desarrollarse en etapas posteriores.
