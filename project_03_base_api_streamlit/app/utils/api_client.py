
import requests



# Base de URL para endpoints
BASE_URL = "http://127.0.0.1:8000"

# Helper de proceso response  y tranformacion a Json
def fetch_data(endpoint:str):
    """
    Realiza una solicitud HTTP GET a un endpoint de la API
y transforma la respuesta en formato JSON.

Args:
    endpoint (str): endpoint de la API que se desea consultar.
    Ejemplo: "accidents/total"ad

Returns:
    dict | list: respuesta JSON del endpoint.
    """
    try:

        response = requests.get(
            f"{BASE_URL}/{endpoint}"
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return None

    except requests.exceptions.HTTPError:

        return None