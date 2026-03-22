# 🌍 Pandemic Impact Analysis

A data-driven project that analyzes the global impact of COVID-19 by combining pandemic data with population statistics to generate meaningful insights, visualizations, and automated reports.

---

## 📌 Objective

The objective of this project is to evaluate the severity of COVID-19 across countries using both **absolute metrics** (total cases, deaths) and **normalized metrics** (cases per million, deaths per million).

---

## 🚀 Features

* 📥 Data loading from multiple CSV datasets
* 🧹 Data cleaning and preprocessing
* 🔗 Dataset merging (COVID + Population)
* 📊 Data analysis (top affected countries, death rates, per capita metrics)
* 📈 Visualization using bar charts
* 📝 Automated report generation with insights
* 🧠 Object-Oriented Programming (OOP) design
* 🔄 Version control using Git & GitHub

---

## 🏗️ Project Structure

```
pandemic-impact-analysis/
│
├── data/                  # Raw datasets
│   ├── covid-data.csv
│   └── world_population.csv
│
├── output/
│   ├── graphs/            # Generated graphs
│   └── report.txt         # Final analysis report
│
├── src/
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── analysis.py
│   ├── visualization.py
│   └── report_generator.py
│
├── main.py                # Main execution file
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* pandas
* matplotlib
* numpy
* Git & GitHub

---

## 📊 Key Analysis Performed

* Top countries by total COVID cases
* Top countries by cases per million
* Countries with highest death rate
* Comparative analysis between total vs per capita metrics

---

## 📈 Sample Outputs

* Bar charts for:

  * Total cases
  * Cases per million
  * Death rate

* Generated report including:

  * Key findings
  * Insights
  * Conclusion

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone <your-repo-url>
cd pandemic-impact-analysis
```

2. Install dependencies:

```bash
pip install pandas matplotlib numpy
```

3. Run the project:

```bash
python main.py
```

---

## 📄 Output

* 📁 Graphs saved in: `output/graphs/`
* 📄 Report generated at: `output/report.txt`

---

## 🧠 Key Insights

* Countries with larger populations show higher total cases
* Smaller countries often have higher per capita impact
* Death rates vary significantly across regions
* Per capita metrics provide better comparison than raw totals

---

## 🔮 Future Improvements

* Add interactive dashboard (Streamlit / Flask)
* Include correlation heatmaps
* Implement basic prediction models
* Export report as PDF

---

## 👨‍💻 Author

Krishna
B.Tech CSE Student

---

## ⭐ Acknowledgment

Datasets sourced from publicly available COVID-19 and population data repositories.

---
