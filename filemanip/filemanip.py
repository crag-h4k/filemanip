from os import walk
from unicodedata import normalize


def normalize_str(string):
    return normalize("NFKD", string.casefold())

def compare_normalized(str0, str1):
    return normalize_str(str0) == normalize_str(str1)

def find_files(base_path, flag):
    paths = []
    _flag = normalize_str(flag)
    for dirpath, dirs, files in walk(base_path):
        for fname in files:
            _fname = normalize_str(fname)
            if _flag not in _fname: continue
            paths.append('/'.join([dirpath, fname]))
    return paths

def insert_flag(flag, fname, line_no = None):
    try:
        if type(flag) is not str: flag = bytes(flag)
        else: flag = bytes(flag, encoding='utf-8') 

        lines = []
        new_lines = []

        if line_no == None: 
            with open(fname, 'ba+') as f: f.write(flag)
        else: 
            with open(fname, 'br') as f: lines = f.readlines()
        
            lines[line_no - 1]  =+ flag
            new_lines = b''.join(lines)

            with open(fname, 'bw+') as f: f.write(new_lines)
 
    except Exception as e: print(e)

def replace_flag(old_flag, new_flag, fname):
    try:  
        if type(old_flag) is not str: old_flag = bytes(flag)
        else: old_flag = bytes(old_flag, encoding='utf-8') 

        if type(new_flag) is not str: new_flag = bytes(flag)
        else: new_flag = bytes(new_flag, encoding='utf-8') 

        new_lines = []
        valid_lines = []
        
        with open(fname,'rb') as f:
            for line in f:
                if old_flag not in line: 
                    new_lines.append(line)
                    continue
                new_line = line.replace(old_flag, new_flag)
                new_lines.append(new_line)
                print(new_line)
            
        valid_lines = b''.join(new_lines)

        with open(fname, 'bw') as f: f.write(valid_lines)
            
    except Exception as E:
        print(E)
    return

def remove_flag(flag, old_file, new_file): 
    new_lines = []
    try:  
        if type(flag) is not str: flag = bytes(flag)
        else: flag = bytes(flag, encoding='utf-8') 


        with open(old_file,'rb') as f:#lines = f.readlines()
            for line in f:
                if flag not in line: new_lines.append(line)
                else: continue
    
        data = b''.join(new_lines)
        with open(new_file,'wb') as f: f.write(data)

    except Exception as E: 
        print(E, flag)

def change_meta(File)
    return
'''
drwxr-xr-x 4 l0k1 l0k1 4.0K Jan  7 15:59 .
drwxr-xr-x 7 l0k1 l0k1 4.0K Jan  7 15:54 ..
-rw-r--r-- 1 l0k1 l0k1 2.5K Jan  7 15:56 filemanip.py
-rw-r--r-- 1 l0k1 l0k1  129 Jan  7 15:38 __init__.py
drwxr-xr-x 2 l0k1 l0k1 4.0K Jan  7 15:57 .ipynb_checkpoints
-rw-r--r-- 1 l0k1 l0k1 9.2K Jan  3 11:30 speed_results.txt
-rw-r--r-- 1 l0k1 l0k1  452 Jan  3 11:30 speed_test.sh
drwxr-xr-x 2 l0k1 l0k1 4.0K Jan  3 11:30 test_logs
-rw-r--r-- 1 l0k1 l0k1 1.3K Jan  7 15:59 Untitled.ipynb
'''
