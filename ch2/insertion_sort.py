#!/usr/bin/python3
# -*- coding: utf8 -*-
from pprint import pprint
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        while j > -1 and arr[j] > pivot:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot

    return arr


if __name__ == "__main__":
    random.seed(42)
    arr = list(range(10))
    random.shuffle(arr)
    pprint(arr)
    insertion_sort(arr)
    pprint(arr)
