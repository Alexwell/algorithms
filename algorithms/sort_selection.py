def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    i = 1

    while  i < len(arr):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        i += 1
    return smallest_index

def sort_selection(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
