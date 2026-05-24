import pandas as pd
import streamlit as st


def render_table(dataframe:pd.DataFrame,
                 titulo:str |None = None ):

    """
    Renderiza una tabla analítica y opcionalmente
    muestra un título asociado a la visualización.

    Args:
        dataframe (pd.DataFrame):
            DataFrame que será visualizado.

        titulo (str | None):
            título opcional de la sección/taba.
    """
    

    if titulo :    

        # titulo del grafico
        st.markdown(
            f"""
            <h4 style='
                text-align:center;
                margin-bottom:15px;
            '>
            {titulo}
            </h4>
            """,
            unsafe_allow_html=True
        )
    
    #visualizacion del dataframe
    st.dataframe(dataframe)
    
    





