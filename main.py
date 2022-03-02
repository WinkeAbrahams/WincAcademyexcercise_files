__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

CACHE = "cache"
FILE = "files"
PATH = os.path.join(os.getcwd(), FILE, CACHE)

def clean_cache():
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    elif os.path.exists(PATH):
        shutil.rmtree(PATH)
        os.makedirs(PATH)


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    shutil.unpack_archive(zip_file_path, cache_dir_path)


def cached_files():
    list_caches_files = os.listdir(PATH)
    new_abs_list_caches_files = []
    for item in list_caches_files:
        new_abs_list_caches_files += [os.path.join(PATH, item)]
    return new_abs_list_caches_files


def find_password(new_abs_list_caches_files): 
    found = False
    for file in new_abs_list_caches_files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    found = True
                    password = line.split()[1]
                    return password
                else:
                    found = False


if __name__ == "__main__":  
    clean_cache()
    cache_zip('c:/Users/winke/OneDrive/Bureaublad/Winc/files/data.zip', 'c:/Users/winke/OneDrive/Bureaublad/Winc/files/cache')
    new_abs_list_caches_files = (cached_files())
    find_password(new_abs_list_caches_files)


