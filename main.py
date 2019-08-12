from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection

def main():
    # b = None
    # counter = 0
    # while not b:
    #     tmp_arr = generate_array(555, max_rand_coeff=10)
    #     b = binary_search(tmp_arr, 5484)
    #     counter += 1
    #     print(counter)
    # print(f'index ==> {b}')

    tmp_arr = generate_array(10, max_rand_coeff=10)
    print(tmp_arr)
    s = find_smallest(tmp_arr)
    print(s)

    print(sort_selection(tmp_arr))



if __name__ == '__main__':
    main()
