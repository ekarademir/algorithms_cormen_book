#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import seed, shuffle


def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    new_arr = insertion_sort(arr[:-1])
    for i, x in enumerate(new_arr):
        if x > pivot:
            return new_arr[:i] + [pivot] + new_arr[i:]
    return new_arr + [pivot]


if __name__ == "__main__":
    seed(42)
    arr = list(range(10))
    shuffle(arr)
    print(arr)
    print(insertion_sort(arr))
