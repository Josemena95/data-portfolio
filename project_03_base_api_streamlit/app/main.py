import streamlit as st
import pandas as pd
from utils.api_client import fetch_data
from components.header import render_header
from components.sidebar import render_sidebar
from components.kpis import render_kpis
from components.tables import render_table
from components.charts import render_bar_chart, render_donut_chart, render_treemap_chart
from components.common import render_section_title
from utils.theme import SECTION_GAP

# configuracion de pagina


st.set_page_config(
    page_title= "Dashboard Analítico de Accidentes",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# respuesta y transformacion de respuesta a Json 
health_json=fetch_data("/health")
sidebar_accidents_by_locality_json = fetch_data("accidents/by-locality")
accidents_by_condition_json = fetch_data("/accidents/by-condition")

# Conversión a dataframe
sidebar_accidents_by_locality_df = pd.DataFrame(sidebar_accidents_by_locality_json)
accidents_by_condition_df = pd.DataFrame(accidents_by_condition_json)




# Seccion Sidebar

# Estado API
api_status = health_json is not None


if  health_json:
    
    # lista localidades
    localities_sidebar = (
        sidebar_accidents_by_locality_df["Localidad"]
        .sort_values()
        .tolist()
    )
    
    # lista localidades
    conditions_sidebar =(
        accidents_by_condition_df["condicion"]
        .sort_values()
        .tolist()
    )

    # lista sexo
    sex_sidebar =["Masculino", "Femenino"]

    #lista de horario
    horario_sidebar = ["Madrugada","Mañana","Tarde","Noche"]

    selected_localidad,selected_condicion, selected_sex,selected_horario = render_sidebar(
        api_status,
        localities_sidebar,
        conditions_sidebar,
        sex_sidebar,
        horario_sidebar
    )

    # diccionario filtros globales
    params = {}


    if selected_localidad != "Todas":

        params["localidad"] = selected_localidad
    
    if selected_condicion != "Todas":

        params["condicion"] = selected_condicion

    if selected_sex != "Todos":

        params["sexo"] = selected_sex
    
    if selected_horario != "Todos":

        params["horario"] = selected_horario

else :
    render_sidebar(api_status)







# seccion Header


render_header()



# seccion KPIS



kpi_section = st.container()

with kpi_section:

    render_section_title("Indicadores generales")

    for _ in range(SECTION_GAP):
        st.write("")


# respuesta y transformacion de respuesta a Json
total_accidents_json=fetch_data("accidents/total",params) 
fatal_accidents_json=fetch_data("accidents/fatal",params)
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



#filtros para graficos de localidad 


localidad_params=params.copy()
localidad_params.pop("localidad",None)

# respuesta y transformacion de respuesta a Json 
accidents_by_locality_json = fetch_data("accidents/by-locality",params=localidad_params)


#creaccion columnas del layout
table_col, chart_col = st.columns(
    [1.8, 2.2],
    gap="large"
)



# Tabla accidentes por localidad


if accidents_by_locality_json is not None:
    
    # Conversión a dataframe
    accidents_by_locality_df = pd.DataFrame(accidents_by_locality_json)
    with table_col:
        
        render_section_title("Tabla accidentes por localidad","h4")

        # visualizacion de dataframe
        render_table(accidents_by_locality_df)


    # grafico de barras de accidentes por localidad
    top_10_localities = accidents_by_locality_df.head(10).sort_values(by="total_accidentes",ascending=True)
 


    with chart_col:

        # titulo del grafico
       
        render_section_title("Top 10 Localidades con Mayor Número de Accidentes","h4")

        st.write("")

        render_bar_chart(top_10_localities)

else:
    st.info("Tabla temporalmente no disponible.")





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
    localities = ["Consultar localidad específica"] + localities

    # Creacion de selectbox
    selected_locality = st.selectbox(
        "Consultar localidad específica",
        options=localities
    )

    #condicional  que limita el uso del fetch
    if selected_locality != "Consultar localidad específica":

        # Creacion de ruta endpoint 
        endpoint = f"accidents/locality/{selected_locality}"
        

        locality_filter_params = params.copy()
        locality_filter_params.pop("localidad",None)


        # Respuesta y Transformacion de respuesta a Json 
        locality_filter_json = fetch_data(endpoint,locality_filter_params)


        
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

st.divider()



# section  Distribuciones (gravedad|sexo):



#creacion columnas del layout
donut_chart_gravedad, donut_chart_sexo = st.columns(
    [1.2,1.2],
    gap="large"
)

with donut_chart_gravedad:
    render_section_title("Distribución por gravedad","h3")
    st.write("")

    
    accidents_by_severity_json= fetch_data("/accidents/by-severity",params = params)
    if accidents_by_severity_json is not None:
        accidents_by_severity_df = pd.DataFrame(accidents_by_severity_json)
        render_donut_chart(accidents_by_severity_df,names="gravedad",values="cantidad")

    else:
        st.warning("No fue posible obtener datos de accidentes.")

with donut_chart_sexo:
    render_section_title("Distribución por sexo","h3")
    st.write("")

    sex_filter_params = params.copy()
    sex_filter_params.pop("sexo",None)
    accidents_by_sex_json= fetch_data("/accidents/by-sex", params= sex_filter_params)
    if accidents_by_sex_json is not None:
        accidents_by_sex_df = pd.DataFrame(accidents_by_sex_json)
        render_donut_chart(accidents_by_sex_df,names="sexo",values="cantidad")

    else:
        st.warning("No fue posible obtener datos de accidentes.")


st.divider()



# Seccion condicion implicacion (Tipo de accidente| Condicion actor vial)



#creaccion columnas del layout
condition_chart, accident_type_chart = st.columns(
    [1.3,1],
    gap="large"
)

with condition_chart:

    render_section_title(
        "Distribución por condición",
        "h3"
    )

    st.write("")

    conditions_params=params.copy()
    conditions_params.pop("condicion",None)
    accidents_by_condition_json = fetch_data(
        "/accidents/by-condition",
        params= conditions_params
    )

    if accidents_by_condition_json is not None:

        accidents_by_condition_df = pd.DataFrame(
            accidents_by_condition_json
        )
       
        render_treemap_chart(
            accidents_by_condition_df,
            names="condicion",
            values="cantidad"
        )

    else:

        st.warning(
            "No fue posible obtener datos."
        )

with accident_type_chart:

    render_section_title(
        "Tipos de accidente",
        "h3"
    )

    st.write("")

    accidents_by_type_json = fetch_data(
        "/accidents/by-accident-type",params
    )

    if accidents_by_type_json is not None:

        accidents_by_type_df = pd.DataFrame(
            accidents_by_type_json
        )

        
        render_bar_chart(
            accidents_by_type_df
        )

    else:

        st.warning(
            "No fue posible obtener datos."
        )


