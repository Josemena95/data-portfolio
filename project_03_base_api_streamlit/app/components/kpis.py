import streamlit as st

from utils.theme import (
    KPI_BORDER,
    KPI_GAP,
    KPI_TOTAL_COLOR,
    KPI_FATAL_COLOR
)


      

def render_kpis(total_accidents:int,
               fatal_accidents:int):
    """
    Renderiza la sección de indicadores del dashboard,
    incluyendo el layout visual y las métricas principales.

    Args:
        total_accidents (int):
            cantidad total de accidentes.

        fatal_accidents (int):
            cantidad total de accidentes fatales.
    """

    st.markdown(
        """
        <style>

        div[data-testid="stMetricValue"]{
            text-align:center;
            justify-content:center;
        }

        div[data-testid="stMetricLabel"]{
            justify-content:center;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    left_space, metrics_col, right_space = st.columns([2,4,2])

    with metrics_col:

        col1, col2 = st.columns(
            2,
            gap=KPI_GAP
        )

        with col1:

            st.markdown(
                f"""
                <div style='color:{KPI_TOTAL_COLOR};
                            font-size:18px;
                            font-weight:600;
                            text-align:center;'>

                Accidentes Totales

                </div>
                """,
                unsafe_allow_html=True
            )

            st.metric(
                label="",
                value=f"{total_accidents:,}",
                border=KPI_BORDER
            )

        with col2:

            st.markdown(
                f"""
                <div style='color:{KPI_FATAL_COLOR};
                            font-size:18px;
                            font-weight:600;
                            text-align:center;'>

                Accidentes Fatales

                </div>
                """,
                unsafe_allow_html=True
            )

            st.metric(
                label="",
                value=f"{fatal_accidents:,}",
                border=KPI_BORDER
            )

    st.divider()
