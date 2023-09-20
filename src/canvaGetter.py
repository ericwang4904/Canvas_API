from canvasapi import Canvas

class canvasGetter:
    def __init__(self, API_TOKEN, API_URL):
        self.API_TOKEN = API_TOKEN
        self.API_URL = API_URL

        self.load_canvas()

    def load_canvas(self):
        self.canvas = Canvas(base_url=self.API_URL, access_token=self.API_TOKEN)

    def return_courses(self, canvas) -> list:
        courses = canvas.get_courses()
        course_list = [course for course in courses]
        return course_list
    
    def return_assignments(self, course) -> list:
        assignments = course.get_assignments()
        assignment_list = [assignment for assignment in assignments]
        return assignment_list

    
    
