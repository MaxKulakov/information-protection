import os

CHUNK_SIZE = 2
IGNORED_FILES = ['.DS_Store']

state = int(input('1 - Подсчитать ХЭШ-сумму файлов\n2 - Проверить целостность каталога\n') or 1)


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


# функция нахождения всех файлов в каталоге
def get_path_to_files(path):
    os.chdir(path)
    path_to_files = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name not in IGNORED_FILES:
                path_to_files.append(os.path.join(root, name))
    return path_to_files


path_to_directory = input('Введите путь до директории (folder-with-files по умолчанию): ') \
                    or './folder-with-files'

path_to_hash = input('Введите путь до файла с хэшем (hash.txt по умолчанию): ') \
                or './hash.txt'


# Подсчитать ХЭШ-сумму файлов каталога
if state == 1:
    path_to_files = get_path_to_files(path_to_directory)
    t_str = ''
    for file_path in path_to_files:
        t_str += file_path + ' -- ' + str(get_hash_file(file_path)) + '\n'
    os.chdir('..')
    with open(path_to_hash, 'w') as file:
        file.write(t_str)
    
# Проверить целостность каталога
else:
    path_to_files = {}
    with open(path_to_hash, 'r') as file:
        lines = [line for line in file]
        for line in lines:
            t = line.replace('\n', '').split(' -- ')
            path_to_files[t[0]] = t[1]
    os.chdir(path_to_directory)

    changed_files = []
    for files in path_to_files:
        if os.path.exists(files) and str(get_hash_file(files)) != path_to_files[files]:
            changed_files.append(files)
    os.chdir('..')
    
    current_path_to_files = get_path_to_files(path_to_directory)
    deleted_files = list(set(list(path_to_files)).difference(set(current_path_to_files)))
    added_files = list(set(current_path_to_files).difference(set(list(path_to_files))))

    print('Изменённые файлы: ', *changed_files)
    print('Удалённые файлы: ', *deleted_files)
    print('Добавленные файлы: ', *added_files)
    