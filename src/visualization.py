import matplotlib.pyplot as plt

class Visualizer:
    def plot_bar(self, data, column, title, ylabel, filename):
        top = data.sort_values(by=column, ascending=False).head(10)

        plt.figure()
        plt.bar(top['location'], top[column])
        plt.xticks(rotation=60)
        plt.title(title)
        plt.xlabel("Country")
        plt.ylabel(ylabel)

        plt.tight_layout()
        plt.savefig(f"output/graphs/{filename}")
        plt.show()