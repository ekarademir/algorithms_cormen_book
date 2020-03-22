#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import inf
from random import seed, shuffle


def merge(left, right):
    left = iter(left + [inf])
    right = iter(right + [inf])
    next_left, next_right = next(left), next(right)

    while next_left != inf or next_right != inf:
        if next_left < next_right:
            yield next_left
            next_left = next(left)
        else:
            yield next_right
            next_right = next(right)


def merge_sort(arr):
    l = len(arr)
    if l < 2:
        return arr
    mid = l // 2
    left = arr[:mid]
    right = arr[mid:]
    return list(merge(merge_sort(left), merge_sort(right)))


if __name__ == "__main__":
    seed(42)
    arr = list(range(10))
    shuffle(arr)
    print(arr)
    print(merge_sort(arr))
