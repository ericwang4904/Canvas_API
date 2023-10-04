import logging
import requests

class canvasGetter:
    def __init__(self, API_URL, API_TOKEN):
        self.API_URL = API_URL
        self.API_TOKEN = API_TOKEN
        self.headers = {'Authorization': f'Bearer {API_TOKEN}'}

    def get_link(self, url, data=None):
        response = requests.get(f'{self.API_URL}{url}', headers=self.headers, data=data)

        if response.status_code == 200:
            return response.json()
        logging.error(f'Failed with status code: {response.status_code} and message {response.text}')
        return []

    def post_link(self, url, data=None):
        response = requests.post(f'{self.API_URL}{url}', headers=self.headers, data=data)

        if response.status_code == 201:
            return
        logging.error(f'Failed with status code: {response.status_code} and message {response.text}')

    def get_all_items_in_module(self, course_id, module_id):
        response = self.get_link(f'/api/v1/courses/{course_id}/modules/{module_id}')
        return response

    def post_assignment(self, course_id, assignment_data):
        response = self.post_link(f'/api/v1/courses/{course_id}/assignments', assignment_data)
        return response
    
    def update_assignment(self, course_id, assignment_id, assignment_data):
        response = self.post_link(f'/api/v1/courses/{course_id}/assignments/{assignment_id}', assignment_data)
        return response
    
    def get_course_data(self, course_id):
        response = self.get_link(f'/api/v1/courses/{course_id}')
        return response

    def get_all_courses(self):
        response = self.get_link(f'/api/v1/courses?enrollment_type=teacher')
        return response

    def get_all_modules(self, course_id):
        response = self.get_link(f'/api/v1/courses/{course_id}/modules')
        return response

    def get_all_assignments(self, course_id):
        response = self.get_link(f'/api/v1/courses/{course_id}/assignments')
        return response
    

    
    

    

