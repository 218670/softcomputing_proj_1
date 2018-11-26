from PIL import Image
import glob
import os
import math
base_path = 'data'
width = height = 32


def get_abs_path():
    parts = __file__.split('/')
    return '/'.join(parts[:-1])

def create_path(original_path: str) -> str:
    split = original_path.split('/')
    folder_path = '/'.join([base_path, split[1]])
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return '/'.join([folder_path, split[2]])

def create_copy_and_resize(path: str) -> Image:
    img = Image.open(path)
    return img.resize((width, height), Image.ANTIALIAS)

def convert_and_create_copy(path: str):
    copy_path = create_path(path)
    resized = create_copy_and_resize(path)
    resized.save(copy_path)


if __name__ == '__main__':
    paths = glob.glob(get_abs_path() + '/**/**.png')
    percent = math.floor(len(paths)/100)
    for idx, path in enumerate(paths):
        if(idx % percent == 0):
            print(f'Done: {math.floor((idx * 100) / len(paths))}%\r', end='')
        convert_and_create_copy(path)
        if idx == len(paths) - 1:
            print('Done: 100%')
    print('Finished')