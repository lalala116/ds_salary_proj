#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:13:10 2021

@author: shamah
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}
data = {'input': data_in}

r = requests.get(URL, headers = headers, json = data)

r.json()