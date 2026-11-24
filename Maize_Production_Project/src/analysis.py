import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "outputs"


def load_data():
    """Load maize production data from the CSV file."""

    file_path = DATA_DIR / "maize_data.csv"

    df = pd.read_csv(file_path)

    return df


def analyse_data(df):
    """Calculate descriptive statistics for maize production."""

    print("\nMAIZE PRODUCTION STATISTICS")
    print("")

    print("Mean:", df["Maize_Production"].mean())
    print("Standard Deviation:", df["Maize_Production"].std())
    print("Minimum:", df["Maize_Production"].min())
    print("Maximum:", df["Maize_Production"].max())

    print("\nComplete Statistical Summary:")
    print(df.describe())


def create_histogram(df):
    """Generate and save a maize production histogram."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Maize_Production"],
        bins=15,
        edgecolor="black"
    )

    plt.title("Maize Production Distribution")
    plt.xlabel("Production (tonnes)")
    plt.ylabel("Frequency")

    plt.tight_layout()

    output_file = OUTPUT_DIR / "maize_histogram.png"

    plt.savefig(output_file, dpi=300)

    plt.show()
    plt.close()

    print("\nHistogram saved to:", output_file)


def main():
    """Run the complete maize production analysis."""

    df = load_data()

    analyse_data(df)

    create_histogram(df)


if __name__ == "__main__":
    main()