import json

import logging

PATH = "data.json"

class dataEditor:
    def __init__(self):
        self.open_data_file()

    def open_data_file(self):
        self.data_file = open(PATH, "r")
        self.data_dict = json.load(self.data_file)

    def close_data_file(self):
        self.data_file.close()

    def update_data(self):
        self.close_data_file()  # Close read–only file

        write_file = open(PATH, "w")
        json.dump(self.data_dict, write_file)
        write_file.close()

        self.open_data_file() # Re–open read–only file
    
    def update_course_data(self, course_id, write_data):
        id_string = str(course_id)

        self.data_dict['courses_data'][id_string] = write_data
        self.update_data()
        print('Done!')

    def delete_course_data(self, course_id):
        id_string = str(course_id)
        if not (id_string in self.data_dict['courses_data'].keys()):
            logging.error("ID not found in data.json")
            print("ID not found in data.json")
            return
        
        del(self.data_dict['courses_data'][id_string])
        self.update_data()
        print("Done!")

    def create_course_group(self, name, id_list):
        id_list_string = map(str, id_list)
        
        self.data_dict['courses_groups'][name] = id_list_string
        self.update_data()
        print('Done!')
    
    def delete_course_group(self, name):
        name_string = str(name)
        if not (name_string in self.data_dict['courses_groups'].keys()):
            logging.error("Name not found in data.json")
            print("Name not found in data.json")
            return

        del(self.data_dict['courses_groups'][name_string])
        self.update_data()
        print('Done!')
# All input_functions

    def get_input(self):
        response = input('> ')
        return response
    
    def start_config(self):
        print(' "settings" or blank to cancel ')
        response = self.get_input()
        match response:
            case 'settings':
                self.settings_config()
            case '':
                print('Operation Canceled.')
            case _:
                logging.warning(f'Invalid input {response}')
                print("I don't understand that input.")
        
    def settings_config(self):
        print("Re-enter your Canvas token (blank to pass)")
        response = self.get_input()
        if response != '':
            self.data_dict['API_TOKEN'] = response
        
        print("Re-enter your Canvas URL (blank to pass)")
        response = self.get_input()
        if response != '':
            self.data_dict['API_URL'] = response

        print('All Done!')
    
    
