class ReportGenerator:
    def generate(self, data):
        with open("output/report.txt", "w") as f:

            f.write("Pandemic Impact Analysis Report\n")
            f.write("=" * 50 + "\n\n")

            # Objective
            f.write("Objective:\n")
            f.write("To analyze the impact of COVID-19 across countries using population-normalized metrics.\n\n")

            # Top Countries
            top_cases = data.sort_values(by='total_cases', ascending=False).head(5)
            top_per_million = data.sort_values(by='cases_per_million', ascending=False).head(5)
            top_death = data.sort_values(by='death_rate', ascending=False).head(5)

            f.write("Top 5 Countries by Total Cases:\n")
            for _, row in top_cases.iterrows():
                f.write(f"- {row['location']}: {int(row['total_cases'])} cases\n")
            f.write("\n")

            f.write("Top 5 Countries by Cases per Million:\n")
            for _, row in top_per_million.iterrows():
                f.write(f"- {row['location']}: {round(row['cases_per_million'], 2)} per million\n")
            f.write("\n")

            f.write("Top 5 Countries by Death Rate:\n")
            for _, row in top_death.iterrows():
                f.write(f"- {row['location']}: {round(row['death_rate'], 2)}%\n")
            f.write("\n")

            # Insights
            f.write("Key Insights:\n")
            f.write("- Countries with large populations tend to report higher total cases.\n")
            f.write("- Smaller countries often show higher per capita infection rates.\n")
            f.write("- Death rate varies significantly, indicating differences in healthcare systems.\n")
            f.write("- Per capita metrics provide a more accurate comparison than total values.\n\n")

            # Interpretation
            f.write("Analysis Interpretation:\n")
            f.write("The analysis shows that raw case counts can be misleading when comparing countries.\n")
            f.write("Population-normalized metrics reveal the actual severity of the pandemic.\n")
            f.write("Some smaller nations experienced disproportionately high infection rates.\n\n")

            # Conclusion
            f.write("Conclusion:\n")
            f.write("Population size strongly influences total case counts, but per capita analysis provides a clearer understanding of pandemic impact.\n")