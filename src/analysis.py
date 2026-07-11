import pandas as pd

def summary_statistics(df):
    return df.describe()

def top_selling_games(df):
    top_games = df[["Name", "Global_Sales"]].sort_values(
        by="Global_Sales",
        ascending=False
    ).head(10)

def top_platforms(df):
    top_platforms = (
        df.groupby("Platform")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return top_platforms

    return top_games
