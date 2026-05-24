import streamlit as st
import pandas as pd
from utils.api_client import fetch_data
from components.header import render_header
from components.sidebar import render_sidebar
from components.kpis import render_kpis
from components.tables import render_table
from components.charts import render_bar_chart
from components.common import render_section_title

# configuracion de pagina
st.set_page_config(
    page_title= "Dashboard Analítico de Accidentes",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# seccion Header

render_header()

# seccion KPIS

render_section_title("Indicadores generales")
st.write("")
st.write("")

# respuesta y transformacion de respuesta a Json 
total_accidents_json=fetch_data("accidents/total")
fatal_accidents_json=fetch_data("accidents/fatal")

if total_accidents_json is not None and fatal_accidents_json is not None:


    total_accidents = total_accidents_json["total_accidents"]
    fatal_accidents = fatal_accidents_json["total_fatal_accidents"]

    # KPI Accidentes totales con st.metric
    render_kpis(total_accidents,fatal_accidents)
    
else:
    st.warning("No fue posible obtener datos de accidentes.")
    #division 2
    st.divider()


# seccion Tabla analitica(accidentes por localidad)


render_section_title("Accidentes por localidad")

st.write("")
st.write("")


#creaccion columnas del layout
table_col, chart_col = st.columns([2,3],
                                  gap="xxlarge")

# Tabla accidentes por localidad

# respuesta y transformacion de respuesta a Json 
accidents_by_locality_json = fetch_data("accidents/by-locality")

if accidents_by_locality_json is not None:
    
    # Conversión a dataframe
    accidents_by_locality_df = pd.DataFrame(accidents_by_locality_json)

    with table_col:
        
        # visualizacion de dataframe
        render_table(accidents_by_locality_df)


    # grafico de barras de accidentes por localidad
    top_10_localities = accidents_by_locality_df.head(10) 

    # preparacion del dataframe para el grafico
    chart_df = top_10_localities.set_index("Localidad")

    with chart_col:

        # titulo del grafico
       
        render_section_title("Top 10 Localidades con Mayor Número de Accidentes","h4")

        st.write("")

        render_bar_chart(chart_df)

else:
    st.info("Tabla temporalmente no disponible.")


# division 3
st.divider()



#Consulta por localidad


#Subtitulo de  seccion
render_section_title("Consulta por localidad")

st.write("")
st.write("")


# Condicional seccion
if accidents_by_locality_json is not None:

    #Transformacion de serie localidades a lista de localidades
    localities = accidents_by_locality_df["Localidad"].to_list()

    # Lista de localidades mas opcion de pregunta
    localities = ["Seleccione una localidad"] + localities

    # Creacion de selectbox
    selected_locality = st.selectbox(
        "Seleccione una localidad",
        options=localities
    )

    #condicional  que limita el uso del fetch
    if selected_locality != "Seleccione una localidad":

        # Creacion de ruta endpoint 
        endpoint = f"accidents/locality/{selected_locality}"
        
        # Respuesta y Transformacion de respuesta a Json 
        locality_filter_json = fetch_data(endpoint)


        
        if locality_filter_json is not None:

            locality_filter_df = pd.DataFrame(
                locality_filter_json
            )

            render_table(locality_filter_df)

    else:

        st.info(
            "Seleccione una localidad para consultar información."
        )

else:

    st.error(
        "No fue posible cargar las localidades desde la API."
    )


# Seccion Sidebar

 
# # Estado API
api_status = total_accidents_json is not None


render_sidebar(api_status)