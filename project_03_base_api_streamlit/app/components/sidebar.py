import streamlit as st



def render_sidebar(api_status:bool):

    """
    Renderiza el sidebar del dashboard, incluyendo
    la descripción general y el estado de conexión
    de la API.

    Args:
        api_status (bool): indica si la API se
        encuentra disponible.
    """


    # Titulo de sidebar
    st.sidebar.title("🛣️Dashboard Analítico")

    #descripcion
    st.sidebar.markdown( 
        """
    Aplicación interactiva de consulta de accidentalidad vial.
    """
        
    )


    st.sidebar.divider()


    #sub titulo seccion
    st.sidebar.subheader("Estado API")

    # Variable de estado de la  API mediante helper
    api_status
    
    # # Estado API
    if api_status :
         st.sidebar.markdown("🟢 API Conectada")

    else:
        st.sidebar.markdown("🔴 API Desconectada")

    st.sidebar.divider()

