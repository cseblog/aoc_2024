import fileinput
import locale
import re
import copy


class Day5:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.forward_rules = {}
        self.backward_rules = {}
        self.page_updates = []

    def process(self):
        is_first_part = True
        for line in fileinput.input(files=self.config_file, encoding="utf-8"):
            if line == "\n":
                is_first_part = False
                continue

            if is_first_part:
                arr = line.rstrip().split("|")
                k = int(arr[0])
                v = int(arr[1])

                if k in self.forward_rules.keys():
                    self.forward_rules[k].append(v)
                else:
                    self.forward_rules[k] = [v]

                if v in self.backward_rules.keys():
                    self.backward_rules[v].append(k)
                else:
                    self.backward_rules[v] = [k]
                continue

            if not is_first_part:
                pages = [int(num) for num in line.split(",")]
                self.page_updates.append(pages)

        print(self.forward_rules)
        print(self.page_updates)

    def part1(self):
        total = 0
        for u in self.page_updates:
            if self.is_valid(u):
                middle = int(len(u) / 2)
                total = total + u[middle]
        return total

    def is_valid(self, u):
        is_good = True
        for i in range(len(u)):
            rules = self.forward_rules.get(u[i])
            backward_rules = self.backward_rules.get(u[i])
            for j in range(i + 1, len(u)):
                if rules is None:
                    if u[j] in backward_rules:
                        is_good = False
                    else:
                        continue
                else:
                    if not u[j] in rules:
                        is_good = False
        return is_good

    def part2(self):
        total = 0
        for u in self.page_updates:
            is_good = True
            for i in range(len(u)):
                rules = self.forward_rules.get(u[i])
                backward_rules = self.backward_rules.get(u[i])
                for j in range(i + 1, len(u)):
                    if rules is None:
                        if u[j] in backward_rules:
                            is_good = False
                        else:
                            continue
                    else:
                        if not u[j] in rules:
                            is_good = False

            if not is_good:
                total = total + self.correct(u)
        return total

    def correct(self, u):
        while not self.is_valid(u):  # try to correct until the array is valid
            for i in range(len(u)):
                rules = self.forward_rules.get(u[i])
                backward_rules = self.backward_rules.get(u[i])
                for j in range(i + 1, len(u)):
                    if rules is None:
                        if u[j] in backward_rules:
                            tmp = u[i]
                            u[i] = u[j]
                            u[j] = tmp
                        else:
                            continue
                    else:
                        if not u[j] in rules:
                            tmp = u[i]
                            u[i] = u[j]
                            u[j] = tmp

        middle = int(len(u) / 2)
        return u[middle]
