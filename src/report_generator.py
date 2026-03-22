def generate_report(data):
    with open("output/report.txt", "w") as f:

        f.write("Pandemic Impact Analysis Report\n")
        f.write("=" * 40 + "\n\n")

        # top country by total cases
        top_cases = data.sort_values(by='total_cases', ascending=False).iloc[0]
        f.write(f"Most affected country (total cases): {top_cases['location']}\n")

        # top country by cases per million
        top_per_million = data.sort_values(by='cases_per_million', ascending=False).iloc[0]
        f.write(f"Highest cases per million: {top_per_million['location']}\n")

        # highest death rate
        top_death = data.sort_values(by='death_rate', ascending=False).iloc[0]
        f.write(f"Highest death rate: {top_death['location']}\n")

        f.write("\nKey Insights:\n")
        f.write("- Countries with large populations show high total cases.\n")
        f.write("- Smaller countries dominate per capita metrics.\n")
        f.write("- Death rates vary significantly across countries.\n")
        f.write("- Per capita analysis provides better comparison than total values.\n")

        f.write("\nConclusion:\n")
        f.write("Population size plays a crucial role in pandemic spread, but per capita metrics reveal the true severity.\n")