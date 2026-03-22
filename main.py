from src.data_loader import load_data
from src.data_processor import process_data

covid, population = load_data()
merged = process_data(covid, population)

print(merged.head(20))