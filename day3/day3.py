import fileinput
import re



def main():
    print("Hellow day 1")
    txt = open("day3.txt").read()
    t = part1(txt)
    print(t)
    pattern = r'do\(\)(.*?)don\'t\(\)'
    t = part2(txt, pattern)
    t = t + start(txt)
    print(t)

def start(txt):
    # start
    total = 0
    arr = txt.split('don\'t()')
    last = arr[len(arr) - 1]
    first = arr[0]
    pattern4 = r'do\(\).*$'
    pattern5 = r'^.*do\(\)'
    total = total + (part2(last, pattern4))
    total = total + (part2(first,pattern5))
    return total


def part2(txt, pattern):
    # print(txt)
    total = 0
    x = re.findall(pattern, txt)
    for l in x:
        print(l)
        v = part1(l)
        total = total + v
    return total


def part1(line):
    total = 0
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    if x:
        for xx in x:
            val = process(xx)
            total = total + val
    # print(total)
    return total


def process(x):
    # t = re.findall("[0-9]{1,3},[0-9]{1,3}", x)
    # nums = t[0].split(",")
    # num_arr = [int(num) for num in nums]
    # # print(num_arr)
    # return num_arr[0] * num_arr[1]
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, "".join(x))

    result = sum(int(x) * int(y) for x, y in matches)

    return result

#166357705
#81008407
#66317524
#89135798
#88811886

# Learnt lesson: The regrex is not applied to multiple lines
# We need to remove \n characters before we want to grep a pattern crossing lines
# Solution: One of the way to solve by remove all text 'don't()()...don't() and don't()...do()
# Using the result txt and re-run part1
# main()

