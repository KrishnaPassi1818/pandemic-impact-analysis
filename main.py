from src.data_loader import load_data
from src.data_processor import process_data
from src.analysis import top_cases, top_cases_per_million, top_death_rate
from src.visualization import plot_top_cases, plot_cases_per_million, plot_death_rate
from src.report_generator import generate_report

covid, population = load_data()
merged = process_data(covid, population)

merged['death_rate'] = (merged['total_deaths'] / merged['total_cases']) * 100

print("Top 10 Countries by Total Cases:")
print(top_cases(merged))

print("\nTop 10 Countries by Cases per Million:")
print(top_cases_per_million(merged))

print("\nTop 10 Countries by Death Rate:")
print(top_death_rate(merged))

plot_top_cases(merged)
plot_cases_per_million(merged)
plot_death_rate(merged)

generate_report(merged)