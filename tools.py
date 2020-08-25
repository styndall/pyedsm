import requests


BASE = "https://www.edsm.net/api-v1/system?systemName="
COORDS = "&showCoordinates=1"
STAR_TYPE = "&showPrimaryStar=1"
INFO = "&showInformation=1"
PERMIT = "&showPermit=1"

def get_location(system_name):
    call = BASE + system_name + COORDS
    return requests.get(call).json().get("coords")

def get_star_type(system_name):
    call = BASE + system_name + STAR_TYPE
    return requests.get(call).json().get("primaryStar").get("type")

def get_info(system_name):
    call = BASE + system_name + INFO
    return requests.get(call).json().get("information")
