# 🌐 PROYECTO BASE – API + STREAMLIT (CONSULTA DE ACCIDENTES)

---

## 1. Objetivo Técnico

Construir una arquitectura de consulta de datos basada en una API que permita exponer información de accidentes de tránsito y consumirla mediante una aplicación interactiva en Streamlit.

---

## 2. Dataset

* Tipo: Accidentalidad vial (Bogotá 2023)
* Formato: CSV (procesado previamente en proyecto ETL)
* Volumen: ~250.000 registros
* Contiene:

  * Fecha
  * Localidad
  * Tipo de accidente
  * Actor vial
  * Gravedad
  * Edad

---

## 3. Alcance

Incluye:

* Uso de dataset previamente transformado
* Carga de datos en base de datos SQLite
* Desarrollo de capa de servicios (lógica de negocio)
* Construcción de API con FastAPI
* Desarrollo de aplicación interactiva con Streamlit
* Consumo de API desde frontend

No incluye:

* Machine Learning
* Uso de embeddings o bases vectoriales
* Procesamiento de lenguaje natural (en esta fase)

---

## 4. Arquitectura

CSV / SQL (datos)
→ Capa de servicios (Python + Pandas)
→ API (FastAPI)
→ Aplicación (Streamlit)

---

## 5. Tecnologías

* Python
* Pandas
* SQLite
* FastAPI
* Streamlit
* Requests
* Git
* GitHub
* Visual Studio Code

---

## 6. Metodología de trabajo

* Explicación teórica antes de implementar
* Desarrollo guiado paso a paso
* Separación clara de responsabilidades
* Discusión de alternativas técnicas
* Enfoque en arquitectura modular
* Simulación de entorno profesional (backend + frontend)

---

## 7. Fases

1. Preparación de datos (SQLite)
2. Diseño de capa de servicios
3. Desarrollo de API (FastAPI)
4. Pruebas de endpoints
5. Desarrollo de aplicación (Streamlit)
6. Integración completa (API + App)

---

## 8. Estructura de carpetas

data/

api/
├── main.py
└── routes/
└── accidents.py

app/
└── streamlit_app.py

src/
└── services/
└── accident_service.py

notebooks/
README.md

---

## 9. Modularidad

### Capa de servicios

* `accident_service.py`

  * Carga de datos
  * Filtrado
  * Agrupaciones
  * Cálculo de métricas

### API

* `routes/accidents.py`

  * Definición de endpoints
  * Validación de parámetros
  * Llamado a servicios

### Aplicación

* `streamlit_app.py`

  * Interfaz de usuario
  * Consumo de API
  * Visualización

---

## 10. Reproducibilidad

* Separación de capas (datos, lógica, API, frontend)
* Código modular y reutilizable
* Ejecución independiente de API y aplicación
* Datos accesibles desde base SQLite

---

## 11. Reglas del proyecto

* No mezclar lógica de negocio con la API
* No consumir datos directamente desde Streamlit (usar API)
* Mantener separación de capas
* Documentar endpoints
* Validar entradas de usuario

---

## 12. Estado actual

* Documento base del proyecto creado (api_accidents_project_context.md)
* Dataset disponible desde proyecto ETL anterior
* Se está realizando comprensión conceptual profunda de:
    APIs
    arquitectura cliente-servidor
    FastAPI
    endpoints
    capa de servicios
    flujo request/response
    interacción entre frontend, API y SQLite
* Se está definiendo y entendiendo la arquitectura modular del proyecto
* Aún NO se ha iniciado implementación técnica
* Aún NO se ha creado la estructura física del proyecto
* Aún NO se han definido endpoints iniciales
* Aún NO se ha implementado conexión SQLite
* Aún NO se ha desarrollado capa services
* Aún NO se ha iniciado FastAPI ni Streamlit

---

## 13. Próximo paso

### 🔹 Desarrollo de capa de servicios

* comienzo de estructura técnica
* crear estructura física del proyecto
* inicializar repositorio Git
* configurar entorno virtual
* preparar organización modular
* Posteriormente:
    * iniciar capa de acceso a datos y services
    * definir primeros endpoints de consulta

---



---

## 14. Decisiones tomadas

### 🔹 Base de datos

* Se utilizará SQLite por simplicidad y portabilidad
* Los datos serán cargados desde el dataset procesado del proyecto ETL

---

### 🔹 Arquitectura

* Separación en capas:

  * Servicios (lógica)
  * API (exposición)
  * App (visualización)

---

### 🔹 Manejo de datos

* Los datos son estructurados (tabulares)
* No se utilizarán embeddings ni bases vectoriales
* Las consultas se realizarán mediante:

  * Pandas
  * SQL (si es necesario)

---

### 🔹 Consumo de datos

* Streamlit consumirá la API mediante requests HTTP
* La API será el único punto de acceso a los datos

---

### 🔹 Escalabilidad conceptual

* Este proyecto servirá como base para integración futura con IA:

  * Generación automática de consultas
  * Uso de agentes (LangChain / LangGraph)

---

## 15. Control de versiones y entorno de desarrollo

### Entorno de desarrollo

* Visual Studio Code como editor principal
* Estructura modular del proyecto

---

### Control de versiones

* Uso de Git
* Repositorio en GitHub

---

### Flujo de trabajo

* Commits frecuentes y descriptivos
* Seguimiento por fases
* Versionamiento desde inicio del proyecto

---

### Objetivo

* Mantener trazabilidad de cambios
* Garantizar reproducibilidad
* Simular entorno profesional de desarrollo
