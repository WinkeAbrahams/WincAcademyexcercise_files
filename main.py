__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import glob
import shutil

def clean_cache():
    cache = "cache"
    path = os.path.join(os.getcwd(), cache)
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)
    elif os.path.exists(path):
        shutil.rmtree(path)
        os.makedirs(path)


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    shutil.unpack_archive(zip_file_path, cache_dir_path)


def cached_files():
    cache = "cache"
    path = os.path.join(os.getcwd(), cache)
    list_caches_files = os.listdir(path)
    new_abs_list_caches_files = []
    for item in list_caches_files:
        new_abs_list_caches_files += [os.path.join(path, item)]
    return new_abs_list_caches_files


def find_password(new_abs_list_caches_files): 
    found = False
    for file in new_abs_list_caches_files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    found = True
                    print( line)
                else:
                    found = False
           
  
os.chdir('files')

clean_cache()
cache_zip('c:/Users/winke/OneDrive/Bureaublad/Winc/files/data.zip', 'c:/Users/winke/OneDrive/Bureaublad/Winc/files/cache')
new_abs_list_caches_files = (cached_files())

find_password(new_abs_list_caches_files)


