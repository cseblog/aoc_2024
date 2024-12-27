import fileinput
from ctypes.wintypes import tagMSG
from copy import copy, deepcopy

class Day7:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.data_map = []


    def process(self):
        for line in fileinput.input(files=self.config_file, encoding="utf-8"):
            line = line.rstrip()
            arr = line.split(": ")
            key = int(arr[0])
            v_array = arr[1].rstrip().split(" ")
            values = [int(i) for i in v_array]
            self.data_map.append({'k': key, 'values': values})

        print(self.data_map)

    def exec(self, total, val, op):
        if op == '*':
            return total * val
        if op == '+':
            return total + val

    def is_valid(self, k, values, ops):
        if len(values) == 1:
            if k == values[0]:
                return True
            else:
                return False


        total = self.exec(values[0],  values[1], ops[0])
        if len(values) == 2:
            if total == k:
                return True
            else:
                return False

        for i in range(2, len(values)):
            total = self.exec(total, values[i], ops[i-1])
        # print(total, " ,", k, ", ", values, ", ", ops)

        # if total >= k and total < (k + 10000):
        #     # print("total:", total, ops)
        #     st = []
        #     for i in range(0, len(values)):
        #
        #         # st.append(str(values[i]))
        #         # st.append(")")
        #
        #         if i < (len(values) - 1):
        #             st.append( ops[i])




        if total == k:
            return True
        else:
            return False

    def get_equation(self, k, values):
        if len(values) == 1:
            if k == values[0]:
                print("valid: ", k, values)
                return k
            else:
                return 0

        if len(values) == 2:
            if k == values[0] + values[1] or k == values[0] * values[1]:
                print("valid: ", k, values)
                return k
            else:
                return 0

        op_matrix = self.generate_operator_maxtr(len(values)- 1)
        for ops in op_matrix:
            if self.is_valid(k, values, ops):
                print("valid: ", k, values, ops)
                return k
        return 0


    def get(self, arr):
        new_arr = []
        for x in ['*', '+']:
            for i in range(len(arr)):
                a = deepcopy(arr[i])
                a.append(x)
                new_arr.append(a)
        return new_arr

    def generate(self, k, arr):
        while k >= 1:
            arr = self.get(arr)
            k = k - 1
        return  arr


    def generate_operator_maxtr(self, n):
        arr = [['*', '*'], ['*', '+'], ['+', '*'], ['+', '+']]
        if n == 1:
            return [['*'], ['+']]
        if n == 2:
            return arr

        # n > 2
        k = n - 2
        arr = self.generate(k, arr)
        # print(arr)
        return arr

    def part_11(self):
        self.process()
        keys = self.part_1(False)
        data = []
        for line in fileinput.input(files=self.config_file, encoding="utf-8"):
            line = line.rstrip()
            data.append(line)

        equations = []
        for line in data:
            test_value, numbers = line.split(":")
            equations.append((int(test_value), [*map(int, numbers.strip().split())]))

        result = []

        for test_value, numbers in equations:
            possibles = [numbers.pop(0)]
            while numbers:
                curr = numbers.pop(0)
                temp = []
                for p in possibles:
                    temp.append(p + curr)
                    temp.append(p * curr)
                possibles = temp

            if test_value in possibles:
                result.append(test_value)


        for r in result:
            if not r in keys:
                print('missing', r)
        return sum(result)


    def part_1(self, is_print):
        s = 0
        s2 = 0
        keys = set([])
        for k in self.data_map:
            key = k["k"]
            values = k["values"]

            t = self.get_equation(key, values)
            s2 = s2 + t
            if t > 0:
                keys.add(t)

        # Cater for duplicated keys
        for d in self.data_map:
            k = d["k"]
            if k in keys:
                s = s + k
        return sum(keys)




