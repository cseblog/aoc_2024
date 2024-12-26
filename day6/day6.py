import fileinput
import os
from time import sleep

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
            data[self.i][self.j] = 'X'
            self.j = l
            data[self.i][self.j] = '<'
            return True
        return False

    def is_able_right(self, data):
        r = self.j + 1
        if r < len(data[0]) and data[self.i][r] != '#':
            data[self.i][self.j] = "X"
            self.j = r
            data[self.i][self.j] = ">"
            return True
        return False

    def is_able_up(self, data):
        u = self.i - 1
        if u >= 0 and data[u][self.j] != '#':
            data[self.i][self.j] = 'X'
            self.i = u
            data[self.i][self.j] = '^'
            return True
        return False

    def is_able_down(self, data):
        d = self.i + 1
        if d < len(data[0]) and data[d][self.j] != '#':
            data[self.i][self.j] = 'X'
            self.i = d
            data[self.i][self.j] = 'v'
            return True
        return False

    def is_final(self, data):
        d = self.i + 1
        if self.direction == 'v' and d == len(data[0]):
            return True
        return False


    def clear(self):
        os.system('clear') #MacOS

    def print_grid(self, data):
        self.clear()
        for i in range(len(data)):
            print("".join(data[i]))

    def move(self, data):
        track = []
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

            track.append(self.i * len(data[0]) + self.j)
            sleep(0.05)
            self.print_grid(data)

        # print(set(track))
        return len(set(track))


class Day6:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.data = []
        self.actor = None

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

        print("data len ", len(self.data))


    def part_1(self):
        print("hello")
        return self.actor.move(self.data)

