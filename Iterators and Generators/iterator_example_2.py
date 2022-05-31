import math
class Pandemic:
    def __init__(self, infection_rate, no_of_initial_infections):
        self.infection_rate = infection_rate
        self.no_of_initial_infections = no_of_initial_infections
        self.pandemic_day = 0

    def cases_by_day(self, no_of_days):
        no_of_cases = (self.no_of_inital_infections)*((math.e)**(self.infection_rate*no_of_days))
        return no_of_cases

    def __iter__(self):
        return self

    def __next__(self):
        current_cases = self.cases_by_day(self.pandemic_day)
        self.pandemic_day +=1
        return current_cases