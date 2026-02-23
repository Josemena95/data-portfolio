# Digital Sales Performance

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo analizar el comportamiento de las ventas digitales durante el último año, evaluando su desempeño frente a las metas comerciales y los costos asociados al envío de mensajes por producto y grupo de nivel.

El análisis integra múltiples fuentes de datos y construye una sábana final consolidada que permite medir indicadores clave de desempeño (KPIs) y visualizar el cumplimiento comercial mediante un dashboard interactivo en Power BI.

---

## 🎯 Objetivos del Análisis

* Analizar la evolución de las ventas digitales por mes y día.

* Evaluar el cumplimiento de metas comerciales mensuales.

* Calcular el costo total asociado a los mensajes enviados por venta.

* Identificar los días con mayor volumen de ventas.

* Medir el porcentaje de cumplimiento frente a las metas establecidas.

---

## 🗂️ Fuentes de Datos

El proyecto integra tres fuentes principales:

### 1️⃣ Ventas Digitales

Contiene información transaccional diaria:

* Fecha de venta

* Código de producto

* Grupo de nivel

* Monto vendido

* Cantidad de ventas por día

### 2️⃣ Metas Digitales

Contiene metas mensuales por producto y grupo:

* Código de producto

* Grupo de nivel

* Mes

* Año

* Meta asignada

### 3️⃣ Mensajes Banco

Contiene información de costos de contacto:

* Código de producto

* Grupo de nivel

* Número de mensajes enviados

* Valor unitario del mensaje

---

## 🛠️ Proceso Técnico

### 🔹 1. Integración y Transformación en SQL (SQLite)

Se realizó el cruce de las tres fuentes mediante llaves lógicas (cod_prod, grp_nivel, mes y año).

Se construyeron los siguientes campos calculados:

* **total_val_msj_dia:**
  
  Cálculo del costo total de mensajes por día:
  venta_dia * vlr_msj

 * **f_ven:**
   
    Conversión de fecha al formato numérico AAAAMMDD.

 * **nombre_mes:**
  
    Campo descriptivo con el nombre del mes de la venta.

 * **p_meta**
   
    Indicador de cumplimiento:
  
    total_val_msj_dia / meta

El resultado es una sábana final consolidada lista para análisis y visualización.

---

## 🔹 2. Modelado y Visualización en Power BI

Se construyó un dashboard interactivo que incluye:

* 📈 Ventas por mes y día.

* 💬 Cantidad de mensajes enviados y costo mensual.

* 🏆 Top 10 fechas con mayor volumen de ventas.

* 📊 Comparativo entre costo total de mensajes y meta.

* 📌 Indicador de porcentaje de cumplimiento (p_meta).

El reporte permite segmentación dinámica por:

* Producto

* Grupo de nivel

* Mes

* Día

---

## 📊 Principales Indicadores (KPIs)

* Total de ventas

* Total de monto vendido

* Costo total de mensajes

* Meta mensual

* Porcentaje de cumplimiento

---

## 🏗️ Estructura del Proyecto

```text
project-02-digital-sales-performance/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   └── transformaciones.sql
│
├── powerbi/
│   └── digital_sales_dashboard.pbix
│
├── images/
│   └── dashboard_preview.png
│
└── README.md
```
---

## 🚀 Tecnologías Utilizadas

- SQL (SQLite)

- Power BI

- Integración de múltiples fuentes de datos

- Construcción de métricas derivadas

- Visualización y análisis de KPIs

---

## 📌 Enfoque Analítico

- Este proyecto demuestra capacidades en:

- Integración de múltiples fuentes de datos

- Transformación y enriquecimiento de datos

- Construcción de métricas de negocio

- Modelado analítico

- Visualización ejecutiva para toma de decisiones

---
