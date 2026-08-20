# Python Learning 🐍

My Python learning journey through hands-on projects, progressing from Python fundamentals to data analysis and visualization.

## Projects

### 01 — Grade Calculator 🎓

A simple Python program that calculates a student's average grade and assigns a letter grade.

**Concepts practiced:**
- Variables and user input
- Arithmetic operations
- Conditional statements
- Comparison operators
- Type conversion

📁 [`01-grade-calculator`](./01-grade-calculator)

---

### 02 — Expense Analyzer 💰

A data analysis project for exploring and summarizing personal expense data using Python.

**Concepts practiced:**
- Pandas DataFrames
- Data cleaning and manipulation
- Grouping and aggregation
- Basic statistical analysis
- Data visualization with Matplotlib

📁 [`02-expense-analyzer`](./02-expense-analyzer)

---

### 03 — Climate Data Explorer 🌍

A climate data analysis project exploring long-term changes in Turkey's annual average surface temperature from 1940 to 2025.

**Concepts practiced:**
- Real-world data exploration
- Pandas filtering
- Descriptive statistics
- Time-series analysis
- 10-year moving averages
- Linear trend estimation with NumPy
- Data visualization with Matplotlib

**Key finding:**  
The analysis estimates an overall linear temperature trend of approximately **+0.28 °C per decade** for Turkey over the 1940–2025 period.

📁 [`03-climate-data-explorer`](./03-climate-data-explorer)

---

### 4. Particle Collision EDA ⚛️

An exploratory data analysis project using simulated high-energy physics collision data from the HIGGS dataset.

**What I practiced:**
- Descriptive statistics
- Signal vs background comparison
- Grouping and aggregation with Pandas
- Pearson correlation analysis
- Scientific data visualization with Matplotlib

**Key finding:** Among the selected features, `missing_energy` and `m_wwbb` showed the strongest positive linear relationship (**r ≈ 0.313**).

📁 [View Project](./04-particle-collision-eda)

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git & GitHub

## Learning Progress

This repository documents my progression from Python fundamentals toward data analysis, scientific computing, and real-world problem solving.

Each project focuses on applying newly learned concepts through practical implementation rather than isolated exercises.

## Repository Structure

```text
python-learning/
│
├── grade_calculator.py
│
├── 02-expense-analyzer/
│   ├── expense_analyzer.py
│   ├── expenses.csv
│   └── README.md
│
├── 03-climate-data-explorer/
│   ├── climate_analysis.py
│   ├── data/
│   ├── visualizations/
│   └── README.md
│
├── 04-particle-collision-eda/
│   ├── analysis.py
│   ├── higgs_train_10k.csv
│   ├── correlation_plot.png
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```