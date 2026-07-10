from src.data_loader import load_data
from src.data_cleaning import inspect_data, clean_data
from src.analysis import summary_statistics


def main():
    df = load_data("data/video_games_sales.csv")
    inspect_data(df)
    df = clean_data(df)
    inspect_data(df)
    
    print(summary_statistics(df))


if __name__ == "__main__":
    main()