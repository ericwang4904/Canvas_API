import json

DEBUG_MESSAGES = True

# Load data
PATH = "data.json"
with open(PATH, "r") as data_file:
    data_dict = json.load(data_file)

# Set up variables
API_KEY = data_dict["API_KEY"]
API_URL = data_dict["API_URL"]
REQUEST_HEADERS = {'Authorization': f'Bearer {API_KEY}'}

courses_groups = data_dict["courses_groups"]

