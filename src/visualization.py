import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (10, 6)

def plot_top_selling_games(top_games):

    plt.figure(figsize=(10, 6))

    plt.bar(top_games["Name"], top_games["Global_Sales"])

    plt.title("Top 10 Best-Selling Video Games")
    plt.xlabel("Game")
    plt.ylabel("Global Sales (Millions)")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("images/top_10_best_selling_games.png")

    plt.show()

def plot_top_platforms(platforms):

    plt.figure(figsize=(10, 6))

    plt.barh(platforms.index, platforms.values)

    plt.title("Top 10 Platforms by Global Sales")
    plt.xlabel("Global Sales (Millions)")
    plt.ylabel("Platform")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("images/top_10_platforms.png")

    plt.show()

def plot_top_genres(genres):

    plt.figure(figsize=(10, 6))

    plt.barh(genres.index, genres.values)

    plt.title("Global Sales by Genre")
    plt.xlabel("Global Sales (Millions)")
    plt.ylabel("Genre")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("images/global_sales_by_genre.png")

    plt.show()    

def plot_top_publishers(publishers):
    plt.figure(figsize=(10, 6))

    plt.barh(publishers.index, publishers.values)

    plt.title("Top 10 Publishers by Global Sales")
    plt.xlabel("Global Sales (Millions)")
    plt.ylabel("Publisher")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("images/top_10_publishers.png")

    plt.show()

def plot_games_by_year(games):
    plt.figure(figsize=(10, 6))

    plt.plot(games.index, games.values, marker="o")

    plt.title("Number of Games Released by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Games")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("images/games_released_by_year.png")

    plt.show()

def plot_global_sales_by_year(sales):
    plt.figure(figsize=(10, 6))

    plt.plot(sales.index, sales.values, marker="o")

    plt.title("Global Video Game Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Global Sales (Millions)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("images/global_sales_by_year.png")

    plt.show()

def plot_correlation_heatmap(corr):
    plt.figure(figsize=(10, 8))

    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")

    plt.colorbar(label="Correlation")

    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("images/correlation_heatmap.png")

    plt.show()             
