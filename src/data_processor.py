import pandas as pd

def process_data(covid, population):
    covid = covid[[
        'location',
        'date',
        'total_cases',
        'total_deaths'
    ]]
    covid_latest = covid.sort_values('date').groupby('location').tail(1)
    population = population.rename(columns={
        'Country/Territory': 'location',
        '2022 Population': 'population'
    })
    population = population[[
        'location',
        'population'
    ]]
    merged = pd.merge(covid_latest, population, how="inner", on='location')

    merged['cases_per_million'] = (merged['total_cases'] / merged['population']) * 1_000_000
    merged['deaths_per_million'] = (merged['total_deaths'] / merged['population']) * 1_000_000

    return merged








