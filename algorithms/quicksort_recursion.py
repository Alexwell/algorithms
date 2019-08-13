def quicksort_recursion(array):
    if len(array) < 2:
        return array

    else:
        pivot = array.pop(0)
        less = []
        greater = []
        i = 0
        while i < len(array):
            if array[i] <= pivot:
                less.append(array[i])
            else:
                greater.append(array[i])
            i += 1

        return quicksort_recursion(less) + [pivot] + \
                quicksort_recursion(greater)
