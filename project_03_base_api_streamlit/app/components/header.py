import streamlit as st

def render_header():
    """
    Renderiza el encabezado principal del dashboard,
    incluyendo el título y la descripción general
    de la aplicación.
    """

    st.markdown(
        """
        <h1 style='
            text-align:center;
            margin-bottom:15px;
        '>
        Dashboard Analítico de Accidentes
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    #descripcion del dashboard 
    st.markdown(
        """
        <p style='text-align:center;'>
        Visualización analítica de accidentalidad vial en Bogotá
        mediante arquitectura basada en SQLite, FastAPI y Streamlit.
        </p>
        """,
        unsafe_allow_html=True
    )
    #division 1
    st.divider()
