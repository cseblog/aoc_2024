import fileinput
def main():
    print("Hellow day 1")
    a = []
    b = []
    dist = []
    for line in fileinput.input(files=('day1.txt'), encoding="utf-8"):
        inputs = line.split("   ")
        a.append(int(inputs[0]))
        b.append(int(inputs[1]))
    a.sort()
    b.sort()

    for i in range(len(a)):
        dist.append(abs(a[i] - b[i]))

    total = sum(dist)
    print(total)

    #Part 2
    factor = []
    for i in range(len(a)):
        count = 0
        for j in range(len(b)):
            if a[i] < b[j]:
                continue

            if b[j] > a[i]:
                break
            if a[i] == b[j]:
                count = count + 1
        factor.append(a[i] * count)

    total2 = sum(factor)
    print(total2)


# executive the main
main()