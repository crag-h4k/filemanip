from pprint import pprint
from os import walk

from Flag import Flag, find_flag, make_flags


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

def remove_flag(flag, old_file, new_file):
    try: 
        if type(flag) is not str: flag = bytes(flag)
        else: flag = bytes(flag, encoding='utf-8') 

        lines = []
        new_lines = []

        with open(old_file,'rb') as f:lines = f.readlines()

        for line in lines:
            if flag not in line: new_lines.append(line)
            else: continue
        
        data = b''.join(new_lines)

        with open(new_file,'wb') as f: f.write(data)

    except Exception as E: 
        print(E, flag)

def find_files(base_path = '/', flag = 'find_me'):
    paths = []
    for dirpath, dirs, files in walk(base_path):
        for fname in files:
            if flag not in fname: continue
            paths.append('/'.join([dirpath, fname]))
    return paths

if __name__ == '__main__':
    pprint(find_files())
