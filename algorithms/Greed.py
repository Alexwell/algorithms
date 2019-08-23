class Greed(object):
    def __init__(self, states_needed, stations):
        self.states_needed = states_needed
        self.stations = stations
        self.final_stations = self.calculate_final_stations()

    def calculate_final_stations(self):
        final_stations = set()
        while self.states_needed:
            best_station = None
            states_covered = set()
            for station, states in self.stations.items():
                covered = self.states_needed & states
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered
            self.states_needed -= states_covered
            final_stations.add(best_station)
        return final_stations
