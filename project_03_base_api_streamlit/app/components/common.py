import streamlit as st

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
        <{nivel} style='
            text-align:center;
            margin-bottom:15px;
        '>
        {titulo}
        </{nivel}>
        """,
        unsafe_allow_html=True
    )

    
