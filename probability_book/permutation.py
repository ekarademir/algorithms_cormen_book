#!/usr/bin/python3
from pprint import pprint


def permutations(arr):
    _permutations = []
    def permute(arr, head):
        if len(arr) == 1:
            _permutations.append(head + arr)

        for i in range(len(arr)):
            permute(arr[:i] + arr[i + 1:], head + [arr[i]])
    permute(arr, [])
    return _permutations


if __name__ == "__main__":
    pprint(permutations(list(range(5))))
