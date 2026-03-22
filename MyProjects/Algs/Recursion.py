def recursive_sum(arr: list):
    if recursive_len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

def recursive_len(arr: list):
    if arr != []:
        return 1 + recursive_len(arr[1:])
    else:
        return 0
    
print(recursive_sum([1,2,3,4,]))