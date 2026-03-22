import matplotlib.pyplot as plt

def plot_top_cases(data):
    top = data.sort_values(by='total_cases', ascending=False).head(10)

    plt.figure()
    plt.bar(top['location'], top['total_cases'])
    plt.xticks(rotation=45)
    plt.title("Top 10 Countries by Total Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")

    plt.tight_layout()
    plt.savefig("output/graphs/top_cases.png")
    plt.show()

def plot_cases_per_million(data):
    top = data.sort_values(by='cases_per_million', ascending=False).head(10)

    plt.figure()
    plt.bar(top['location'], top['cases_per_million'])
    plt.xticks(rotation=45)
    plt.title("Top 10 Countries by Cases per Million")
    plt.xlabel("Country")
    plt.ylabel("Cases per Million")

    plt.tight_layout()
    plt.savefig("output/graphs/cases_per_million.png")
    plt.show()

def plot_death_rate(data):
    top = data.sort_values(by='death_rate', ascending=False).head(10)

    plt.figure()
    plt.bar(top['location'], top['death_rate'])
    plt.xticks(rotation=45)
    plt.title("Top 10 Countries by Death Rate")
    plt.xlabel("Country")
    plt.ylabel("Death Rate (%)")

    plt.tight_layout()
    plt.savefig("output/graphs/death_rate.png")
    plt.show()