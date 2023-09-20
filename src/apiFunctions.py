from canvaGetter import canvasGetter
from dataEditor import dataEditor

class apiFunctions():
    def __init__(self):
        self.data_obj = dataEditor()

        API_URL = self.data_obj.data_dict["API_URL"]
        API_TOKEN = self.data_obj.data_dict["API_TOKEN"]
        self.canvas_obj = canvasGetter(API_URL, API_TOKEN)

    def add_across_classes(self, class_list):
        pass

    def update_across_classes(self, class_list):
        pass
