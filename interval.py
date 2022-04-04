from note import Note

ref = 'CDEFGAB'
rei = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}

q_list_P = {
    -4: 'qd',
    -3: 'td',
    -2: 'dd',
    -1: 'd',
    1: 'A',
    2: 'dA',
    3: 'tA',
    4: 'qA'
}

def count_interval(n1: Note, n2: Note) -> str:
    res = ''
    mi = ref.index(n2.base) - ref.index(n1.base)
    if mi < 0:
        mi += 7
    mi += 1
    res = str(mi)
    ms = n2.semic - n1.semic
    # print(mi, ms)
    if mi in [1, 4, 5]:
        res = ('P' if ms == 0 else q_list_P[ms]) + res
    if mi in [2, 3, 6, 7]:
        ti = rei[n2.base] - rei[n1.base]
        ti += 0 if ti >= 0 else 12
        ri = mi * 2 - (2 if mi < 5 else 3)
        if ri == ti:
            if ms == 0:
                res = 'M' + res
            elif ms == -1:
                res = 'm' + res
            else:
                res = q_list_P[ms + (0 if ms > 0 else 1)] + res
        if ri == ti + 1:
            if ms == 0:
                res = 'm' + res
            elif ms == 1:
                res = 'M' + res
            else:
                res = q_list_P[ms + (-1 if ms > 0 else 0)] + res
    # print(n1, n2)
    return res

if __name__ == '__main__':
    print(count_interval(Note('B#'), Note('Cb')))