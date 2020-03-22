#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import seed, shuffle


def insert(arr, val):
    if len(arr) == 1:
        if arr[0] < val:
            return arr + [val]
        else:
            return [val] + arr

    mid = len(arr) // 2
    if arr[mid] > val:
        return insert(arr[:mid], val) + arr[mid:]
    elif arr[mid] < val:
        return arr[:mid] + insert(arr[mid:], val)
    else:
        return arr[:mid] + [val] + arr[mid:]


def insertion_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[-1]
    new_arr = insertion_sort(arr[:-1])
    return insert(new_arr, pivot)


if __name__ == "__main__":
    seed(42)
    arr = list(range(10))
    shuffle(arr)
    print(arr)
    print(insertion_sort(arr))
