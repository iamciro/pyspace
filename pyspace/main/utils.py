"""
This file contains utils functions for the main
blueprint.
"""
import requests
import json
from datetime import datetime


def convert_str_to_datatime(str_value):
    '''
        Converts a string to a datime with the
        %Y-%m-%d %H:%M:%S format.
    '''
    # Format string
    str_value = str_value.replace('T', ' ').replace('Z', '')
    # Convert to datetime
    datetime_value = datetime.strptime(str_value, '%Y-%m-%d %H:%M:%S')
    return datetime_value


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
