import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import (
    CHART_HEIGHT,
    CHART_MARGIN,
    CHART_COLORWAY,
    PLOTLY_TEMPLATE,
    FONT_FAMILY,
    FONT_SIZE,
    TITLE_X,
    BAR_SHOW_LEGEND,
    DONUT_SHOW_LEGEND,
    TREEMAP_SHOW_LEGEND
)


def render_bar_chart(
    dataframe: pd.DataFrame,
    horizontal: bool = True,
    title: str | None = None
):
    """
    Renderiza un gráfico de barras a partir
    de un DataFrame preparado previamente.

    Args:

        dataframe (pd.DataFrame):
            DataFrame utilizado para construir
            el gráfico.

        horizontal (bool):

            True  -> gráfico horizontal
            False -> gráfico vertical
    """

    x_col = dataframe.columns[0]
    y_col = dataframe.columns[1]

    if horizontal:

        x = y_col
        y = x_col
        orientation = "h"

    else:

        x = x_col
        y = y_col
        orientation = "v"

    fig = px.bar(
        dataframe,
        x=x,
        y=y,
        orientation=orientation,
        color_discrete_sequence=CHART_COLORWAY
    )

    fig.update_layout(

    template=PLOTLY_TEMPLATE,

    height=CHART_HEIGHT,

    margin=CHART_MARGIN,

    font=dict(
        family=FONT_FAMILY,
        size=FONT_SIZE
    ),

 

    

    showlegend=BAR_SHOW_LEGEND
)

    fig.update_traces(
    hovertemplate="%{x}<extra></extra>"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)
    

def render_donut_chart(
    dataframe: pd.DataFrame,
    names: str,
    values: str,
    title: str |None = None
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
        hole=0.45,
        color_discrete_sequence=CHART_COLORWAY
    )

    fig.update_traces(

    textposition="outside",

    textinfo="percent+label",

    pull=[0.02]*len(dataframe)
    )

    fig.update_layout(


    template=PLOTLY_TEMPLATE,

    height=CHART_HEIGHT,

    margin=CHART_MARGIN,

    font=dict(
        family=FONT_FAMILY,
        size=FONT_SIZE
    ),

    legend=dict(
        orientation="h",
        y=-0.15,
        x=0.5,
        xanchor="center"
    ),

    showlegend=DONUT_SHOW_LEGEND
)
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
def render_treemap_chart(
    dataframe: pd.DataFrame,
    names: str,
    values: str,
    title:str|None = None
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
        values=values,
        color_discrete_sequence=CHART_COLORWAY
    )

    fig.update_traces(

    textinfo="label+percent entry",

    textfont_size=14
    )

    fig.update_layout(



    template=PLOTLY_TEMPLATE,

    height=CHART_HEIGHT,

    margin=CHART_MARGIN,

    font=dict(
        family=FONT_FAMILY,
        size=FONT_SIZE
    ),

    showlegend=TREEMAP_SHOW_LEGEND

    
)
    st.plotly_chart(
        fig,
        use_container_width=True)
    