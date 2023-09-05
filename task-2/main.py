import os
import module

CHUNK_SIZE = 2
IGNORED_FILES = ['.DS_Store']

# функция нахождения ХЭШ-суммы
def get_hash_file(path):
    cur_hash = b'\0'
    with open(path, 'rb') as file:
        chunk = file.read(CHUNK_SIZE)
        cur_hash = chunk
        while chunk:
            chunk = file.read(CHUNK_SIZE)
            if chunk != b'':
                if len(chunk) < CHUNK_SIZE:
                    chunk.zfill(CHUNK_SIZE) 
                cur_hash = bytes(a ^ b for a, b in zip(cur_hash, chunk))
    return cur_hash

# функция обновления количества запусков программы
def update_run_count():
    old_count = ''
    with open('module.py', 'r') as file_read:
        old_count = file_read.read()
        old_count = old_count.split(' = ')
        old_count[1] = int(old_count[1]) + 1
    with open('module.py', 'w') as file_write:
        file_write.write(str(old_count[0]) + ' = ' + str(old_count[1]))


path_to_main_file = './main.py'
path_to_hash = './hash.txt'


if module.RUN_COUNT == 0:
    with open(path_to_hash, 'w') as file:
        t = get_hash_file(path_to_main_file)
        file.write(str(t))
        print('Превый запуск программы, ХЭШ-сумма:', str(t))
else:
    if not os.path.exists(path_to_hash):
        print('Не найден ХЭШ-файл контрольной суммы')
    else:
        rf = ''
        with open(path_to_hash, 'r') as file:
            rf = file.read()
        
        if os.path.exists(path_to_hash) and str(get_hash_file(path_to_main_file)) != rf:
            print('! ХЭШ-сумма программы изменилась !')
        if os.path.exists(path_to_hash) and str(get_hash_file(path_to_main_file)) == rf:
            print('ХЭШ-сумма программы не изменилась')

update_run_count()

