# Customer Churn Analysis - EDA and Data Cleaning

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_churn_raw.csv")

print("Dataset loaded successfully!\n")

# Basic info
print("Shape of the dataset:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Convert data types
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Convert Churn Yes/No to 1/0
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# Fill missing values
df["TotalCharges"].fillna(
    df["TotalCharges"].mean(),
    inplace=True
)

# Drop duplicates
df.drop_duplicates(inplace=True)

print("\nData cleaning completed successfully!")

print("\nFinal shape of dataset:")
print(df.shape)