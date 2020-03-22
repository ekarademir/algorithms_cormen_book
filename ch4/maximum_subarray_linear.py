# -*- coding: utf-8 -*-
from math import inf
from random import seed, randint


def find_max_subarray(arr):
    low = high = 0
    max_total = -inf
    total = -inf
    left = 0
    for right, x in enumerate(arr):
        if total > 0:
            total += x
        else:
            left = right
            total = x

        if total > max_total:
            max_total = total
            low = left
            high = right


    return arr[low:high + 1]





if __name__ == "__main__":
    seed(45)
    arr = [randint(-20, 20) for _ in range(10)]
    print(arr)
    print(find_max_subarray(arr))
