from random import randint
import time, sys
sys.setrecursionlimit(1000000)

def fast_sort(arr: list) -> list:
    if len(arr) > 1:
        criteria = arr.pop(0)
        less = []
        more = []
        for i in arr:
            if i < criteria:
                less.append(i)
            else:
                more.append(i)
        return (fast_sort(less) + [criteria] + fast_sort(more))
    else:
        return arr

def slow_sort(arr: list) -> list:
    output = []
    while arr != []:
        minimal = float('inf')
        for i in arr:
            if i < minimal:
                minimal = i
        arr.remove(minimal)
        output.append(minimal)
    return output

sort_array = list([randint(-100, 100) for _ in range(100000)])

start = time.time()
fast_sort(sort_array)
print(format(((time.time() - start) * 1000), ".6f"), "мс")

start = time.time()
slow_sort(sort_array)
print(format(((time.time() - start) * 1000), ".6f"), "мс")