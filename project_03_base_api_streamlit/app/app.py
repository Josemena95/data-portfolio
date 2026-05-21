import streamlit as st
import requests
import pandas as pd

# configuracion de pagina
st.set_page_config(
    page_title= "Dashboard Analítico de Accidentes",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)





BASE_URL = "http://127.0.0.1:8000"

# Helper de proceso response  y tranformacion a Json
def fetch_data(endpoint:str):
    """
    Realiza una solicitud HTTP GET a un endpoint de la API
y transforma la respuesta en formato JSON.

Args:
    endpoint (str): endpoint de la API que se desea consultar.
    Ejemplo: "accidents/total"

Returns:
    dict | list: respuesta JSON del endpoint.
    """
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        if response.status_code == 200:
            transformed_json = response.json()
            return transformed_json
        else:
            st.error(f"problema en el endpoint: {endpoint}")
        return None
    
    except requests.exceptions.ConnectionError:

        return None

# seccion Header

# Titulo de pagina

st.markdown(
        """
        <h1 style='
            text-align:center;
            margin-bottom:15px;
        '>
        Dashboard Analitico de Accidentes
        </h1>
        """,
        unsafe_allow_html=True
    )

st.write("")


#descripcion del dashboard 


st.markdown(
    """
    <p style='text-align:center;'>
    Visualización analítica de accidentalidad vial en Bogotá mediante arquitectura basada en SQLite, FastAPI y Streamlit.
    </p>
    """,
    unsafe_allow_html=True
)


#division 1
st.divider()


# seccion KPIS




# subtitulo
st.markdown(
    "<h2 style='text-align:center;'>Indicadores Generales</h2>",
    unsafe_allow_html=True
)

st.write("")
st.write("")


# columnas visuales
left_space, metrics_col, right_space = st.columns([3,2,3])

with metrics_col:
    col1,col2 =st.columns(2,gap="xxlarge")


    # KPI Accidentes totales

    # respuesta y transformacion de respuesta a Json 
    total_accidents_json=fetch_data("accidents/total")

    if total_accidents_json is not None:

        total_accidents = total_accidents_json["total_accidents"]

        # KPI Accidentes totales con st.metric

        with col1:
            st.metric(label="Accidentes Totales", value=total_accidents, border= True,width="content",height="content")
    
    else:
        st.warning("No fue posible obtener datos de accidentes.")


    # KPI Accidentes fatales

    # respuesta y transformacion de respuesta a Json 
    fatal_accidents_json=fetch_data("accidents/fatal")

    if fatal_accidents_json is not None:
        
        fatal_accidents= fatal_accidents_json["total_fatal_accidents"]

        # KPI Accidentes totales con st.metric
        with col2:
            st.metric(label="Accidentes Fatales", value=fatal_accidents,border= True,width="content",height="content")

    else:
          st.warning("No fue posible obtener datos de accidentes.")


#division 2
st.divider()



# seccion Tabla analitica(accidentes por localidad)




st.markdown(
    "<h2 style='text-align:center;'>Accidentes por Localidad</h2>",
    unsafe_allow_html=True
)

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
    accidents_by_locality_dataframe = pd.DataFrame(accidents_by_locality_json)

    with table_col:
        
        # visualizacion de dataframe
        st.dataframe(accidents_by_locality_dataframe)


    # grafico de barras de accidentes por localidad
    top_10_localities = accidents_by_locality_dataframe.head(10) 

    # preparacion del dataframe para el grafico
    chart_dataframe = top_10_localities.set_index("Localidad")

    with chart_col:

        # titulo del grafico
        st.markdown(
        """
        <h4 style='
            text-align:center;
            margin-bottom:15px;
        '>
        Top 10 Localidades con Mayor Número de Accidentes
        </h4>
        """,
        unsafe_allow_html=True
    )

        st.write("")

        st.bar_chart(chart_dataframe,
                     horizontal=True)

else:
    st.info("Tabla temporalmente no disponible.")


# division 3
st.divider()



#Consulta por localidad


#Subtitulo de  seccion
st.markdown(
    "<h2 style='text-align:center;'>Consulta por Localidad</h2>",
    unsafe_allow_html=True
)

st.write("")
st.write("")


# Condicional seccion
if accidents_by_locality_json is not None:

    #Transformacion de serie localidades a lista de localidades
    localities = accidents_by_locality_dataframe["Localidad"].to_list()

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

            locality_filter_dataframe = pd.DataFrame(
                locality_filter_json
            )

            st.dataframe(locality_filter_dataframe)

    else:

        st.info(
            "Seleccione una localidad para consultar información."
        )

else:

    st.error(
        "No fue posible cargar las localidades desde la API."
    )






# sidebar


# Titulo de sidebar
st.sidebar.title("🛣️Dashboard Analítico")

#descripcion
st.sidebar.markdown( 
    """
Aplicación interactiva de consulta de accidentalidad vial.
"""
    
)


# # Estado API

st.sidebar.divider()


#sub titulo seccion
st.sidebar.subheader("Estado API")

# Variable de estado de la  API mediante helper
api_status = fetch_data("accidents/total")
 
# # Estado API
if api_status is not None:

    st.sidebar.markdown("🟢 API Conectada")

else:

    st.sidebar.markdown("🔴 API Desconectada")

st.sidebar.divider()