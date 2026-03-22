import pandas as pd

class DataProcessor:
    def process(self, covid, population):
        covid = covid[['location', 'date', 'total_cases', 'total_deaths']]
        covid_latest = covid.sort_values('date').groupby('location').tail(1)

        population = population.rename(columns={
            'Country/Territory': 'location',
            '2022 Population': 'population'
        })
        population = population[['location', 'population']]

        merged = pd.merge(covid_latest, population, on='location', how='inner')

        merged = merged.dropna(subset=['total_cases', 'total_deaths'])

        merged['cases_per_million'] = (merged['total_cases'] / merged['population']) * 1_000_000
        merged['deaths_per_million'] = (merged['total_deaths'] / merged['population']) * 1_000_000

        merged['death_rate'] = (merged['total_deaths'] / merged['total_cases']) * 100

        # Remove unwanted aggregated rows
        merged = merged[~merged['location'].isin(['World', 'Asia', 'Europe', 'Africa'])]

        return merged
    