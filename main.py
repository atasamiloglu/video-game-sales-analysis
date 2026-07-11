from src.data_loader import load_data
from src.data_cleaning import inspect_data, clean_data
from src.analysis import summary_statistics,top_selling_games, top_platforms, top_genres
from src.visualization import plot_top_genres, plot_top_selling_games, plot_top_platforms

def main():
    df = load_data("data/video_games_sales.csv")
    inspect_data(df)
    df = clean_data(df)
    inspect_data(df)

    #print(summary_statistics(df))

    #print(top_selling_games(df))

    #plot_top_selling_games(top_selling_games(df))

    #print(top_platforms(df))

    #plot_top_platforms(top_platforms(df))

    print(top_genres(df))
    
    plot_top_genres(top_genres(df))

if __name__ == "__main__":
    main()