import streamlit as st
from utils.theme import (
    SECTION_TITLE_COLOR,
    SECTION_TITLE_MARGIN,
    SECTION_TITLE_WEIGHT,
    SECTION_TITLE_SIZE
)

def render_section_title(
        titulo:str,
        nivel:str = "h2"
        ):
    

    """
    Renderiza un subtítulo reutilizable
    para secciones del dashboard.

    Args:
        titulo (str):
            texto del subtítulo.

        nivel (str):
            nivel HTML del encabezado.
    """

    st.markdown(
        f"""
        <{nivel} style="
            text-align:center;
            margin-bottom:{SECTION_TITLE_MARGIN};
            color:{SECTION_TITLE_COLOR};
            font-weight:{SECTION_TITLE_WEIGHT};
            font-size:{SECTION_TITLE_SIZE};
        ">

            {titulo}

        </{nivel}>
        """,
        unsafe_allow_html=True
    )

    
