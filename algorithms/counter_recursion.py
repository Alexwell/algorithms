def counter_recursion(list):
    try:
        list.pop()
    except: return 0
    return 1 + counter_recursion(list)
