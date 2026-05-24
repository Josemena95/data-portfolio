import streamlit as st


      

def render_kpis(total_accidents:int,
               fatal_accidents:int):
    """
    Renderiza la sección de indicadores del dashboard,
    incluyendo el layout visual y las métricas principales.

    Args:
        total_accidents (int):
            cantidad total de accidentes.

        fatal_accidents (int):
            cantidad total de accidentes fatales.
    """


    # columnas visuales
    left_space, metrics_col, right_space = st.columns([3,2,3])

    with metrics_col:
        col1,col2 =st.columns(2,gap="xxlarge")


        # KPI Accidentes totales

        with col1:
                st.metric(label="Accidentes Totales", value=total_accidents, border= True,width="content",height="content")
        
        # KPI Accidentes fatales

        with col2:
                st.metric(label="Accidentes Fatales", value=fatal_accidents,border= True,width="content",height="content")

    #division 2
    st.divider()

