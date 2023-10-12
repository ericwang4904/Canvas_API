from src.data_setup import *
from src.functions import *

def main():
    id_list = askfor_id_list()
    if id_list == None:
        return
    
    course_group = askfor_course_group()
    if course_group == None:
        return

    post_to_course_group(id_list, course_group)

if __name__ == "__main__":
    main()