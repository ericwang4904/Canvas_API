import requests
import datetime as dt
from src.data_setup import *
# - All request functions -

# Base
def post_link(url, data=None):
    response = requests.post(f'{API_URL}{url}', headers=REQUEST_HEADERS, data=data)

    if response.status_code == 200:
        return
    if DEBUG_MESSAGES: 
        print(f'Failed with status code: {response.status_code}')
        print(response.text)
def put_link(url, data=None):
    response = requests.put(f'{API_URL}{url}', headers=REQUEST_HEADERS, data=data)

    if response.status_code == 200:
        return
    if DEBUG_MESSAGES: 
        print(f'Failed with status code: {response.status_code}')
        print(response.text)
def get_link(url, data=None):
        response = requests.get(f'{API_URL}{url}', headers=REQUEST_HEADERS, data=data)

        if response.status_code == 200:
            return response.json()
        if DEBUG_MESSAGES: 
            print(f'Failed with status code: {response.status_code}')
            print(response.text)
        return {}
def delete_link(url, data=None):
    response = requests.delete(f'{API_URL}{url}', headers=REQUEST_HEADERS, data=data)
    
    if response.status_code == 200:
        return
    if DEBUG_MESSAGES: 
        print(f'Failed with status code: {response.status_code}')
        print(response.text)

# Mass getting
def courses_teaching():
    response = get_link(f'/api/v1/courses?enrollment_type=teacher')
    return response
def modules_in_course(course_id):
    response = get_link(f'/api/v1/courses/{course_id}/modules')
    return response
def items_in_module(course_id, module_id):
    response = get_link(f'/api/v1/courses/{course_id}/modules/{module_id}/items')
    return response

# Singular Getting
def get_module(course_id, module_id):
    response = get_link(f'/api/v1/courses/{course_id}/modules/{module_id}')
    return response

def get_module_item(course_id, module_id, item_id):
    response = get_link(f'/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}')
    return response
def post_module_item(course_id, module_id, item_data):
    post_link(f'/api/v1/courses/{course_id}/modules/{module_id}/items', data=item_data)
def update_module_item(course_id, module_id, item_id, item_data):
    put_link(f'/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}', data=item_data)
def delete_module_item(course_id, module_id, item_id):
    delete_link(f'/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}')


# - name_id pair functions -

# Base
def canvas_to_name_id_list(item_list, name_key):  #[module_name, module_id]
    return [str(item_list[name_key]), str(item_list['id'])]  # The keys HAVE to be strings for input() compatability
def list_pairs_to_dict(list_pairs):  #[[name_1, id_1], [name_2, id_2], ...] to {name_1 : id_1, name_2 : id_2, ...}
    output_dict = {}
    for pair in list_pairs:
        if pair[0] in output_dict.keys():  # Check if module is already added
            if DEBUG_MESSAGES:
                print(f"Warning: Duplicated item: {pair}. Overriding.")
        
        output_dict[str(pair[0])] = str(pair[1])
    
    return output_dict
def canvas_dict_to_name_id_dict(canvas_dict, name_key='name'):  # data from canvas to {name: id}
    list_pairs = list(map(lambda item_list: canvas_to_name_id_list(item_list, name_key=name_key), canvas_dict))
    dict_pairs = list_pairs_to_dict(list_pairs)
    return dict_pairs

# Getting name_id pairs 
def courses_name_id_dict():
    courses = courses_teaching()
    return canvas_dict_to_name_id_dict(courses)
def modules_name_id_dict(course_id):
    modules = modules_in_course(course_id)
    return canvas_dict_to_name_id_dict(modules)
def items_name_id_dict(course_id, module_id):
    items = items_in_module(course_id, module_id)
    return canvas_dict_to_name_id_dict(items, 'title')

#  The function (singular) that finds modules with the same name
def get_same_modules(cid_list, module_name):
    cid_module_pairs = {}
    for cid in map(str, cid_list):
        # Dictionary of {module_name : module_id}
        dict_pairs = modules_name_id_dict(cid)
        try:
            cid_module_pairs[cid] = dict_pairs[module_name]
        except KeyError:
            if DEBUG_MESSAGES:
                print(f"Warning: Module named {module_name} not found in course {cid}. It will be skipped when posted.")
            cid_module_pairs[cid] = None
    
    return cid_module_pairs

# The functions that push things to courses
def format_module_item_data(item_dict):  # Convert 'key' to 'module_item[key]' bcs get_module_item returns 'key' when api wants 'module_item[key]'
    output_dict = {}
    for key in item_dict.keys():
        output_dict[f'module_item[{key}]'] = item_dict[key]
    
    return output_dict

def post_to_course_group(id_list, course_group):  # [course_id, module_id, item_id]
    # Variables
    main_course_id,main_module_id,main_item_id = id_list
    module_name = str(get_module(main_course_id, main_module_id)['name'])  # possibly replace with [name, id] input?

    upload_modules = get_same_modules(course_group, module_name)

    item_data = get_module_item(main_course_id, main_module_id, main_item_id)
    item_data = format_module_item_data(item_data)

    for course_id in course_group:
        if upload_modules[course_id] == None:
            continue

        post_module_item(course_id, upload_modules[course_id], item_data)
    
    return

# - The functions that print and get input -

# Base
def askfor_selection(name_id_pairs):
    pair_keys = list(name_id_pairs.keys())
    for index,name in enumerate(pair_keys):
        print(f"{index}. {name_id_pairs[name]}: {name}")

    response = input("> ")
    
    try:
        response = int(response)
    except ValueError:
        if DEBUG_MESSAGES:
            print("Error: Response is not an integer")
        return None
    
    try: 
        output = name_id_pairs[pair_keys[response]]
    except IndexError:
        if DEBUG_MESSAGES:
            print("Error: Index out of range")
        return None

    return name_id_pairs[pair_keys[response]]

# the actual input functions
def askfor_id_list():
    print("Which Course?")
    course_id = askfor_selection(courses_name_id_dict())
    if course_id == None:
        return None
    
    print("which Module?")
    module_id = askfor_selection(modules_name_id_dict(course_id))
    if module_id == None:
        return None
    
    print("which Item?")
    item_id = askfor_selection(items_name_id_dict(course_id, module_id))
    if module_id == None:
        return None

    return [course_id, module_id, item_id]

def askfor_course_group():
    print("Which Course Group?")
    response = askfor_selection(courses_groups)
    if response == None:
        return None
    
    return response