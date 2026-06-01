# app/utils/theme.py

# ==========
# COLORS
# ==========

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#14B8A6"
ACCENT_COLOR = "#7C3AED"

SUCCESS_COLOR = "#16A34A"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#DC2626"


# ==========
# PLOTLY CONFIG
# ==========

CHART_HEIGHT = 460

CHART_MARGIN = dict(
    l=40,
    r=40,
    t=70,
    b=40
)

CHART_COLORWAY = [
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    ACCENT_COLOR,
    "#F97316",
    "#EC4899"
]


# ==========
# TYPOGRAPHY
# ==========

FONT_FAMILY = "Arial"

FONT_SIZE = 14


# ==========
# TITLES
# ==========

TITLE_X = 0.5


# ==========
# LEGENDS
# ==========

BAR_SHOW_LEGEND = False

DONUT_SHOW_LEGEND = True

TREEMAP_SHOW_LEGEND = False


# ==========
# TEMPLATE
# ==========

PLOTLY_TEMPLATE = "plotly_white"


# ==========
# LAYOUT
# ==========

SECTION_SPACING = "medium"

CARD_RADIUS = 12

# ==========
# KPI CONFIG
# ==========

KPI_BORDER = True

KPI_GAP = "large"

KPI_TOTAL_COLOR = PRIMARY_COLOR

KPI_FATAL_COLOR = ERROR_COLOR


# ==========
# SIDEBAR
# ==========

SIDEBAR_TITLE = "🛣️ Dashboard Analítico"

SIDEBAR_DESCRIPTION = (
    "Aplicación interactiva de consulta "
    "de accidentalidad vial."
)

# ==========
# HEADER
# ==========

HEADER_TITLE = "Dashboard Analítico de Accidentes"

HEADER_SUBTITLE = (
    "Visualización analítica de accidentalidad vial en Bogotá "
    "mediante arquitectura basada en SQLite, FastAPI y Streamlit."
)

HEADER_TITLE_SIZE = "2.8rem"

HEADER_SUBTITLE_SIZE = "1rem"

# ==========
# SECTION TITLES
# ==========

SECTION_TITLE_COLOR = "#111827"

SECTION_TITLE_MARGIN = "20px"

SECTION_TITLE_WEIGHT = "900"

SECTION_TITLE_SIZE = "2rem"

# ==========
# SPACING
# ==========

SECTION_GAP = 1