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



def find_lowest_coast_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def lowest_cost(graph, costs, parents):
    processed = []
