from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection
from algorithms.sum_recursion import sum_recursion
from algorithms.counter_recursion import counter_recursion
from algorithms.max_number_recursion import max_number_recursion
from algorithms.quicksort_recursion import quicksort_recursion
from algorithms.queue import search_seller


def main():
    # graph = {}
    # graph['you'] = ['alice', 'bob', 'peggy']
    # graph['bob'] = ['anuj', 'peggy', 'you']
    # graph['alice'] = ['peggy', 'claire']
    # graph['claire'] = ['thom', 'jonny']
    # graph['anuj'] = []
    # graph['peggy'] = ['you', 'alice', 'bob']
    # graph['thom'] = []
    # graph['jonny'] = []
    #
    # search_seller(**graph)


    graph = {
            'start':
                {
                'a': 6,
                'b': 2,
                },
            'a':
                {
                'fin': 1
                },
            'b':{
                'a': 3,
                'fin': 5
                }
            }

    costs = {
            'a': 6,
            'b': 2,
            'fin': float('inf')
            }

    parents = {
            'a': 'start',
            'b': 'start',
            'fin': None
            }



if __name__ == '__main__':
    main()
