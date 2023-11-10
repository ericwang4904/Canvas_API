from src.data_setup import *
from src.functions import *

def main():
    id_list = askfor_id_list()
    if id_list == None:
        return
    
    course_group = askfor_course_group()
    if course_group == None:
        return

## Added prompt 
    def askaction():
        print("Duplicate (D), Delete (X), or Update (U)?")
        response = input("> ")
        if response == "D" or response == "d":
            post_to_course_group(id_list, course_group)
        elif response == "X" or response == "x":
            delete_to_course_group(id_list, course_group)
        elif response == "U" or response == "u":
            update_to_course_group(id_list, course_group)
    askaction()

if __name__ == "__main__":
    main()