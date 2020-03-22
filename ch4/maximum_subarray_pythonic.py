# -*- coding: utf-8 -*-
from random import seed, randint
from math import inf


def find_crossing_subarray(arr):
    mid = len(arr) // 2
    left_sum = right_sum = -inf
    low = high = 0

    total = 0
    for i, x in enumerate(reversed(arr[:mid])):
        total += x
        if total > left_sum:
            left_sum = total
            low = i

    total = 0
    for j, x in enumerate(arr[mid:]):
        total += x
        if total > right_sum:
            right_sum = total
            high = j

    return arr[mid - low - 1: mid + high + 1], left_sum + right_sum


def find_max_subarray(arr):
    if len(arr) == 1:
        return arr, arr[0]

    mid = len(arr) // 2
    left_arr, left_sum = find_max_subarray(arr[:mid])
    right_arr, right_sum = find_max_subarray(arr[mid:])
    crossing_arr, crossing_sum = find_crossing_subarray(arr)

    if left_sum > right_sum and left_sum > crossing_sum:
        return left_arr, left_sum
    if right_sum> left_sum and right_sum > crossing_sum:
        return right_arr, right_sum
    else:
        return crossing_arr, crossing_sum


if __name__ == "__main__":
    seed(45)
    arr = [14, -6, 10, 11, 1, 3, -10, -3, 1, -4]# [randint(-20, 20) for _ in range(10)]
    print(arr)
    # print(find_crossing_subarray(arr))
    print(find_max_subarray(arr))
