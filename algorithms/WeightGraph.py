class WeightGraph(object):
    def __init__(self, graph):
        self.graph = graph
        self.costs = self.create_costs()
        self.parents = self.create_parents()
        self.processed = []
        self.best_way_cost = self.find_way()


    def create_costs(self):
        initial_costs = {
            'start': 0,
            'fin': float('inf'),
        }

        for i in self.graph.keys():
            if i == 'start': continue
            initial_costs[i] = float('inf')
        return initial_costs


    def create_parents(self):
        initial_parents = {
            'start': None,
            'fin': None,
        }
        for i in self.graph['start'].keys():
            initial_parents[i] = 'start'
        return initial_parents


    def start_fin_checking(self, start='start', fin='fin'):
        if start not in self.graph.keys() or fin not in self.graph.keys():
            return True


    def inner_keys_chacking(self):
        tmp = []
        for i in self.graph:
            for j in self.graph[i]:
                tmp.append(j)
        set(tmp)
        for i in tmp:
            if i not in self.costs:
                return True


    def find_lowest_cost_node(self):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node


    def find_way(self):
        if self.start_fin_checking():
            print('wrong graph')
            return 'wrong graph'
        if self.inner_keys_chacking():
            print('incorrect inner key')
            return 'incorrect inner key'

        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()

        current_parrent = 'fin'
        best_way =[current_parrent]

        while current_parrent != 'start':
            best_way.append(self.parents[current_parrent])
            current_parrent = self.parents[current_parrent]

        best_way.reverse()
        return [self.costs['fin'], best_way]
