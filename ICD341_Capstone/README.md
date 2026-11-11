# Statistical Analysis and Visualization of Maize Production in Zambia (1961–2024)

## 1. Project Overview

This project investigates historical maize production in Zambia from 1961 to 2024 using statistical computing techniques in Python.

Maize is an important agricultural crop in Zambia. Understanding historical production patterns can help identify long-term trends, changes in harvested area, yield variations and possible structural changes in agricultural production.

The project applies descriptive statistics, data visualization, correlation analysis, regression modelling and structural break analysis. An interactive dashboard built with Streamlit and Plotly presents the findings.

## 2. Project Aim

To statistically analyse and visualize historical maize production in Zambia between 1961 and 2024 using Python.

## 3. Objectives

The project aims to:

1. Obtain and prepare historical maize production data for Zambia.
2. Examine trends in maize production, harvested area and yield.
3. Apply descriptive statistical methods to summarize the dataset.
4. Investigate relationships between production, harvested area and yield.
5. Fit and evaluate regression models for maize production.
6. Investigate potential structural changes in historical production trends.
7. Develop an interactive dashboard for presenting the results.
8. Apply reproducible statistical computing practices.

## 4. Data Sources

The primary dataset was obtained from the Food and Agriculture Organization of the United Nations (FAOSTAT).

**Primary source:**
https://www.fao.org/faostat/en/

**Supplementary source:**
https://www.zamstats.gov.zm/agriculture-and-environment/

The analysis focuses on:

- Country: Zambia
- Crop: Maize (corn)
- Period: 1961–2024
- Number of annual observations: 64

The dataset contains three main agricultural indicators:

| Indicator | Description | Unit |
|---|---|---|
| Production | Total maize production | Tonnes |
| Area harvested | Total land area harvested for maize | Hectares |
| Yield | Maize production per harvested area | kg/ha |

FAOSTAT observation flags are retained to distinguish official, estimated, imputed and other reported values.

## 5. Methodology

The project follows a structured statistical computing workflow.

### 5.1 Data Preparation

- Extracted Zambia's maize production records from the FAOSTAT dataset.
- Filtered the data by country and crop.
- Restructured the original data into a usable tabular format.
- Cleaned and organized the dataset.
- Preserved the original observation flags.
- Exported the cleaned dataset to CSV.

### 5.2 Descriptive Statistics

Calculated summary statistics, including:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum

### 5.3 Data Visualization

Created visualizations to investigate:

- Annual maize production trends.
- Harvested area trends.
- Yield trends.
- Relationships between agricultural indicators.
- Correlation patterns.

### 5.4 Correlation Analysis

Used Pearson correlation coefficients to examine the relationships between maize production, harvested area and yield.

### 5.5 Regression Analysis

Applied simple linear regression to investigate the long-term production trend.

Regression diagnostics included:

- Residual analysis.
- Durbin-Watson test.
- Breusch-Pagan test.
- Shapiro-Wilk test.
- Newey-West heteroscedasticity and autocorrelation consistent standard errors.

### 5.6 Structural Break Analysis

Applied continuous segmented regression to investigate possible changes in the long-term production trend.

Additional procedures included:

- Grid-search breakpoint selection.
- Model comparison using R-squared, adjusted R-squared, AIC and BIC.
- Residual and influence diagnostics.
- Sensitivity analysis excluding the 2024 observation.
- Leave-one-out breakpoint stability analysis.
- Sup-F testing with dependent wild bootstrap calibration.

## 6. Key Findings

The analysis produced several important findings.

### Historical Production

- The highest recorded production in the dataset occurred in 2021, at approximately 3.62 million tonnes.
- The lowest occurred in 1992, at approximately 483,492 tonnes.
- The simple linear regression indicates a positive long-term production trend.

### Relationship Between Agricultural Indicators

Both harvested area and yield have positive correlations with maize production.

| Variable | Correlation with Production |
|---|---:|
| Harvested Area | 0.7713 |
| Yield | 0.8029 |

These results indicate positive associations but do not establish causation.

### 2023–2024 Production Change

Between 2023 and 2024:

- Maize production declined by approximately 53.67%.
- Harvested area declined by approximately 51.75%.
- Yield declined by approximately 3.98%.

The reduction in harvested area was the dominant factor associated with the production decline.

### Structural Break Analysis

The segmented regression analysis identified 2002 as the best-fitting candidate breakpoint.

Breakpoint stability analysis indicates that the exact year is uncertain, with 2001 also being a close candidate. The findings therefore suggest a possible change in the production trend during the early 2000s.

Bootstrap testing provided statistical evidence of a structural break under the assumptions of the fitted model.

The results do not establish the cause of the structural change.

## 7. Interactive Dashboard

The project includes an interactive dashboard developed using Streamlit and Plotly.

The dashboard provides:

- Dataset overview and summary indicators.
- Key agricultural production statistics.
- Interactive year-range filtering.
- Annual production visualizations.
- Harvested area and yield visualizations.
- Correlation heatmap.
- Structural break analysis.
- Segmented regression visualization.
- Key findings and interpretation.
- Data source and quality information.
- Downloadable datasets and analysis results.

### Running the Dashboard

From the capstone project directory, run:

```bash
python -m streamlit run dashboard/app.py
```

The dashboard will open in your default web browser.

## 8. Project Structure

```text
ICD341_Capstone/
│
├── data/
│   ├── raw/
│   │   └── extracted/
│   └── maize_production.csv
│
├── notebooks/
│   └── maize_analysis.ipynb
│
├── src/
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── annual_maize_production.png
│   ├── bootstrap_sup_f_comparison.png
│   ├── maize_correlation_heatmap.png
│   ├── maize_harvested_area.png
│   ├── maize_yield.png
│   ├── segmented_regression.png
│   ├── correlation_matrix.csv
│   ├── descriptive_statistics.csv
│   ├── regression_results.csv
│   └── structural_break_results.csv
│
├── clean_data.py
├── requirements.txt
├── PROJECT_PROPOSAL.md
├── DATA_SOURCES.md
└── README.md
```

## 9. Installation and Reproducibility

### Requirements

The project uses Python and the following major libraries:

- NumPy
- Pandas
- Matplotlib
- SciPy
- Statsmodels
- Plotly
- Streamlit
- JupyterLab
- nbconvert

### Install Dependencies

Clone the repository and navigate into the capstone directory.

Install the required packages:

```bash
pip install -r requirements.txt
```

### Reproduce Data Cleaning

Run:

```bash
python clean_data.py
```

This regenerates the cleaned maize production dataset.

### Reproduce the Statistical Analysis

Open the notebook:

```text
notebooks/maize_analysis.ipynb
```

Select the project Python environment and execute the notebook cells in order.

### Run the Dashboard

Execute:

```bash
python -m streamlit run dashboard/app.py
```

## 10. Limitations

The analysis has several limitations:

1. The study relies on historical secondary data obtained from FAOSTAT.
2. Some historical observations are estimated or sourced from external organizations, as indicated by the original observation flags.
3. The analysis identifies statistical relationships but does not establish causation.
4. Regression diagnostics indicate autocorrelation and heteroscedasticity, which affect conventional regression inference.
5. The identified structural breakpoint is a statistical candidate rather than proof of a specific historical event or policy effect.
6. The 2024 observation is influential, but it has been retained because it is a valid reported observation in the dataset.

## 11. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Statistical computing |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib | Statistical visualization |
| SciPy | Statistical testing |
| Statsmodels | Regression analysis |
| Plotly | Interactive visualization |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Reproducible analysis |
| Git and GitHub | Version control |

## 12. Author

**Mwila Singoma**

Bachelor of Data Science Student
Mulungushi University

**Course:** ICD341 – Advanced Statistical Computing

**Academic Year:** 2026

**GitHub:** [CodeCrafterMwila](https://github.com/CodeCrafterMwila)

---

*This project was developed for academic purposes as part of the ICD341 Advanced Statistical Computing course at Mulungushi University.*