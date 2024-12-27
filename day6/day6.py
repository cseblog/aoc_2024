import fileinput
import os
from time import sleep
from collections import Counter

class Actor:
    def __init__(self, i, j, c):
        self.i = i
        self.j = j
        self.direction = c  # 1- UP, 2- Down, 3- Left, 4- Right

    def to_string(self):
        return "[" + str(self.i) + ", " + str(self.j) + "]" + str(self.direction)

    def is_able_left(self, data):
        l = self.j - 1
        if l >= 0 and data[self.i][l] != '#':
            data[self.i][self.j] = '.'
            self.j = l
            data[self.i][self.j] = '<'
            return True
        return False

    def is_able_right(self, data):
        r = self.j + 1
        if r < len(data[0]) and data[self.i][r] != '#':
            data[self.i][self.j] = "."
            self.j = r
            data[self.i][self.j] = ">"
            return True
        return False

    def is_able_up(self, data):
        u = self.i - 1
        if u >= 0 and data[u][self.j] != '#':
            data[self.i][self.j] = '.'
            self.i = u
            data[self.i][self.j] = '^'
            return True
        return False

    def is_able_down(self, data):
        d = self.i + 1
        if d < len(data) and data[d][self.j] != '#':
            data[self.i][self.j] = '.'
            self.i = d
            data[self.i][self.j] = 'v'
            return True
        return False

    def is_final(self, data):
        if self.direction == 'v' and (self.i + 1) == len(data):
            return True
        if self.direction == '^' and (self.i  - 1) < 0:
            return True
        if self.direction == '>' and (self.j + 1) == len(data[0]):
            return True
        if self.direction == '<' and (self.j - 1) < 0:
            return True
        return False


    def clear(self):
        os.system('clear') #MacOS

    def print_grid(self, data):
        sleep(0.1)
        self.clear()
        for i in range(len(data)):
            print("".join(data[i]))

    def move(self, data, is_print):
        track = set([self.i * len(data[0]) + self.j])
        while not self.is_final(data):
            match self.direction:
                case '^':  #UP
                    if not self.is_able_up(data):
                        self.direction = '>'
                        continue
                case 'v': #DOWN
                    if not self.is_able_down(data):
                        self.direction = '<' # left
                        continue
                case '<': #LEFT
                    if not self.is_able_left(data):
                        self.direction = '^' #UP
                        continue
                case '>': # RIGHT
                    if not self.is_able_right(data):
                        self.direction = 'v'
                        continue

            track.add(self.i * len(data[0]) + self.j)
            if is_print:
                self.print_grid(data)

        return len(track)

    def find_max_dup(self, track):
        values = track.values()
        return max(values)


    def is_loop(self, data, is_print):
        pos = self.i * len(data[0]) + self.j
        track = {pos:  1}
        while not self.is_final(data):
            match self.direction:
                case '^':
                    if not self.is_able_up(data):
                        self.direction = '>'
                        continue
                case 'v':
                    if not self.is_able_down(data):
                        self.direction = '<' # left
                        continue
                case '<':
                    if not self.is_able_left(data):
                        self.direction = '^' #UP
                        continue
                case '>':
                    if not self.is_able_right(data):
                        self.direction = 'v'
                        continue
            pos = self.i * len(data[0]) + self.j
            p = track.get(pos)
            if p is None:
                track[pos] = 1
            else:
                track[pos] = p + 1

            if is_print:
                self.print_grid(data)

            max_dup = self.find_max_dup(track)
            if max_dup > 4:
                data[self.i][self.j] = '.'
                return True # Found loop
            else:
                continue

        max_dup = self.find_max_dup(track)
        if max_dup > 4:
            data[self.i][self.j] = '.'
            return True

        data[self.i][self.j] = '.'
        return False

class Day6:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.data = []
        self.actor = None
        self.i = None
        self.j = None
        self.direction = None

    def get_actor(self, r, line, c):
        col = line.index(c)
        self.actor = Actor(r, col, c)

    def process(self):
        r = 0
        for line in fileinput.input(files=self.config_file, encoding="utf-8"):
            line = line.rstrip()
            if '^' in line:
                self.get_actor(r, line,  '^')
            elif '>' in line:
                self.get_actor(r, line,  '>')
            elif '<' in line:
                self.get_actor(r, line,  '<')
            elif 'v' in line:
                self.get_actor(r, line,  'v')
            self.data.append(list(line.rstrip()))
            r = r + 1

        self.i = self.actor.i
        self.j = self.actor.j
        self.direction = self.actor.direction

        print("Max row:", len(self.data))
        print("Max col:", len(self.data[0]))


    def part_1(self, is_print):
        return self.actor.move(self.data, is_print)

    def part_2(self, is_print):
        cnt = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                print("[",i,",",j,"]")
                if self.data[i][j] == '.':
                    self.data[i][j] = '#'
                    if self.actor.is_loop(self.data, is_print):
                        cnt = cnt + 1
                    # Reset before next check
                    self.data[i][j] = '.'
                    self.actor.i = self.i
                    self.actor.j = self.j
                    self.actor.direction = self.direction

        return cnt



