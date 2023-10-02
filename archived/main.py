import logging
from apiFunctions import apiFunctions

logging.basicConfig(filename='app.log',
 level=logging.DEBUG,
 filemode='w', 
 format='%(asctime)s - %(filename)s:%(funcName)s:%(levelname)s:%(message)s', 
 datefmt='%m/%d/%Y %H:%M:%S')

def main():
    api = apiFunctions()
    api.test()


if __name__ == '__main__':
    main()