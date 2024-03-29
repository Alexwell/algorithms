from algorithms.binary_search import binary_search
from utils.generate_array import generate_array
from algorithms.sort_selection import find_smallest, sort_selection
from algorithms.sum_recursion import sum_recursion
from algorithms.counter_recursion import counter_recursion
from algorithms.max_number_recursion import max_number_recursion
from algorithms.quicksort_recursion import quicksort_recursion
from algorithms.queue_graphs import search_seller
from algorithms.graph_weight import lowest_cost, best_cost_way
from algorithms.WeightGraph import WeightGraph
from algorithms.Greed import Greed

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

    graph2 = {
            'start':
                {
                'a': 5,
                'b': 2,
                },
            'a':
                {
                'c': 4,
                'd': 2
                },
            'b':
                {
                'a': 8,
                'd': 7
                },
            'c':
                {
                'fin': 3,
                'd': 6
                },
            'd':
                {
                'fin':1
                },
            'fin':
                {
                }
            }


    # a = lowest_cost(graph2)
    # print(a)
    # b = best_cost_way(a[0], a[1])
    # print(b)
    #
    # obj = WeightGraph(graph2)
    # print(obj.best_way_cost)

    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    stations = {
        'kone': {
            'id',
            'nv',
            'ut'
        },
        'ktwo': {
            'wa',
            'id',
            'mt'
        },
        'kthree':{
            'or',
            'nv',
            'ca'
        },
        'kfour':{
            'nv',
            'ut'
        },
        'kfive':{
            'ca',
            'az'
        }
    }

    a = Greed(states_needed, stations)

    print(a)

    print(a.final_stations)


if __name__ == '__main__':
    main()
