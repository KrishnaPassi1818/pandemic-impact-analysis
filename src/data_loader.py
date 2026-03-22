import pandas as pd

def load_data():
    covid = pd.read_csv("data/covid-data.csv")
    population = pd.read_csv("data/world_population.csv")

    return covid, population