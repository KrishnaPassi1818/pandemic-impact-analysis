from src.data_processor import process_data as pr_dt

import pandas as pd

def top_cases(merged):
    return merged.sort_values(by='total_cases', ascending=False).head(10)

def top_cases_per_million(merged):
    return merged.sort_values(by='cases_per_million', ascending=False).head(10)

def top_death_rate(merged):
    return merged.sort_values(by='death_rate', ascending=False).head(10)