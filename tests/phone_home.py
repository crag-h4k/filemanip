from subprocess import check_output
from os import system
from pprint import pprint
from sys import argv, stdout
from urllib.request import urlopen
#from paramiko import *


class Flag:
    def __init__(self, str_flag, fname, line_no, line_text):
        self.str_flag = str_flag
        self.fname = fname
        self.line_no = int(line_no)
        self.line_text = line_text

def find_files(fname, loc):
    cmd = " ".join(['find', loc, ' -name ', '\"*'+ fname + '*\"', ])
    fnames = check_output(cmd, shell=True).decode('utf-8')
    fname_list = fnames.split('\n')
    i = 0
    for name in fname_list:
        if '/' not in name: del fname_list[i]
        else: continue
        i += 1
    return fname_list

def get_key(url):
    key = urlopen(url).readlines()
    if len(key) != 1: return False
    #else: return key[0]
    else: 
        print(key[0])
        return key[0]

def insert_text(text, fname, line_no = None):
    print(type(text))
    try: text.encode()
    except Exception as e: print(e)
    print(type(text))
    if line_no == None:
        with open(fname, 'ba+') as f: f.write(text)
    else: 
        with open(fname, 'br') as f:
            lines = f.readlines()
            print(lines)
            lines[line_no - 1] += text
        with open(fname, 'bw+') as f:
            for line in lines:
                f.write(line)
    return


def find_flag(flag, loc):
    cmd = " ".join(["grep -iRn", flag, search_dir])
    flags = check_output(cmd, shell=True).decode('utf-8')
    return [flag] + flags.split('\n')

def make_flag(raw_flags):
    F_list = []
    str_flag = raw_flags[0]

    for flag in raw_flags:
        data = [str_flag] + flag.split(':')
        if len(data) != 4: continue
        F = Flag(
            str_flag = data[0],
            fname = data[1],
            line_no = data[2],
            line_text = data[3],)
        F_list.append(F)
        pprint(data)
    return F_list

        
    print(_flags)

def clear_tracks(flag, logs):
    #auth, 
    return

def send_info(text):
    return

if __name__ == '__main__':
    #flag = 'flag'
    #search_dir = '../tests/log'
    #raw_flags = find_flag(flag, search_dir)
    #F_list = make_flag(raw_flags)
    #print(F_list)
    #fname = argv[1]
    #pprint(find_files(fname, '/'))
    url = argv[1]
    fname = argv[2]
    insert_text('poopypants', fname, line_no = 1)
