import pandas as pd

class Analyzer:
    def top_cases(self, data):
        return data.sort_values(by='total_cases', ascending=False).head(10)

    def top_cases_per_million(self, data):
        return data.sort_values(by='cases_per_million', ascending=False).head(10)

    def top_death_rate(self, data):
        return data.sort_values(by='death_rate', ascending=False).head(10)