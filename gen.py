import os
import sys


def gen_wrong_params():
    print('Please try running to generate all folders for the course:')
    print('python gen.py')
    print('Please try running to generate all files for each day:')
    print('python gen.py scope day folder1 extension1 quantity1 ... folderN extensionN quantityN')
    print('\nExample: python gen.py 1 1 exercises exe 4 lectures lec 5 steps band_name_generator 0')
    print('Creates the following structure:')
    print('days001-010')
    print('|_ day001')
    print('   |_ exercises')
    print('      |_ exe01.py')
    print('      |_ exe02.py')
    print('      |_ exe03.py')
    print('      |_ exe04.py')
    print('   |_ lectures')
    print('      |_ lec01.py')
    print('      |_ lec02.py')
    print('      |_ lec03.py')
    print('      |_ lec04.py')
    print('      |_ lec05.py')
    print('   |_ project')
    print('      |_ band_name_generator.py')


def gen_filenames(params):
    filenames = []
    folders = []
    folder = ''
    extension = ''
    for index, param in enumerate(params):
        if index % 3 == 0:
            folder = param
            folders.append(folder)
        elif index % 3 == 1:
            extension = param
        else:
            quantity = int(param)
            if quantity == 0:
                files = [f'{folder}/{extension}.py']
            else:
                files = [f'{folder}/{extension}{x:02d}.py' for x in range(1, quantity + 1)]
            filenames.extend(files)
    return folders, filenames


def gen_right_params():
    key, day = [int(x) for x in sys.argv[1:3]]
    scopes = {index: f'days{x:03d}-{x + 9:03d}' for index, x in enumerate(range(1, 100, 10), 1)}
    path = f'{scopes[key]}/day{day:03d}'
    os.chdir(path)
    folders, filenames = gen_filenames(sys.argv[3:])
    for folder in folders:
        os.mkdir(folder)
    for filename in filenames:
        with open(filename, 'w'):
            pass


def create_structure():
    folders = {
        f'days{x:03d}-{x + 9:03d}': [f'day{y:03d}' for y in range(x, x + 10)]
        for x in range(1, 100, 10)
    }

    for folder, sub_folders in folders.items():
        os.mkdir(folder)
        for sub_folder in sub_folders:
            os.mkdir(f'{folder}/{sub_folder}')


def generate():
    n = len(sys.argv)
    if n == 1:
        create_structure()
    elif n % 3 == 0:
        gen_right_params()
    else:
        gen_wrong_params()


generate()
