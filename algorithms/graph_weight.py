processed = []

def lowest_cost(graph, costs, parents):
    if start_fin_checking(graph):
        return 'wrong graph'
    elif start_fin_checking(costs):
        return 'wrong costs'
    elif start_fin_checking(parents):
        return 'wrong parents'

    if keys_chacking(graph, costs, parents):
        return 'incorrect input'

    if inner_keys_chacking(graph, costs):
        return 'incorrect inner key'


    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return [costs, parents]


def best_cost_way(costs, parents):
    best_cost = costs['fin']

    current_parrent = 'fin'
    best_way = [current_parrent]

    while current_parrent != 'start':
        best_way.append(parents[current_parrent])
        current_parrent = parents[current_parrent]

    best_way.reverse()
    return [best_cost, best_way]



def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def start_fin_checking(dict, start='start', fin='fin'):
    if start not in dict.keys() or fin not in dict.keys():
        return True


def keys_chacking(*args):
    tmp_keys = args[0].keys()
    for i in args:
        if i.keys() != tmp_keys: return True


def inner_keys_chacking(main_dict, checker):
    tmp = []
    for i in main_dict:
        for j in main_dict[i]:
            tmp.append(j)
    set(tmp)
    for i in tmp:
        if i not in checker: return True
