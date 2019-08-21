import numpy as np

def expanding(lst):
    size = len(lst)
    res = False
    diff, max = 0, 0
    if size <= 1:
        return False
    else:
        for i in range(1, size):
            diff = abs(lst[i - 1] - lst[i])
            if diff > max:
                (max, res) = (diff, True)
            else:
                res = False
    return res


print(expanding([1, 3, 7, 2, 9]))


def is_accordain_dec(lst):
    size = len(lst)
    diff, max, res = 0, 0, False
    for i in range(1, size):
        diff = abs(lst[i - 1] - lst[i])
        if i % 2 != 0:
            if diff > max:
                max, res = diff, True
            else:
                return False
        else:
            if diff < max:
                max, res = diff, True
            else:
                return False
    return res


def is_accordain_inc(lst):
    size = len(lst)
    diff, max, res = 0, 0, False
    for i in range(1, size):
        diff = abs(lst[i - 1] - lst[i])
        if i % 2 != 0:
            if diff < max:
                max, res = diff, True
            else:
                return False
        else:
            if diff > max:
                max, res = diff, True
            else:
                return False
    return res


def accordian(lst):
    diff = 0
    abs_lst = []
    res = False
    for i in range(1, len(lst)):
        diff = abs(lst[i - 1] - lst[i])
        abs_lst.append(diff)
    for i in range(0, len(abs_lst) - 2):
        if abs_lst[i] < abs_lst[i + 1] and abs_lst[i + 1] > abs_lst[i + 2]:
            res = True
        elif abs_lst[i] > abs_lst[i + 1] and abs_lst[i + 1] < abs_lst[i + 2]:
            res = True
        else:
            return False
    if res:
        return True
    else:
        return False


print(accordian([-2, 1, 5, 2, 8, 3, ]))


def rotate(arr):
    res = np.rot90(arr, -1)
    return res


print(rotate([[1, 2], [3, 4]]))
