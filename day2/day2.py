import fileinput

def main():
    print("Hellow day 2")
    count = 0
    for line in fileinput.input(files=('day2.txt'), encoding="utf-8"):
        inputs = line.split(" ")
        int_arr = [int(num) for num in inputs]
        in1 = int_arr.copy()
        res2 = part22(in1)
        if res2:
            count = count + 1
    print(count)


def part22(int_arr):
    res = valTrend(int_arr)
    if res:
        res = gap_test(int_arr)
        if res:
            return True
        else:
            for i in range(len(int_arr)):
                a = int_arr.copy()
                del a[i]
                r2 = gap_test(a)
                if r2:
                    return True
    else:
        for i in range(len(int_arr)):
            a = int_arr.copy()
            del a[i]
            r = valTrend(a)
            if r:
                r2 = gap_test(a)
                if r2:
                    return True
    return False

    # Part 2

    # count2 = 0
    # for line in fileinput.input(files=('day2.txt'), encoding="utf-8"):
    #     inputs = line.split(" ")
    #     int_arr = [int(num) for num in inputs]
    #     res = desc_val_trend2(int_arr)
    #     if res:
    #         count2 = count2 + 1
    #
    #     # res = inc_val_trend2(int_arr)
    #     # if res:
    #     #     count2 = count2 + 1
    #
    #
    # print(count2)


def part2(levels):
    safe = 0
    if is_safe(levels):
        return True
    else:
        for i in range(len(levels)):
            tolerated_levels = levels[:i] + levels[i + 1:]
            if is_safe(tolerated_levels):
                return True
    return False


def is_safe(levels):
    differs = [a - b for a, b in zip(levels, levels[1:])]
    is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    is_in_range = all(0 < abs(i) <= 3 for i in differs)
    if is_monotonic and is_in_range:
        return True
    return False


def inc_val_trend2(orginArry):
    is_increase = True
    inc_count = 0
    inc_last_index = -1
    prev = orginArry[0]
    for i in range(1, len(orginArry)):
        if orginArry[i] < prev:
            is_increase = False
            inc_count = inc_count + 1
            inc_last_index = i
        prev = orginArry[i]
    if not is_increase:
        if inc_count > 1:
            return False
        if inc_count == 1:
            arr1 = orginArry.copy()
            del arr1[inc_last_index]
            test1 = gap_test(arr1)
            if test1:
                return True
            else:
                arr1 = orginArry.copy()
                del arr1[inc_last_index - 1]
                test2 = gap_test(arr1)
                if test2:
                    return True
                else:
                    return False
    if is_increase:
        res = gap_test2(orginArry)
        if res:
            return True
        else:
            return False


def desc_val_trend2(orgin_array):
    is_desc = True
    desc_count = 0
    last_desc_index = -1
    prev = orgin_array[0]
    for i in range(1, len(orgin_array)):
        if orgin_array[i] > prev:
            is_desc = False
            desc_count = desc_count + 1
            last_desc_index = i
        prev = orgin_array[i]

    if not is_desc:
        if desc_count > 1:
            return False
        if desc_count == 1:
            arr1 = orgin_array.copy()
            del arr1[last_desc_index]
            test1 = gap_test(arr1)
            if test1:
                return True
            else:
                arr1 = orgin_array.copy()
                del arr1[last_desc_index - 1]
                test2 = gap_test(arr1)
                if test2:
                    return True
                else:
                    return False

    if is_desc:
        res = gap_test2(orgin_array)
        if res:
            return True
        else:
            return False


def gap_test2(inputs):
    prev = inputs[0]
    count = 0
    last_index = -1
    prev_index = -1
    for i in range(1, len(inputs)):
        if abs(inputs[i] - prev) > 3 or abs(inputs[i] - prev) < 1:
            count = count + 1
            last_index = i
            prev_index = i - 1
        prev = inputs[i]

    if count == 0:
        return True
    if count > 1:
        return False
    if count == 1:
        arr1 = inputs.copy()
        del arr1[last_index]
        test = gap_test(arr1)
        if test:
            return True
        else:
            arr1 = inputs.copy()
            del arr1[prev_index]
            return gap_test(arr1)


def valTrend(int_arr):
    asc_arr = int_arr.copy()
    asc_arr.sort()
    desc_arr = int_arr.copy()
    desc_arr.sort(reverse=True)
    is_asc = True
    is_desc = True
    for i in range(len(int_arr)):
        if int_arr[i] != asc_arr[i]:
            is_asc = False
        if int_arr[i] != desc_arr[i]:
            is_desc = False
    return is_asc or is_desc


def gap_test(inputs):
    prev = inputs[0]
    for i in range(1, len(inputs)):
        if abs(inputs[i] - prev) > 3 or abs(inputs[i] - prev) < 1:
            return False
        prev = inputs[i]
    return True


# executive the main
# Solution: Very straight forward solution for part 2:
# Count all the case of part 1, then brute force remote one element of the array input and re-run part 1 again...
main()
