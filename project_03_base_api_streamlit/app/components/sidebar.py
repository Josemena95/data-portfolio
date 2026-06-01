import streamlit as st

from utils.theme import (
    SIDEBAR_TITLE,
    SIDEBAR_DESCRIPTION
)

def render_sidebar(
    api_status: bool,
    localidades: list[str] | None = None,
    condiciones: list[str] | None = None,
    sexo: list[str] | None = None,
    horario: list[str] | None = None
) -> tuple[str, str, str, str] | None:

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

    with st.sidebar:

        st.title(
            SIDEBAR_TITLE
        )

        st.caption(
            SIDEBAR_DESCRIPTION
        )

        st.divider()

        st.subheader(
            "Estado servicio API"
        )

        if not api_status:

            st.error(
                "API desconectada"
            )

            return None

        st.success(
            "API conectada"
        )

        st.divider()

        st.subheader(
            "Filtros globales"
        )

        selected_localidad = st.selectbox(
            "📍 Localidad",
            options=["Todas"] + localidades
        )

        selected_condicion = st.selectbox(
            "⚠️ Condición",
            options=["Todas"] + condiciones
        )

        selected_sexo = st.selectbox(
            "👤 Sexo",
            options=["Todos"] + sexo
        )

        selected_horario = st.selectbox(
            "🕒 Horario",
            options=["Todos"] + horario
        )

    return (
        selected_localidad,
        selected_condicion,
        selected_sexo,
        selected_horario
    )