#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import inf
from random import shuffle, seed
from pprint import pprint


def merge(left, right):
    left += [inf]
    right += [inf]
    i = j = 0
    res = []
    for _ in range(len(left) + len(right) - 2):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == "__main__":
    seed(42)
    arr = list(range(10))
    shuffle(arr)
    pprint(arr)
    pprint(merge_sort(arr))
