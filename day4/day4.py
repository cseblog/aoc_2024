import fileinput
import re
import copy


class Day4:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.keys = ['X', 'M', 'A', 'S']
        self.patterns = ["XMAS", "SAMX", 'X.*MAS', 'XM.*AS', 'XMA.*S', 'S.*AMX', 'SA.*MX', 'SAM.*X', 'X.*M.*A.*S', 'S.*A.*M.*X']
        self.data = []
        self.lines = []
        self.cols = []
        self.diagonals = []

    @staticmethod
    def find_all_concatenations(keys):
        all_concatenations = []

        def backtrack(current, remaining):
            if not remaining:
                all_concatenations.append(current)
            else:
                for i in range(len(remaining)):
                    backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])

        backtrack('', keys)
        return all_concatenations

    def process1(self):
        for line in fileinput.input(files=self.config_file, encoding="utf-8"):
            self.data.append(line.rstrip())
            self.lines.append(line.rstrip())

        self.get_cols()
        self.get_right_diagnal()
        self.get_left_diagnal()

    def get_cols(self):
        for i in range(len(self.data)):
            col = []
            for j in range(len(self.data[i])):
                col.append((self.data[j][i]))
            st = "".join(col)
            self.cols.append(st)

    def get_right_diagnal(self):
        for i in range(len(self.data)):
            col = []
            j = 0
            while (j + i) < len(self.data):
                col.append(self.data[j][j + i])
                j = j + 1
            self.diagonals.append("".join(col))

    def get_left_diagnal(self):
        for i in range(len(self.data)):
            col = []
            j = len(self.data) - 1
            while (j - i) >= 0:
                col.append(self.data[j][j - i])
                j = j - 1
            self.diagonals.append("".join(col))

    def count(self, lines, patterns):
        t1 = 0
        for line in lines:
            mx = 0
            for p in patterns:
                matches = re.findall(p, line)
                if matches:
                    if(len(matches) > mx):
                        mx = len(matches)
            t1 = t1 + mx
        return t1

    def find_word_1(self):
        cnt = 0
        cnt = cnt + self.count(self.lines, self.patterns)
        print(cnt)
        print("ddxxxd")

        cnt = cnt + self.count(self.cols, self.patterns)
        print(cnt)
        print("dddxxxx")
        cnt = cnt + self.count(self.diagonals, self.patterns)
        print(cnt)
        return cnt
