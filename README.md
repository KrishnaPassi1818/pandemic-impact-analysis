# 🌍 Pandemic Impact Analysis

A comprehensive data analysis project that evaluates the global impact of COVID-19 by integrating pandemic data with population statistics.
The system provides insights, visualizations, automated reports, and a rule-based risk prediction model using a structured Object-Oriented design.

---

## 📌 Objective

To analyze COVID-19 impact across countries using both absolute and population-normalized metrics, and to derive meaningful insights along with risk-based classification.

---

## 🚀 Features

* 📥 Data loading from multiple CSV datasets
* 🧹 Data cleaning and preprocessing
* 🔗 Dataset merging (COVID + Population)
* 📊 Data analysis (top affected countries, death rates, per capita metrics)
* 📈 Visualization using bar charts
* 📝 Automated report generation with insights
* 🧠 Object-Oriented Programming (OOP) design
* 💻 Interactive CLI (Command Line Interface)
* 🔮 Risk Prediction Module (rule-based classification)
* 🔄 Version control using Git & GitHub

---

## 🏗️ Project Structure

```
pandemic-impact-analysis/
│
├── data/
│   ├── covid-data.csv
│   └── world_population.csv
│
├── output/
│   ├── graphs/
│   └── report.txt
│
├── src/
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── report_generator.py
│   └── predictor.py
│
├── main.py
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

## 🧠 Key Analysis Performed

* Top countries by total COVID cases
* Top countries by cases per million
* Countries with highest death rate
* Comparative analysis between total vs per capita metrics

---

## 🔮 Prediction Module

A rule-based prediction system is implemented to classify countries into:

* **High Risk**
* **Medium Risk**
* **Low Risk**

### 📊 Criteria Used:

* Cases per million
* Death rate (%)

### 🧠 Logic:

* High risk → High cases per million OR high death rate
* Medium risk → Moderate cases
* Low risk → Lower infection impact

This demonstrates basic data-driven decision making and serves as an introduction to predictive modeling.

---

## 💻 CLI Interface

The project includes an interactive menu:

```
1. Top Countries by Total Cases
2. Top Countries by Cases per Million
3. Top Countries by Death Rate
4. Generate Graphs
5. Generate Report
6. Exit
7. Predict Risk Levels
```

---

## 📈 Outputs

* 📊 Graphs:

  * Total Cases
  * Cases per Million
  * Death Rate

* 📄 Report:

  * Key findings
  * Insights
  * Conclusion

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone <your-repo-url>
cd pandemic-impact-analysis
```

2. Install dependencies:

```
pip install pandas matplotlib numpy
```

3. Run the project:

```
python main.py
```

---

## 📁 Output Location

* Graphs → `output/graphs/`
* Report → `output/report.txt`

---

## 🧠 Key Insights

* Larger populations often show higher total cases
* Smaller countries may show higher per capita impact
* Death rates vary significantly across regions
* Per capita analysis provides better comparison than raw totals

---

## 🔮 Future Improvements

* Add machine learning-based prediction
* Build web dashboard (Streamlit / Flask)
* Export report as PDF
* Add real-time data updates

---

## 👨‍💻 Author

Krishna
B.Tech CSE Student

---

## ⭐ Acknowledgment

Datasets sourced from publicly available COVID-19 and population data repositories.

---