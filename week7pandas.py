import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("data.csv")
    print(df.head())

    # Info about dataset
    print(df.info())

    # Check for missing values
    print("Missing values:\n", df.isnull().sum())

    # Drop rows with missing data
    df = df.dropna()
    print('\nAfter dropping missing values:')
    print(df)

    # Compute basic statistics
    print("\nBasic statistics:\n", df.describe())

    # Group by Position
    grouped = df.groupby("Position")[["Age", "Matches_Played_Past_Season"]].mean()
    print("\nGrouped Means by Position:\n", grouped)

    """ Defenders are, on average, the youngest group at about 20.87 years.
        Forwards (21.37 years) and Goalkeepers (21.27 years) are slightly older.
        Midfielders sit in between (21.05 years)."""

    # Bar Chart - Avg Age by Position
    grouped['Age'].plot(kind='bar', color='yellow')
    plt.title("Average Age by Position")
    plt.ylabel("Average Age")
    plt.xlabel("Position")
    plt.tight_layout()
    plt.show()

    #  Line Chart - Avg Matches Played by Position
    grouped['Matches_Played_Past_Season'].plot(kind='line', marker='o', color='blue')
    plt.title("Average Matches Played by Position")
    plt.ylabel("Average Matches Played (Past Season)")
    plt.xlabel("position")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Histogram of a numerical column to understand its distribution.
    grouped['Age'].plot(kind='hist', bins=10, color='purple', alpha=0.7)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Scatter Plot - Age vs Matches Played
    grouped.plot.scatter(x='Age', y='Matches_Played_Past_Season', color="green", alpha=0.6, edgecolors="black")
    plt.title("Scatter Plot: Age vs Matches Played")
    plt.xlabel("Age")
    plt.ylabel("Matches Played (Past Season)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: The file 'data.csv' was not found.")
except Exception as e:
    print("Error:", e)
