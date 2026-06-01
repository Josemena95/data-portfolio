import streamlit as st

from utils.theme import (
    HEADER_TITLE,
    HEADER_SUBTITLE,
    HEADER_TITLE_SIZE,
    HEADER_SUBTITLE_SIZE
)


def render_header():
    """
    Renderiza el encabezado principal del dashboard,
    incluyendo el título y la descripción general
    de la aplicación.
    """

    st.markdown(
            f"""
    <div style="text-align:center;">

    <h1 style="
    margin-bottom:10px;
    font-size:{HEADER_TITLE_SIZE};
    ">

    🚦 {HEADER_TITLE}

    </h1>

    <p style="
    font-size:{HEADER_SUBTITLE_SIZE};
    color:#6B7280;
    max-width:900px;
    margin:auto;
    line-height:1.7;
    ">

    {HEADER_SUBTITLE}

    </p>

    </div>
    """,
            unsafe_allow_html=True
        )

    st.divider()
