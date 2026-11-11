# Maize Production Statistical Analysis

## Project Overview

This project demonstrates the application of statistical
computing techniques using a simulated maize production dataset.

The project uses Python, NumPy, Pandas and Matplotlib to
generate data, calculate descriptive statistics and visualise
the distribution of maize production.

## Dataset

The dataset contains 100 randomly generated maize production
observations using a normal distribution.

- Mean used for generation: 5 tonnes
- Standard deviation used for generation: 1.2 tonnes
- Number of observations: 100
- Random seed: 123

The dataset is stored in `data/maize_data.csv`.

## Statistical Analysis

The analysis calculates:

- Mean
- Standard deviation
- Minimum
- Maximum
- Descriptive statistical summary

## Visualisation

A histogram is generated to illustrate the distribution
of maize production observations.

The histogram is saved in:

`outputs/maize_histogram.png`

## Project Structure

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