import requests


BASE = "https://www.edsm.net/api-v1/"


def get_location(system_name):
    call = BASE + "system?systemName=" + system_name + "&showCoordinates=1"
    return requests.get(call).json().get("coords")
