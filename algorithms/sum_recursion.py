def sum_recursion(arr):
    if len(arr) == 0: return 0
    elif len(arr) == 1: return arr[0]

    return arr.pop(0) + sum_recursion(arr)
