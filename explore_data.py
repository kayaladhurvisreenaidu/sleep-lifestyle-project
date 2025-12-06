import pandas as pd

# Load dataset
df = pd.read_csv("data/Sleep_Health_and_Lifestyle_Dataset.csv")

# Show first few rows
print("First 5 rows:")
print(df.head())

# Show basic info
print("\nDataset Info:")
print(df.info())

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))
