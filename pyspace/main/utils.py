"""
This file contains utils functions for the main
blueprint.
"""
import requests
import json


def get_space_launches():
    API_END_POINT = "https://ll.thespacedevs.com/2.0.0/launch/?limit=10"
    launches = requests.get(API_END_POINT)
    launches_data = json.loads(launches.text)

    return launches_data
