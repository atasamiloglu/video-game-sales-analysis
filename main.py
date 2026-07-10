from src.data_loader import load_data
from src.data_cleaning import inspect_data, clean_data


def main():
    df = load_data("data/video_games_sales.csv")
    inspect_data(df)
    df = clean_data(df)
    inspect_data(df)


if __name__ == "__main__":
    main()