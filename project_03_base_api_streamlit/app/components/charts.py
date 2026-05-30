import streamlit as st
import pandas as pd
import plotly.express as px


def render_bar_chart(dataframe:pd.DataFrame,horizontal:bool = True):
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

        sentido (bool):
            Orientación del gráfico.

            True  -> horizontal
            False -> vertical
    """

    st.bar_chart(dataframe,horizontal=horizontal)

    

def render_donut_chart(
    dataframe: pd.DataFrame,
    names: str,
    values: str,
):
    """
    Renderiza un gráfico donut a partir
    de un DataFrame preparado previamente.

    Args:
        dataframe (pd.DataFrame):
            DataFrame utilizado para construir
            el gráfico.

        names (str):
            Columna categórica utilizada
            para las etiquetas.

        values (str):
            Columna numérica utilizada
            para los valores.
    """

    fig = px.pie(
        dataframe,
        names=names,
        values=values,
        hole=0.45
    )

    fig.update_traces(
    textposition="outside",
    textinfo="percent+label"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)
    
def render_treemap_chart(
    dataframe: pd.DataFrame,
    names: str,
    values: str
):
    """
    Renderiza un gráfico treemap a partir
    de un DataFrame preparado previamente.

    Args:
        dataframe (pd.DataFrame):
            DataFrame utilizado para construir
            el gráfico.

        names (str):
            Columna categórica utilizada
            para las etiquetas.

        values (str):
            Columna numérica utilizada
            para los valores.
    """

    fig = px.treemap(
        dataframe,
        path=[names],
        values=values
    )

    
    fig.update_traces(
    textinfo="label+percent entry"
)
    st.plotly_chart(
        fig,
        use_container_width=True
    )