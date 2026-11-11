from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px


# ---------------------------------------
# 1. PROJECT PATHS
# ---------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "maize_production.csv"
OUTPUTS_PATH = PROJECT_ROOT / "outputs"


# ---------------------------------------
# 2. PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Zambia Maize Production Dashboard",
    page_icon="🌽",
    layout="wide"
)


# ---------------------------------------
# 3. LOAD DATA
# ---------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()


# ---------------------------------------
# 4. DASHBOARD HEADER
# ---------------------------------------

st.title("🌽 Zambia Maize Production Dashboard")

st.markdown(
    """
    ### Statistical Analysis and Visualization of Maize Production in Zambia

    This interactive dashboard explores Zambia's historical maize
    production, harvested area and yield from 1961 to 2024.

    **Data source:** FAOSTAT.
    """
)

st.divider()


# ---------------------------------------
# 5. BASIC DATASET INFORMATION
# ---------------------------------------

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Observations", len(df))

with col2:
    st.metric("Starting Year", int(df["Year"].min()))

with col3:
    st.metric("Ending Year", int(df["Year"].max()))


st.success("Dataset loaded successfully!")

st.subheader("Preview of Maize Production Data")

st.dataframe(
    df.head(10),
    use_container_width=True
)


# ---------------------------------------
# 6. KEY PERFORMANCE INDICATORS
# ---------------------------------------

latest = df.iloc[-1]
previous = df.iloc[-2]

production_change = (
    (latest["Production_tonnes"] - previous["Production_tonnes"])
    / previous["Production_tonnes"]
) * 100

st.subheader("Key Production Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Years Analysed",
        len(df)
    )

with col2:
    st.metric(
        "Latest Production",
        f"{latest['Production_tonnes']:,.0f} tonnes",
        f"{production_change:+.2f}%"
    )

with col3:
    st.metric(
        "Harvested Area",
        f"{latest['Area_harvested_ha']:,.0f} ha"
    )

with col4:
    st.metric(
        "Latest Yield",
        f"{latest['Yield_kg_per_ha']:,.0f} kg/ha"
    )


# ---------------------------------------
# 7. YEAR RANGE FILTER
# ---------------------------------------

st.divider()

st.subheader("Explore a Specific Period")

selected_years = st.slider(
    "Select year range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(int(df["Year"].min()), int(df["Year"].max()))
)

filtered_df = df[
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
]


# ---------------------------------------
# 8. ANNUAL MAIZE PRODUCTION
# ---------------------------------------

st.divider()

st.subheader("Annual Maize Production in Zambia")

fig = px.line(
    filtered_df,
    x="Year",
    y="Production_tonnes",
    title=f"Maize Production Trend ({selected_years[0]}–{selected_years[1]})",
    markers=True,
    labels={
        "Year": "Year",
        "Production_tonnes": "Production (tonnes)"
    }
)

fig.update_layout(
    hovermode="x unified",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ---------------------------------------
# 9. HARVESTED AREA AND MAIZE YIELD
# ---------------------------------------

st.divider()

st.subheader("Harvested Area and Maize Yield")

col1, col2 = st.columns(2)


# Harvested area chart
with col1:

    area_fig = px.line(
        filtered_df,
        x="Year",
        y="Area_harvested_ha",
        title="Annual Harvested Area",
        markers=True,
        labels={
            "Year": "Year",
            "Area_harvested_ha": "Area (hectares)"
        }
    )

    area_fig.update_layout(
        template="plotly_dark",
        hovermode="x unified"
    )

    st.plotly_chart(
        area_fig,
        use_container_width=True
    )


# Maize yield chart
with col2:

    yield_fig = px.line(
        filtered_df,
        x="Year",
        y="Yield_kg_per_ha",
        title="Annual Maize Yield",
        markers=True,
        labels={
            "Year": "Year",
            "Yield_kg_per_ha": "Yield (kg/ha)"
        }
    )

    yield_fig.update_layout(
        template="plotly_dark",
        hovermode="x unified"
    )

    st.plotly_chart(
        yield_fig,
        use_container_width=True
    )


# ---------------------------------------
# 10. CORRELATION HEATMAP
# ---------------------------------------

st.divider()

st.subheader("Correlation Analysis")

correlation = df[
    [
        "Area_harvested_ha",
        "Yield_kg_per_ha",
        "Production_tonnes"
    ]
].corr()

fig_corr = px.imshow(
    correlation,
    text_auto=".3f",
    color_continuous_scale="RdYlGn",
    zmin=-1,
    zmax=1,
    aspect="auto",
    title="Correlation Between Maize Production Variables"
)

fig_corr.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)

st.caption(
    "Correlation measures the strength and direction of linear "
    "relationships. Correlation does not establish causation."
)

# ---------------------------------------
# 11. STRUCTURAL BREAK ANALYSIS
# ---------------------------------------

st.divider()

st.subheader("Structural Break Analysis")

break_path = OUTPUTS_PATH / "structural_break_results.csv"

if break_path.exists():

    break_df = pd.read_csv(break_path)

    st.markdown(
        """
        This analysis examines whether Zambia's maize production
        trend experienced a structural change around the early 2000s.
        """
    )

    st.dataframe(
        break_df,
        use_container_width=True
    )

    # Compare observed Sup-F statistics with critical values

    fig_break = px.bar(
        break_df,
        x="Dataset",
        y=["Observed_Sup_F", "Critical_Value_95"],
        barmode="group",
        title="Observed Sup-F Statistics vs 95% Bootstrap Critical Values",
        labels={
            "value": "Sup-F Statistic",
            "variable": "Statistic"
        },
        text_auto=".2f"
    )

    fig_break.update_layout(
        template="plotly_dark",
        xaxis_title="Dataset",
        yaxis_title="Sup-F Statistic",
        legend_title="Comparison"
    )

    st.plotly_chart(
        fig_break,
        use_container_width=True
    )

    # Display bootstrap significance results

    st.subheader("Bootstrap Hypothesis Test Results")

    for _, row in break_df.iterrows():

        st.write(f"**Dataset:** {row['Dataset']}")

        p_value = row["Bootstrap_P_Value"]

        st.metric(
            "Bootstrap p-value",
            f"{p_value:.6f}"
        )

        if p_value < 0.05:
            st.success(
                "Statistically significant structural break detected "
                "at the 5% significance level."
            )
        else:
            st.info(
                "Insufficient evidence of a structural break "
                "at the 5% significance level."
            )

else:
    st.warning("Structural break results file not found.")
    
# ---------------------------------------
# SEGMENTED REGRESSION VISUALISATION
# ---------------------------------------

st.divider()

st.subheader("Segmented Regression Analysis")

st.markdown("""
This visualisation illustrates the estimated change in Zambia's
maize production trend around the early 2000s.
""")

segmented_plot = OUTPUTS_PATH / "segmented_regression.png"

if segmented_plot.exists():

    st.image(
        str(segmented_plot),
        caption="Segmented Regression Model — Candidate Breakpoint: 2002",
        use_container_width=True
    )

else:
    st.warning("Segmented regression visualisation was not found.")
    
# ---------------------------------------
# 12. KEY FINDINGS AND INTERPRETATION
# ---------------------------------------

st.divider()

st.subheader("Key Findings and Interpretation")

st.markdown("""
### 1. Historical Production Trends

- Zambia's highest maize production in the dataset was recorded in **2021**,
at approximately 3.62 million tonnes.
- The lowest production was recorded in **1992**, at approximately
483,492 tonnes.
- The long-term linear regression indicates an upward production trend.

### 2. Recent Production Changes

- Maize production declined by approximately **53.67% between 2023 and 2024**.
- Harvested area declined by approximately **51.75%** over the same period.
- Yield declined by approximately **3.98%**.

The larger decline in harvested area suggests that it was the dominant
factor associated with the 2024 production reduction.

### 3. Structural Break Analysis

- The segmented regression identified **2002** as the best-fitting
candidate breakpoint.
- Breakpoint stability analysis suggests that the change occurred
around the early 2000s.
- Bootstrap testing provided statistical evidence of a structural
change in the production trend.

### 4. Statistical Relationships

- Harvested area and maize production have a positive correlation.
- Yield and maize production also have a positive correlation.
- These relationships indicate association, not necessarily causation.
""")

st.info(
    "Interpretation note: The 2024 observation is influential in the "
    "regression analysis. It was retained because it is a valid observation "
    "in the dataset. The estimated structural breakpoint should also be "
    "treated as a statistical finding, not proof of a specific historical cause."
)
    
# ---------------------------------------
# 13. DATA SOURCES AND QUALITY
# ---------------------------------------

st.divider()

st.subheader("Data Sources and Data Quality")

st.markdown("""
### Primary Data Source

**Food and Agriculture Organization (FAO) – FAOSTAT**

The dataset contains Zambia's annual maize production statistics
from 1961 to 2024.

Source: https://www.fao.org/faostat/en/

### Data Preparation

The original FAOSTAT dataset was filtered to include:
- Country: Zambia
- Commodity: Maize (corn)
- Elements: Production, Area harvested and Yield

The data was cleaned and transformed into a structured CSV file
for statistical analysis.

### Understanding Data Flags

FAOSTAT uses observation flags to describe the status of reported values:

| Flag | Meaning |
|---|---|
| A | Official figure |
| E | Estimated value |
| I | Imputed value |
| M | Missing or cannot exist |
| X | Figure from an external organisation |

**Important:** Not every observation in the historical dataset is
an officially reported figure. These flags should be considered when
interpreting the results.
""")

st.markdown("""
### Supplementary Data Source

**Zambia Statistics Agency (ZamStats)**

ZamStats provides agricultural and environmental statistics that
can offer additional context when interpreting Zambia's maize
production trends.

Source: https://www.zamstats.gov.zm/agriculture-and-environment/
""")

# ---------------------------------------
# 12. DOWNLOAD DATA AND RESULTS
# ---------------------------------------

st.divider()

st.subheader("Download Data and Analysis Results")

st.markdown(
    """
    Download the cleaned maize production dataset and statistical
    analysis results for further research.
    """
)

# Download cleaned dataset

st.download_button(
    label="Download Maize Production Dataset",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="maize_production.csv",
    mime="text/csv"
)

# Download statistical results

download_files = {
    "Descriptive Statistics": "descriptive_statistics.csv",
    "Correlation Matrix": "correlation_matrix.csv",
    "Regression Results": "regression_results.csv",
    "Structural Break Results": "structural_break_results.csv"
}

for label, filename in download_files.items():

    file_path = OUTPUTS_PATH / filename

    if file_path.exists():

        with open(file_path, "rb") as file:

            st.download_button(
                label=f"Download {label}",
                data=file.read(),
                file_name=filename,
                mime="text/csv",
                key=filename
            )

    else:
        st.warning(f"{filename} was not found.")
        
# ---------------------------------------
# 14. FOOTER
# ---------------------------------------

st.divider()

st.markdown(
    """
    <div style="text-align: center; color: #888888; padding: 15px;">
        <h4 style="color: #4CAF50;">ICD341 Capstone Project</h4>
        <p>
            Statistical Analysis and Visualization of Maize Production
            in Zambia (1961–2024)
        </p>
        <p>
            Developed by Mwila Singoma using Python, Pandas, Plotly and Streamlit.
        </p>
        <p>Mulungushi University | 2026</p>
        <p>© 2026 CodeCrafterMwila AI Lab</p>
    </div>
    """,
    unsafe_allow_html=True
)