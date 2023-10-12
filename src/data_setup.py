import json

DEBUG_MESSAGES = True  # Keep it on if you want to get information about bad inputs
LOOP_CUTOFF = 20  # Safety measure that stops searching for things in a course/module/etc. after that many loops. Safety precaution for get_all_paginated in functions 

# Load data
PATH = "data.json"
with open(PATH, "r") as data_file:
    data_dict = json.load(data_file)

# Set up variables
API_KEY = data_dict["API_KEY"]
API_URL = data_dict["API_URL"]
REQUEST_HEADERS = {'Authorization': f'Bearer {API_KEY}'}

courses_groups = data_dict["courses_groups"]

