# ICD341 Lab 17 – Interactive Data Dashboards

## Project Title
Zambia Maize Production Dashboard

## Overview
This project demonstrates how to build an interactive data dashboard using Python, Streamlit, Pandas and Matplotlib.

The dashboard explores illustrative maize production data across five selected districts in Zambia.

**Important:** The dataset contains sample figures created for educational purposes. It does not represent official agricultural production statistics.

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib

## Dashboard Features
1. Display maize production data in a table.
2. Filter districts using a minimum production slider.
3. Calculate total and average production.
4. Identify the highest and lowest production values.
5. Visualize production using a bar chart.
6. Select individual districts to explore their production.
7. Download filtered data as a CSV file.

## Project Structure

```text
Lab17_Maize_Dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Ensure Python is installed.

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Dashboard

From the ICD341 repository root, execute:

```bash
python -m streamlit run labs/Lab17_Maize_Dashboard/app.py
```

The dashboard will open in your web browser.

## Sample Dataset

| District | Production (tonnes) |
|---|---:|
| Lusaka | 500 |
| Chongwe | 350 |
| Kabwe | 450 |
| Chipata | 600 |
| Mumbwa | 400 |

## Learning Outcomes

This project demonstrates:
- Data preparation using Pandas.
- Statistical summaries using Python.
- Interactive dashboard development with Streamlit.
- Data visualization using Matplotlib.
- User interaction through filters and selection widgets.
- Exporting data into CSV format.

## Author
ICD341 Advanced Statistical Computing  
Bachelor of Data Science  
Mulungushi University