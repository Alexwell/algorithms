from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection
from algorithms.sum_recursion import sum_recursion
from algorithms.counter_recursion import counter_recursion
from algorithms.max_number_recursion import max_number_recursion
from algorithms.quicksort_recursion import quicksort_recursion
from algorithms.queue_graphs import search_seller
from algorithms.graph_weight import lowest_cost, best_cost_way


def main():
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
            'b':
                {
                'a': 3,
                'fin': 5
                },
            'fin':
                {

                }
            }

    costs = {
            'start': 0,
            'a': float('inf'),
            'b': float('inf'),
            'fin': float('inf')
            }

    parents = {
            'start': None,
            'a': 'start',
            'b': 'start',
            'fin': None
            }

    a = lowest_cost(graph, costs, parents)
    print(a)
    b = best_cost_way(a[0], a[1])
    print(b)



if __name__ == '__main__':
    main()
