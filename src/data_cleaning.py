import pandas as pd
import numpy as np

def inspect_data(df):
    print("=" * 50)
    print("Dataset Overview")
    print("=" * 50)

    print(f"Shape: {df.shape}\n")

    print("Columns:")
    print(df.columns.tolist(), "\n")

    print("Data Types:")
    print(df.dtypes, "\n")

    print("Missing Values:")
    print(df.isnull().sum(), "\n")

    print(f"Duplicate Rows: {df.duplicated().sum()}")

def clean_data(df):
    df = df.dropna()

    df["Year"] = df["Year"].astype(int)

    return df    