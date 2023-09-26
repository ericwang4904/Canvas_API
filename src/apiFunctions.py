from canvasGetter import canvasGetter
from dataEditor import dataEditor
from uiHandler import uiHandler

import canvasapi
import logging

class apiFunctions:
    def __init__(self):
        self.ui_obj = uiHandler()
        self.data_obj = dataEditor()

        API_URL = self.data_obj.data_dict["API_URL"]
        API_TOKEN = self.data_obj.data_dict["API_TOKEN"]
        self.canvas_obj = canvasGetter(API_URL, API_TOKEN)

    def update_across_classes(self, class_list):
        pass
    
    def test(self):
        print(self.canvas_obj.get_all_courses())

