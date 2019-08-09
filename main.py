from algorithms.binary_search import binary_search
from utils.generate_array import generate_array


def main():
    b = None
    counter = 0
    while not b:
        tmp_arr = generate_array(555, max_rand_coeff=1000)
        b = binary_search(tmp_arr, 5484)
        counter += 1
        print(counter)
    print(f'index ==> {b}')
    print(sorted(tmp_arr))


if __name__ == '__main__':
    main()
