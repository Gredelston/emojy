#!/usr/bin/python

from translations import translation

class Emojy():
    def __init__(self, pyinput, size=30000):
        self.size = size
        self.pyinput = pyinput
        if self.pyinput:
            self.input_cache = []
    def readchar(self):
        if self.pyinput:
            while len(self.input_cache) == 0:
                self.input_cache = list(str(input()))
            p = self.input_cache.pop(0)
            return p
        else:
            import readchar
            return readchar.readchar()
    def execute(self, code):
        commands = [translation[char] for char in code if char in translation]

        code = commands
        bracemap = self.buildbracemap(code)

        cells, codeptr, cellptr = [0]*self.size, 0, 0

        while codeptr < len(code):
            command = code[codeptr]

            if command == ">":
                cellptr += 1

            if command == "<":
                cellptr = 0 if cellptr <= 0 else cellptr - 1

            if command == "+":
                cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

            if command == "-":
                cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

            if command == "[" and cells[cellptr] == 0:
                codeptr = bracemap[codeptr]
            if command == "]" and cells[cellptr] != 0:
                codeptr = bracemap[codeptr]
            if command == ".":
                print(chr(cells[cellptr]), end="")
            if command == ",":
                cells[cellptr] = ord(self.readchar())
                
            codeptr += 1


    def buildbracemap(self, code):
        temp_bracestack, bracemap = [], {}

        for position, command in enumerate(code):
            if command == "[": temp_bracestack.append(position)
            if command == "]":
                start = temp_bracestack.pop()
                bracemap[start] = position
                bracemap[position] = start
        return bracemap


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Emojy interpreter')
    parser.add_argument('files', metavar='file', type=str, default=["-"],
                       nargs='*', help='the path to the emojy code file, default is "-" for stdin')
    parser.add_argument('--pyinput', dest="pyinput", help='use pythons input function instead of readchar', action='store_true')
    args = parser.parse_args()

    for file in args.files:
        if file == "-":
            emfile = sys.stdin
        else:
            emfile = open(file)

        emojy = Emojy(args.pyinput)
        emojy.execute(emfile.read())


        emfile.close()