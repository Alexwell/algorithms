import random


def generate_array(my_len, max_rand_coeff=100):
    arr = []
    while len(arr) < my_len:
        arr.append(random.randint(0, my_len * max_rand_coeff))

    return arr
