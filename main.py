from os import system
system("cls")

from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.analysis import Analyzer
from src.visualization import Visualizer
from src.report_generator import ReportGenerator

def main():
    print("Starting Pandemic Impact Analysis...\n")

    # Load Data
    loader = DataLoader("data/covid-data.csv", "data/world_population.csv")
    covid, population = loader.load_data()

    # Process Data
    processor = DataProcessor()
    merged = processor.process(covid, population)

    print("Data processed successfully.\n")

    # Analysis
    analyzer = Analyzer()

    print("Top 10 Countries by Total Cases:")
    print(analyzer.top_cases(merged), "\n")

    print("Top 10 Countries by Cases per Million:")
    print(analyzer.top_cases_per_million(merged), "\n")

    print("Top 10 Countries by Death Rate:")
    print(analyzer.top_death_rate(merged), "\n")

    # Visualization
    visualizer = Visualizer()

    visualizer.plot_bar(merged, 'total_cases', "Top Cases", "Cases", "top_cases.png")
    visualizer.plot_bar(merged, 'cases_per_million', "Cases per Million", "Cases", "cases_per_million.png")
    visualizer.plot_bar(merged, 'death_rate', "Death Rate", "Percentage", "death_rate.png")

    print("Graphs generated.\n")

    # Report
    report = ReportGenerator()
    report.generate(merged)

    print("Report generated successfully.\n")
    print("Project Completed.")

if __name__ == "__main__":
    main()