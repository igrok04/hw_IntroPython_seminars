
from os.path import exists
from creating_file import creating
import os
os.chdir(os.path.dirname(__file__))

def check_exist():
    print('Проверка на наличие имеющейся базы данных...')
    path = 'pupils.csv'
    valid = exists(path)
    if not valid:
        creating(path)
        return 'Создана таблица для новой базы данных.'
    else:
        return 'База данных найдена.'