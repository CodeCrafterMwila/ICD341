\# Data Sources and Data Management Plan



\## 1. Primary Dataset: FAOSTAT



\- \*\*Provider:\*\* Food and Agriculture Organization of the United Nations (FAO).

\- \*\*Database:\*\* FAOSTAT – Crops and Livestock Products.

\- \*\*Country:\*\* Zambia.

\- \*\*Crop:\*\* Maize (corn).

\- \*\*Element:\*\* Production.

\- \*\*Unit:\*\* Tonnes.

\- \*\*Expected time coverage:\*\* 1961–2024 (to be verified after downloading).

\- \*\*Purpose:\*\* Analyse national historical production trends, calculate descriptive statistics, and perform time-series regression.

\- \*\*Official source:\*\* https://www.fao.org/faostat/en/



\## 2. Supporting Dataset: Zambia Statistics Agency



\- \*\*Provider:\*\* Zambia Statistics Agency (ZamStats).

\- \*\*Sources:\*\* Crop Forecasting Survey (CFS) and, where available, Post-Harvest Survey (PHS).

\- \*\*Geographic coverage:\*\* Zambia's ten provinces.

\- \*\*Potential variables:\*\* Maize area planted, expected or actual production, harvested area, and yield.

\- \*\*Purpose:\*\* Provincial comparisons and interactive dashboard visualizations.

\- \*\*Official source:\*\* https://www.zamstats.gov.zm/agriculture-and-environment/



\## 3. Data Status and Important Distinctions



\- FAOSTAT annual production data will be the primary historical dataset.

\- CFS figures are forecasts or early estimates made during the growing season.

\- PHS figures are collected after harvest and provide information on actual production.

\- Forecasts and actual production figures must not be mixed without clearly identifying their status.

\- Units, years, agricultural seasons, geographic labels, and source definitions will be preserved.

\- Missing values and any data revisions will be documented.



\## 4. Planned Variables



| Variable | Description | Unit |

|---|---|---|

| Year | Calendar year or agricultural season, depending on source | Year/season |

| Country | Country name | Text |

| Province | Province name, for provincial data | Text |

| Crop | Crop name | Text |

| Production | Quantity of maize produced | Tonnes |

| Area harvested | Land area harvested, where available | Hectares |

| Yield | Production per unit area, where available | Tonnes per hectare |



\## 5. Data Cleaning Plan



1\. Retain records for Zambia and maize.

2\. Select the required production, year, and geographic fields.

3\. Convert numeric fields to appropriate numeric data types.

4\. Standardize province names and year or season formats.

5\. Check for missing values and duplicate records.

6\. Verify measurement units and distinguish calendar years from agricultural seasons.

7\. Preserve the original downloaded data and create separate cleaned datasets.



\## 6. Data Citation



\- FAO. \*FAOSTAT: Crops and Livestock Products.\* Record the date of data access.

\- Zambia Statistics Agency. \*Crop Forecasting Survey / Post-Harvest Survey publications.\* Record the publication and access dates.

