from os import system

from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.analysis import Analyzer
from src.visualization import Visualizer
from src.report_generator import ReportGenerator


def clear():
    system("cls")


def display_table(data):
    print(data.to_string(index=False))


def setup():
    loader = DataLoader("data/covid-data.csv", "data/world_population.csv")
    covid, population = loader.load_data()

    processor = DataProcessor()
    merged = processor.process(covid, population)

    analyzer = Analyzer()
    visualizer = Visualizer()
    report = ReportGenerator()

    return merged, analyzer, visualizer, report


def menu():
    print("\n🌍 Pandemic Impact Analysis")
    print("=" * 40)
    print("1. Top Countries by Total Cases")
    print("2. Top Countries by Cases per Million")
    print("3. Top Countries by Death Rate")
    print("4. Generate Graphs")
    print("5. Generate Report")
    print("6. Exit")


def main():
    merged, analyzer, visualizer, report = setup()

    print("\n✅ Data loaded and processed successfully!\n")

    while True:
        menu()
        choice = input("\nEnter your choice (1-6): ")

        clear()

        if choice == '1':
            print("===== Top Countries by Total Cases =====\n")
            display_table(analyzer.top_cases(merged))

        elif choice == '2':
            print("===== Top Countries by Cases per Million =====\n")
            display_table(analyzer.top_cases_per_million(merged))

        elif choice == '3':
            print("===== Top Countries by Death Rate =====\n")
            display_table(analyzer.top_death_rate(merged))

        elif choice == '4':
            print("Generating graphs...\n")
            visualizer.plot_bar(merged, 'total_cases', "Top Cases", "Cases", "top_cases.png")
            visualizer.plot_bar(merged, 'cases_per_million', "Cases per Million", "Cases", "cases_per_million.png")
            visualizer.plot_bar(merged, 'death_rate', "Death Rate", "Percentage", "death_rate.png")
            print("✅ Graphs generated and saved!")

        elif choice == '5':
            report.generate(merged)
            print("✅ Report generated successfully!")

        elif choice == '6':
            print("\n👋 Thank you for using Pandemic Impact Analysis!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to continue...")
        clear()


if __name__ == "__main__":
    clear()
    main()