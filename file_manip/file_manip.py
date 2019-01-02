from subprocess import check_output
from sys import argv
from urllib.request import urlopen
from pprint import pprint
from os import walk
#from paramiko import *
from Flag import Flag, find_flag, make_flags
from sys import maxsize, getsizeof


def _find_files(fname='ssh', loc= '/'):
    cmd = " ".join(['find', loc, ' -name ', '\"*'+ fname + '*\"', ])
    fnames = check_output(cmd, shell=True).decode('utf-8')
    fname_list = fnames.split('\n')
    i = 0
    for name in fname_list:
        if '/' not in name: del fname_list[i]
        else: continue
        i += 1
    return fname_list

def insert_flag(flag, fname, line_no = None):
    try:
        if type(flag) is not str: flag = bytes(flag)
        else: flag = bytes(flag, encoding='utf-8') 

        lines = []
        new_lines = []

        if line_no == None: 
            with open(fname, 'ba+') as f:
                f.write(flag)
        else: 
            with open(fname, 'br') as f:
                lines = f.readlines()
        
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
            if flag not in line: 
                new_lines.append(line)
            else: 
                continue
        
        data = b''.join(new_lines)

        with open(new_file,'wb') as f: f.write(data)

    except Exception as E: 
        print(E, flag)

def find_files(base_path = '/', fname_flag = 'ssh'):
#def find_files(base_path = '/', fname_flag = False):
    paths = []
    
    for path, dirs, files in walk(base_path):
        if fname_flag == False:
            paths.append(path) 
        else:
            if fname_flag not in path: continue
            paths.append(path)
    return paths

if __name__ == '__main__':
    #flag = argv[1]
    #old_file = '../tests/other_log.log'
    #new_file = '../tests/new_other_log.log'
    #remove_flag(flag, old_file, new_file)
    
    base_path = argv[1]
    flag = argv[2]
    find_files(base_path, flag)
    print(yes)
