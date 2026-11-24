# Maize Production Statistical Analysis

## 1. Project Overview

This project demonstrates the application of statistical computing techniques using a simulated maize production dataset.

Python, NumPy, Pandas and Matplotlib are used to generate data, calculate descriptive statistics and visualise the distribution of maize production.

## 2. Dataset

The dataset contains 100 randomly generated maize production observations using a normal distribution.

- Mean used for generation: 5 tonnes
- Standard deviation used for generation: 1.2 tonnes
- Number of observations: 100
- Random seed: 123

The dataset is stored in `data/maize_data.csv`.

## 3. Statistical Analysis

The analysis calculates:

- Mean
- Standard deviation
- Minimum
- Maximum
- Complete descriptive statistical summary

The analysis is implemented in `src/analysis.py`.

## 4. Visualisation

A histogram is generated to illustrate the distribution of maize production observations.

The resulting image is saved in:

`outputs/maize_histogram.png`

## 5. Project Structure

```text
Maize_Production_Project/
├── data/
│   └── maize_data.csv
├── notebooks/
│   └── maize_analysis.ipynb
├── src/
│   └── analysis.py
├── outputs/
│   └── maize_histogram.png
├── README.md
└── requirements.txt
```

## 6. Installation

Install the required dependencies using:

```bash
python -m pip install -r requirements.txt
```

## 7. Running the Analysis

From the project root directory, execute:

```bash
python src/analysis.py
```

The script loads the dataset, calculates descriptive statistics and generates the histogram.

## 8. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## 9. Conclusion

This project demonstrates reproducible data generation, statistical analysis, data visualisation and basic Python project organisation.