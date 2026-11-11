import pandas as pd
from pathlib import Path

# Define project directories
BASE_DIR = Path(__file__).resolve().parent

RAW_DATA = BASE_DIR / "data" / "raw" / "extracted" / "Production_Crops_Livestock_E_Africa.csv"

OUTPUT_DATA = BASE_DIR / "data" / "maize_production.csv"

# Load the original FAOSTAT dataset
df = pd.read_csv(RAW_DATA)

# Filter records for Zambia's maize production
zambia_maize = df[
    (df["Area"] == "Zambia") &
    (df["Item"] == "Maize (corn)")
].copy()

# Display the selected records
print("Zambia Maize Records:")
print(zambia_maize[["Area", "Item", "Element", "Unit"]])

print("\nTotal records:", len(zambia_maize))

# Convert wide-format data into long format
records = []

for _, row in zambia_maize.iterrows():

    for year in range(1961, 2025):

        records.append({
            "Year": year,
            "Element": row["Element"],
            "Unit": row["Unit"],
            "Value": row[f"Y{year}"],
            "Flag": row[f"Y{year}F"]
        })

# Create a new DataFrame
maize_long = pd.DataFrame(records)

# Display the transformed data
print("\nLong Format Dataset:")
print(maize_long.head(10))

print("\nDataset shape:", maize_long.shape)

# Pivot the values into separate indicator columns
maize_clean = maize_long.pivot(
    index="Year",
    columns="Element",
    values="Value"
).reset_index()

# Rename columns for easier use in Python
maize_clean = maize_clean.rename(columns={
    "Production": "Production_tonnes",
    "Area harvested": "Area_harvested_ha",
    "Yield": "Yield_kg_per_ha"
})

# Convert yield from kg/ha to tonnes/ha
maize_clean["Yield_tonnes_per_ha"] = (
    maize_clean["Yield_kg_per_ha"] / 1000
)

# Display the cleaned structure
print("\nCleaned Dataset:")
print(maize_clean.head())

print("\nDataset shape:", maize_clean.shape)

# Extract data-quality flags into separate columns
maize_flags = maize_long.pivot(
    index="Year",
    columns="Element",
    values="Flag"
).reset_index()

# Rename flag columns
maize_flags = maize_flags.rename(columns={
    "Production": "Production_flag",
    "Area harvested": "Area_harvested_flag",
    "Yield": "Yield_flag"
})

# Merge the flags with the cleaned dataset
maize_clean = pd.merge(
    maize_clean,
    maize_flags,
    on="Year",
    how="left"
)

# Display the dataset with quality flags
print("\nDataset with FAOSTAT Flags:")
print(maize_clean.head())

print("\nMissing values:")
print(maize_clean.isnull().sum())

# Remove unnecessary column index name
maize_clean.columns.name = None

# Sort observations chronologically
maize_clean = maize_clean.sort_values("Year")

# Save the cleaned dataset
maize_clean.to_csv(OUTPUT_DATA, index=False)

# Confirm successful export
print("\nCleaned dataset saved successfully!")
print("File:", OUTPUT_DATA)
print("Final shape:", maize_clean.shape)
print("Year range:", maize_clean["Year"].min(), "-", maize_clean["Year"].max())

# Display data-quality flag frequencies
print("\nProduction flag distribution:")
print(maize_clean["Production_flag"].value_counts())