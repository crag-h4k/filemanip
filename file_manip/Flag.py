from subprocess import check_output
class Flag:
    def __init__(self, str_flag, fname, line_no, line_text):
        self.str_flag = str_flag
        self.fname = fname
        self.line_no = int(line_no)
        self.line_text = line_text

def find_flag(flag, directory):
    cmd = " ".join(['grep -rnw', directory, '-e', flag])
    flags = check_output(cmd, shell=True).decode('utf-8')
    return [flag] + flags.split('\n')

def make_flags(raw_flags):
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
        print(F.str_flag, F.fname, F.line_no, F.line_text)
        F_list.append(F)
    return F_list
