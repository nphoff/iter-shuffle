#!/usr/bin/env python

import random

def iterative_shuffle(arr=[]):
    if arr == []:
        arr = range(3)
    for i in range(0, len(arr)):
        r = random.randrange(0, len(arr))
        temp = arr[i]
        arr[i] = arr[r]
        arr[r] = temp
    return arr

def repeat_and_keep_track(n=10, array_to_be_shuffled=[]):
    results = {}
    for i in range(n):
        arr = str(iterative_shuffle(array_to_be_shuffled))
        if arr in results:
            results[arr] += 1
        else:
            results[arr] = 1
    return results

if __name__ == '__main__':
    a = repeat_and_keep_track(100000)
    print(a)
        
