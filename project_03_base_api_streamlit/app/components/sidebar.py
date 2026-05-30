import streamlit as st



import streamlit as st


def render_sidebar(
    api_status: bool,
    localidades: list[str] | None = None,
    condiciones: list[str] | None = None,
    sexo: list[str]|None = None,
    horario: list[str]|None = None
) -> tuple[str, str,str,str] | None:

    """
    Renderiza el sidebar del dashboard incluyendo:

    - estado de la API
    - filtro global por localidad
    - filtro global por condición
    - filtro global por sexo
    - filtro global por horario
    Args:
        api_status (bool):
            Estado de disponibilidad de la API.

        localidades (list[str] | None):
            Lista utilizada para construir
            el filtro de localidades.

        condiciones (list[str] | None):
            Lista utilizada para construir
            el filtro de condición.

        sexo (list[str] | None):
            Lista utilizada para construir
            el filtro de condición.

        horario (list[str] | None):
            Lista utilizada para construir
            el filtro de condición.            
    Returns:
        tuple[str, str,str,str] | None:

        (
            selected_localidad,
            selected_condicion
        )

        Retorna None si la API no está disponible.
    """

    st.sidebar.title(
        "🛣️ Dashboard Analítico"
    )

    st.sidebar.markdown(
        """
        Aplicación interactiva de consulta
        de accidentalidad vial.
        """
    )

    st.sidebar.divider()

    st.sidebar.subheader(
        "Estado API"
    )

    if not api_status:

        st.sidebar.markdown(
            "🔴 API Desconectada"
        )

        return None

    st.sidebar.markdown(
        "🟢 API Conectada"
    )

    st.sidebar.divider()

    st.sidebar.subheader(
        "Filtros globales"
    )

    selected_localidad = st.sidebar.selectbox(
        "Seleccione una localidad",
        options=["Todas"] + localidades
    )

    selected_condicion = st.sidebar.selectbox(
        "Seleccione una condición",
        options=["Todas"] + condiciones
    )

    selected_sexo = st.sidebar.selectbox(
        "Seleccione un sexo",
        options=["Todos"] + sexo
    )

    selected_horario = st.sidebar.selectbox(
        "Seleccione un horario",
        options=["Todos"] + horario
    )
    return (
        selected_localidad,
        selected_condicion,
        selected_sexo,
        selected_horario
    )



