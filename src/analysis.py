import pandas as pd

def summary_statistics(df):
    return df.describe()

def top_selling_games(df):
    top_games = df[["Name", "Global_Sales"]].sort_values(
        by="Global_Sales",
        ascending=False
    ).head(10)

    return top_games

def top_platforms(df):
    top_platforms = (
        df.groupby("Platform")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return top_platforms

def top_genres(df):
    genres = (
        df.groupby("Genre")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return genres

def top_publishers(df):
    publishers = (
        df.groupby("Publisher")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return publishers

def games_by_year(df):
    games = (
        df.groupby("Year")
        .size()
        .sort_index()
    )

    return games
    
