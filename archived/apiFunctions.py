from canvasGetter import canvasGetter
from dataEditor import dataEditor
from datetimeFunctions import datetimeFunctions

import datetime as dt
import logging

class apiFunctions:
    def __init__(self):
        self.data_obj = dataEditor()
        self.dt_obj = datetimeFunctions()
        
        API_URL = self.data_obj.data_dict["API_URL"]
        API_TOKEN = self.data_obj.data_dict["API_TOKEN"]
        self.canvas_obj = canvasGetter(API_URL, API_TOKEN)

    def get_input(self):
        response = input('> ')
        return response

    def inp_remove_course(self):
        print('What is the course id? (blank to cancel)')
        course_id = self.get_input()
        if course_id == '':
            print('Operation canceled.')
            return
        try:
            int(course_id)
        except ValueError:
            print("Course ID must be an integer.")
            return
        
        self.data_obj.delete_course_data(course_id)

    def inp_add_course(self):
        print('What is the course id? (blank to cancel)')
        course_id = self.get_input()
        if course_id == '':
            print('Operation canceled.')
            return
        try:
            int(course_id)
        except ValueError:
            print("Course ID must be an integer.")
            return
        
        print('What is the course block? (blank to cancel)')
        course_block = self.get_input()
        if course_block == '':
            print('Operation canceled.')
            return
        try:
            int(course_block)
        except ValueError:
            print("Course block must be an integer.")
            return
        if not (1 <= int(course_block) <= 8):
            print("Course block must go from 1 to 8")
            return
        

        course_data = self.canvas_obj.get_course_data(course_id)
        if course_data == []:
            print('Failed to get course data. Possible bad Course ID or network issue. Check logs.')
            return

        write_data = {
            'id': course_id,
            'name': course_data['name'],
            'course_block': course_block
        }

        self.data_obj.update_course_data(course_id, write_data)

    def list_stored_courses(self):
        courses_data = self.data_obj.data_dict['courses_data']
        for i,key in enumerate(courses_data, start=1):
            print(f"{i}. {key}: {courses_data[key]['name']}")
    
    def test(self):
        self.inp_add_course()
        self.list_stored_courses()


