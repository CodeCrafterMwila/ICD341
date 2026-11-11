import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure the dashboard page
st.set_page_config(
    page_title="Zambia Maize Production Dashboard",
    page_icon="🌽",
    layout="wide"
)

# Dashboard title
st.title("🌽 Zambia Maize Production Dashboard")

# Dashboard introduction
st.write(
    "This interactive dashboard analyses maize production "
    "across selected districts in Zambia."
)

# Add a divider
st.divider()

# Create maize production dataset
data = {
    "District": ["Lusaka", "Chongwe", "Kabwe", "Chipata", "Mumbwa"],
    "Production": [500, 350, 450, 600, 400]
}

# Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the dataset
st.subheader("Maize Production Data")
st.dataframe(df)

# Calculate statistical summaries
total_production = df["Production"].sum()
average_production = df["Production"].mean()

# Display summary metrics
st.subheader("Production Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Total Maize Production",
        value=f"{total_production} tonnes"
    )

with col2:
    st.metric(
        label="Average Production",
        value=f"{average_production:.1f} tonnes"
    )
    
# Display production comparison chart
st.subheader("Maize Production by District")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["District"], df["Production"])

ax.set_xlabel("District")
ax.set_ylabel("Production (tonnes)")
ax.set_title("Maize Production Comparison Across Districts")

plt.xticks(rotation=30)

# Display chart in Streamlit
st.pyplot(fig)

plt.close(fig)

# Interactive district selection
st.subheader("Explore Individual Districts")

selected_district = st.selectbox(
    "Choose a district:",
    df["District"]
)

# Filter data for the selected district
result = df[df["District"] == selected_district]

# Display selected district information
st.write("Selected District:", selected_district)

st.success(
    f"Maize Production: {result['Production'].iloc[0]} tonnes"
)