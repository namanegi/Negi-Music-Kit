from interval import *
from note import Note

if __name__ == '__main__':
    ref = 'CDEFGAB'
    OK_count = 0
    NG_count = 0
    for c1 in ref:
        for c2 in reversed(ref):
            for s1 in range(-2, 3):
                for s2 in range(-2, 3):
                    n1 = Note(c1 + (('b' * abs(s1)) if s1<= 0 else ('#' * abs(s1))))
                    # n1 = Note(c1)
                    n2 = Note(c2 + (('b' * abs(s2)) if s2<= 0 else ('#' * abs(s2))))
                    cur_interval = count_interval(n1, n2)
                    # print(n1, n2, cur_interval)
                    check_n2 = note_from_interval(n1, cur_interval)
                    if str(n2) == str(check_n2):
                        OK_count += 1
                    else:
                        print(n1, n2, cur_interval, check_n2)
                        NG_count += 1
    print(OK_count, NG_count)