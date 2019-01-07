from pprint import pprint
from os import walk
from unicodedata import normalize
from sys import argv


def normalize_str(string):
    return normalize("NFKD", string.casefold())

def compare_normalized(str0, str1):
    return normalize_str(str0) == normalize_str(str1)

def find_files(base_path = '/', flag = 'ssh'):
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

def replace_flag(old_flag = 'is', new_flag = 'was', fname = './test_logs/test_log.log')
    return
def remove_flag(flag = 1, old_file = './test_logs/other_log.log', new_file = './test_logs/new_other_log.log'): 
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

if __name__ == '__main__':
    flag = argv[1]
    old_file = argv[2]
    new_file = argv[3]
    #flag = 'summer'
    #old_file = './test_logs/other_log.log'
    #new_file = './test_logs/new_other_log.log'
    remove_flag(flag, old_file, new_file)
