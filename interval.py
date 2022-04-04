from note import Note
from formatexception import IntervalFormatException

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
P_list = {
    1: 0,
    4: 5,
    5: 7
}
q_list_P = {
    -5: 'pd',
    -4: 'qd',
    -3: 'td',
    -2: 'dd',
    -1: 'd',
    1: 'A',
    2: 'dA',
    3: 'tA',
    4: 'qA',
    5: 'pA'
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
        ti = rei[n2.base] - rei[n1.base]
        ti += 0 if ti >= 0 else 12
        # print(ti)
        if P_list[mi] == (ti + ms) % 12:
            res = 'P' + res
        else:
            temp = (ti + ms) % 12 - P_list[mi]
            if temp > 5:
                temp -= 12
            res = q_list_P[temp] + res
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

def note_from_interval(n1: Note, interval: str) -> Note:
    res_note = 'C'
    try:
        p = 0
        q = ''
        while interval[p] not in '0123456789':
            q = q + interval[p]
            p += 1
        mi = int(interval[p:])
    except:
        raise IntervalFormatException
    mi = (mi % 7) if mi > 7 else mi
    # print(q, mi)
    new_n = (ref.index(n1.base) + mi - 1) % 7
    res_note = ref[new_n]
    qi = 0
    if q == 'P':
        if mi not in [1, 4, 5]:
            raise IntervalFormatException
    elif q in ['M', 'm']:
        if mi not in [2, 3, 6, 7]:
            raise IntervalFormatException
    else:
        for k, v in q_list_P.items():
            if q == v:
                qi = k
                break
        else:
            raise IntervalFormatException
    ms = rei[res_note] - rei[n1.base]
    ms += 0 if ms >= 0 else 12
    if mi in [1, 4, 5]:
        ti = P_list[mi]
        f = ti - ms + qi + n1.semic
    else:
        ti = mi * 2 - (2 if mi < 5 else 3)
        f = ti - ms + qi + n1.semic
        if ti - ms != 0:
            f -= 1
    # print(mi, ms, qi, ti)
    s = 'b' if f < 0 else '#'
    for i in range(abs(f)):
        res_note = res_note + s
    return Note(res_note)

if __name__ == '__main__':
    print(count_interval(Note('Bb'), Note('F#')))
    print(note_from_interval(Note('D'), 'M3'))