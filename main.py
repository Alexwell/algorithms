from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection
from algorithms.sum_recursion import sum_recursion
from algorithms.counter_recursion import counter_recursion
from algorithms.max_number_recursion import max_number_recursion
from algorithms.quicksort_recursion import quicksort_recursion

def main():
    tmp_arr = generate_array(100, max_rand_coeff=100)
    print(quicksort_recursion(tmp_arr))


if __name__ == '__main__':
    main()
