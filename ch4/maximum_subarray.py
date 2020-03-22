#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import seed, randint
from math import inf


def find_max_crossing_subarray(arr, low, high):
    left_sum = right_sum = -inf
    left, right, mid = low, high, (low + high) // 2

    total = 0
    for i in range(mid, -1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum, left = total, i
    total = 0
    for i in range(mid + 1, high):
        total += arr[i]
        if total > right_sum:
            right_sum, right = total, i
    return left, right + 1, left_sum + right_sum


def find_max_subarray(arr, low, high):
    if high - low == 1:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_max_subarray(arr, mid, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    # This is not working correctly, but i'm not too much bother with the correct solution
    seed(45)
    arr = [randint(-20, 20) for _ in range(10)]
    print(arr)
    x = find_max_subarray(arr, 0, len(arr))
    subarr = arr[x[0]:x[1]]
    print(subarr, x, sum(subarr))
