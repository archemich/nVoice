import os.path
from TheFirstSwitch import *

check_file = os.path.exists('answer.txt')
try:
    f = open('answer.txt', 'r')
    string = f.read()
    print('Заданное имя:')
    print(string)
    f.close()
    
except FileNotFoundError:
    print('Заданное имя отсутствует') 
    THF = zadanie(command()).lower()

