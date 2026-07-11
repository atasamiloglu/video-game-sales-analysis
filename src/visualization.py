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