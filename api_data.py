# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

#Module for getting elements list from api

#Python modules
import requests
import json

def get_elements_list():
    headers = {'Server': 'gunicorn/20.0.4'}
    url = "https://periodic-table-elements-info.herokuapp.com/elements"
    result = requests.get(url, headers= headers)
    
    return json.loads(result.text)