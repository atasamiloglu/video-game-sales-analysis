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