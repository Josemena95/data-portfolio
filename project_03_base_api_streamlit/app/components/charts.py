import streamlit as st
import pandas as pd


def render_bar_chart(dataframe:pd.DataFrame,sentido:str = True):
    """
    Renderiza un gráfico de barras a partir
    de un DataFrame preparado previamente.

    Args:
        dataframe (pd.DataFrame):
            DataFrame utilizado para construir
            el gráfico.
        sentido str:
        sentido del grafico de barras True si es horizontal, False si es 
        vertical
    """

    st.bar_chart(dataframe,horizontal=sentido)