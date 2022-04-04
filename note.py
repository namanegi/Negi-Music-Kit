from formatexception import NoteFormatException
ref = 'CDEFGAB'

class Note:
    def __init__(self, name: str) -> None:
        temp = []
        self.base = ''
        self.semic = 0
        self.semis = ''
        self.oct = -1
        if name == '':
            raise NoteFormatException
        for c in name:
            temp.append(c)
        if temp[0] in ref:
            self.base = temp.pop(0)
        else:
            raise NoteFormatException
        if temp != [] and temp[-1] in '0123456789':
            self.oct = int(temp.pop(-1))
        while temp != []:
            if temp[0] in 'b#':
                cur = temp.pop(0)
                self.semis = self.semis + cur
                self.semic += (1 if cur == '#' else -1)
            else:
                raise NoteFormatException
        
    def __repr__(self) -> str:
        return self.base + self.semis + (str(self.oct) if self.oct >= 0 else '')

    def __str__(self) -> str:
        return self.base + self.semis + (str(self.oct) if self.oct >= 0 else '')

if __name__ == '__main__':
    test_note1 = Note('C')
    test_note2 = Note('B#')
    print(test_note2.semic)
    print(test_note1, test_note2)