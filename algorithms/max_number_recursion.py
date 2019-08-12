def max_number_recursion(list):
    if len(list) == 2:
        if list[0] > list[1]: return list[0]
        else: return list[1]
    a = list.pop(0)
    tmp_max = max_number_recursion(list)
    if a > tmp_max: return a
    else: return tmp_max
