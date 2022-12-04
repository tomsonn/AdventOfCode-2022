import os
import sys


def read_file_data(file_path: str) -> list:

    dir_path = '/'.join(sys.argv[0].split('/')[:-1])
    full_path = f'{dir_path}/{file_path}'
    if not os.path.isfile(full_path):
        sys.exit(f'File on path - {full_path} - doesn\'t exist.')

    with open(file_path, 'r') as f:
        content = f.readlines()

    return content
