"""
This file contains utils functions for the main
blueprint.
"""
import requests
import json


def get_space_launches(limit=10):
    '''
        This function calls to the Space Launch API and gets Space Launches.
        It returns a list of dictionaries if they're found and None otherwise.
    '''
    try:
        API_END_POINT = f"https://ll.thespacedevs.com/2.0.0/launch/?mode=list&limit={limit}"
        launches = requests.get(API_END_POINT)
        launches_data = json.loads(launches.text)
        return launches_data['results']
    except KeyError:
        return None
