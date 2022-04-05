from note import Note
from interval import note_from_interval
from formatexception import *

ref = 'CDEFGAB'

chord_dict = {
    ('M', '', 'maj'): ['P1', 'M3', 'P5'],
    ('m', 'min'): ['P1', 'm3', 'P5'],
    ('M7', 'maj7'): ['P1', 'M3', 'P5', 'M7'],
    ('m7', 'min7'): ['P1', 'm3', 'P5', 'm7'],
    ('7', 'dom7'): ['P1', 'M3', 'P5', 'm7'],
    ('mM7', ): ['P1', 'm3', 'P5', 'M7'],
    ('m7b5', ): ['P1', 'm3', 'd5', 'm7'],
}

def makeChord(chord_name: str) -> list():
    if chord_name[0] not in ref:
        raise ChordFormatException
    root = chord_name[0]
    p = 1
    while p < len(chord_name):
        if chord_name[p] in ['#', 'b']:
            root = root + chord_name[p]
        else:
            break
        p += 1
    status = chord_name[p:]
    print(root, status)
    root_note = Note(root)
    res = []
    for k, v in chord_dict.items():
        if status in k:
            for interval in v:
                res.append(note_from_interval(root_note, interval))
    return res

if __name__ == '__main__':
    print(makeChord('C'))
    print(makeChord('D#mM7'))
    print(makeChord('Bb7'))