import json

import logging

PATH = "data.json"

class dataEditor:
    def __init__(self):
        self.open_data_file()

    def open_data_file(self):
        self.data_file = open(PATH, "r")
        self.data_dict = json.load(self.data_file)
    def update_data(self):
        self.close_data_file()  # Close read–only file

        write_file = open(PATH, "w")
        json.dump(self.data_dict, write_file)
        write_file.close()

        self.data_file = open(PATH, "r")  # Re–open read–only file

    def close_data_file(self):
        self.data_file.close()
