"""
This file contains utils functions for the main
blueprint.
"""
import requests
import json


def get_space_launches(limit=10):
    API_END_POINT = f"https://ll.thespacedevs.com/2.0.0/launch/?limit={limit}"
    launches = requests.get(API_END_POINT)
    launches_data = json.loads(launches.text)

    return launches_data
