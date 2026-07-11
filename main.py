from src.data_loader import load_data
from src.data_cleaning import inspect_data, clean_data
from src.analysis import summary_statistics
from src.analysis import top_selling_games
from src.visualization import plot_top_selling_games
from src.analysis import top_platforms
from src.visualization import plot_top_platforms


def main():
    df = load_data("data/video_games_sales.csv")
    inspect_data(df)
    df = clean_data(df)
    inspect_data(df)

    #print(summary_statistics(df))

    #print(top_selling_games(df))

    #plot_top_selling_games(top_selling_games(df))

    print(top_platforms(df))

    plot_top_platforms(top_platforms(df))

if __name__ == "__main__":
    main()