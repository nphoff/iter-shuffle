#!/usr/bin/env python

import random
import pprint

def iterative_shuffle(arr=[]):
    if arr == []:
        arr = range(3)
    path_to = []
    for i in range(0, len(arr)):
        r = random.randrange(0, len(arr))
        path_to.append(r)
        temp = arr[i]
        arr[i] = arr[r]
        arr[r] = temp
    return arr, path_to

def repeat_and_keep_track(n=10, array_to_be_shuffled=[]):
    results = {}
    for i in range(n):
        arr, path_to = iterative_shuffle(array_to_be_shuffled)
        arr = str(arr)
        path_to = str(path_to)
        if arr in results:
            results[arr]['count'] += 1
            if path_to not in results[arr]['paths_to']:
                results[arr]['paths_to'].append(path_to)
        else:
            results[arr] = {}
            results[arr]['count'] = 1
            results[arr]['paths_to'] = [path_to]
    for arr in results:
        results[arr]['total_paths_to'] = len(results[arr]['paths_to'])

    return results

if __name__ == '__main__':
    a = repeat_and_keep_track(10000)
    pprint.pprint(a)
        
