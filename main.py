from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection
from algorithms.sum_recursion import sum_recursion
from algorithms.counter_recursion import counter_recursion
from algorithms.max_number_recursion import max_number_recursion

def main():
    # b = None
    # counter = 0
    # while not b:
    #     tmp_arr = generate_array(555, max_rand_coeff=10)
    #     b = binary_search(tmp_arr, 5484)
    #     counter += 1
    #     print(counter)
    # print(f'index ==> {b}')

    # tmp_arr = generate_array(10, max_rand_coeff=10)
    # print(tmp_arr)
    # s = find_smallest(tmp_arr)
    # print(s)
    #
    #
    # print(sort_selection(tmp_arr))

    # tmp_arr = generate_array(10, max_rand_coeff=10)

    # print(sum_recursion([2,4,6]))
    # print(counter_recursion([2,4,2,24,4,4,5,8,6]))

    print(max_number_recursion([2,23213244,2,245,4,4,5,8,6]))




if __name__ == '__main__':
    main()
