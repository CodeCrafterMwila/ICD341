import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Zambia Maize Production Dashboard",
    page_icon="🌽",
    layout="wide"
)

# --------------------------------------------------
# 2. DASHBOARD HEADER
# --------------------------------------------------

st.title("🌽 Zambia Maize Production Dashboard")

st.write(
    "An interactive dashboard exploring maize production "
    "across selected districts in Zambia."
)

st.warning(
    "Note: This dashboard uses illustrative sample data "
    "for educational purposes. The figures are not official "
    "maize production statistics."
)

st.divider()

# --------------------------------------------------
# 3. DATA PREPARATION
# --------------------------------------------------

data = {
    "District": ["Lusaka", "Chongwe", "Kabwe", "Chipata", "Mumbwa"],
    "Production": [500, 350, 450, 600, 400]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 4. INTERACTIVE FILTER
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

minimum_production = st.sidebar.slider(
    "Minimum production (tonnes)",
    min_value=0,
    max_value=int(df["Production"].max()),
    value=0,
    step=50
)

filtered_df = df[
    df["Production"] >= minimum_production
]

st.subheader("Maize Production Data")

st.dataframe(filtered_df, use_container_width=True)

st.write(
    f"Showing {len(filtered_df)} of {len(df)} districts."
)

# --------------------------------------------------
# 5. STATISTICAL SUMMARY
# --------------------------------------------------

st.subheader("Production Statistics")

if not filtered_df.empty:

    total_production = filtered_df["Production"].sum()
    average_production = filtered_df["Production"].mean()
    highest_production = filtered_df["Production"].max()
    lowest_production = filtered_df["Production"].min()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Production",
        f"{total_production} tonnes"
    )

    col2.metric(
        "Average Production",
        f"{average_production:.1f} tonnes"
    )

    col3.metric(
        "Highest Production",
        f"{highest_production} tonnes"
    )

    col4.metric(
        "Lowest Production",
        f"{lowest_production} tonnes"
    )

    # --------------------------------------------------
    # 6. PRODUCTION VISUALIZATION
    # --------------------------------------------------

    st.subheader("Maize Production by District")

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(
        filtered_df["District"],
        filtered_df["Production"]
    )

    ax.set_xlabel("District")
    ax.set_ylabel("Production (tonnes)")
    ax.set_title("Maize Production Comparison")

    ax.bar_label(bars, padding=3)

    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    # --------------------------------------------------
    # 7. DISTRICT EXPLORATION
    # --------------------------------------------------

    st.subheader("Explore Individual Districts")

    selected_district = st.selectbox(
        "Choose a district:",
        filtered_df["District"].tolist()
    )

    result = filtered_df[
        filtered_df["District"] == selected_district
    ]

    production = result["Production"].iloc[0]

    st.success(
        f"{selected_district} recorded "
        f"{production} tonnes in the sample dataset."
    )

    # --------------------------------------------------
    # 8. DOWNLOAD DATA
    # --------------------------------------------------

    csv_data = filtered_df.to_csv(index=False)

    st.download_button(
        label="Download Data as CSV",
        data=csv_data,
        file_name="maize_production.csv",
        mime="text/csv"
    )

else:
    st.info(
        "No districts match the selected production filter."
    )

# --------------------------------------------------
# 9. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "ICD341 Advanced Statistical Computing | "
    "Interactive Dashboard Exercise"
)