import pandas as pd

class DataLoader:
    def __init__(self, covid_path, population_path):
        self.covid_path = covid_path
        self.population_path = population_path

    def load_data(self):
        covid = pd.read_csv(self.covid_path)
        population = pd.read_csv(self.population_path)
        return covid, population