import fileinput
import locale
import re
import copy


class Day4:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.keys = ['X', 'M', 'A', 'S']
        self.patterns = ["XMAS", "SAMX"]
        self.data = []
        self.lines = []
        self.cols = []

        self.right_diagonals = []
        self.left_diagonals = []

        self.part2_data = []

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
            self.data.append(line.strip())
            self.lines.append(line.strip())

    def get_cols(self):
        for i in range(len(self.data)):
            col = []
            for j in range(len(self.data[i])):
                col.append((self.data[j][i]))
            st = "".join(col)
            self.cols.append(st)

    def get_right_diagonal(self):
        for i in range(len(self.data)):
            col = []
            j = 0
            while (j + i) < len(self.data):
                col.append(self.data[j][j + i])
                j = j + 1
            self.right_diagonals.append("".join(col))

        for i in range(1, len(self.data)):
            col = []
            for j in range(i, len(self.data)):
                col.append(self.data[j][j - i])
            self.right_diagonals.append("".join(col))

    def get_left_diagonal(self):
        for i in range(len(self.data)):
            col = []
            for j in range(i + 1):
                col.append(self.data[j][i - j])
            self.left_diagonals.append("".join(col))

        for i in range(1, len(self.data)):
            r = i
            col = []
            for j in range(len(self.data) - 1, i - 1, -1):
                col.append(self.data[r][j])
                r = r + 1
            self.left_diagonals.append("".join(col))

    def count(self, lines, patterns):
        t1 = 0
        for line in lines:
            mx = 0
            for p in patterns:
                matches = re.findall(p, line)
                if matches:
                    # print("line:", line, matches)
                    mx = mx + len(matches)
            t1 = t1 + mx
        return t1

    def find_part1(self):
        cnt = 0
        cnt = cnt + self.count(self.lines, self.patterns)
        print("lines cnt: %s", cnt)

        cnt = cnt + self.count(self.cols, self.patterns)
        print("rows + cols: cnt: %s", cnt)

        cnt = cnt + self.count(self.left_diagonals, self.patterns)
        print("rows + cols: left_diagonals: %s", cnt)

        cnt = cnt + self.count(self.right_diagonals, self.patterns)
        print("rows + cols: right_diagonals: %s", cnt)
        return cnt

    def find_part2(self):
        for i in range(0, len(self.data) - 2, 1):
            for x in range(0, len(self.data) - 2, 1):
                mt = []
                for j in range(i, i + 3):
                    for k in range(x, x + 3):
                        mt.append(self.data[j][k])
                self.part2_data.append("".join(mt))

        print(self.part2_data)

        p2_pattern = ["M.S.A.M.S", "M.M.A.S.S", "S.S.A.M.M", "S.M.A.S.M"]

        count = 0
        for line in self.part2_data:
            for p in p2_pattern:
                matches = re.findall(p, line)
                if matches:
                    print("p", p, "line ", line)
                    count = count + 1

        print(count)
