import matplotlib.pyplot as plt
import seaborn as sns


def plot_class_distribution(df, column="queue"):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    df[column].value_counts().sort_values().plot(
        kind="barh", color=sns.color_palette("viridis")
    )
    plt.title("Class Distribution", fontsize=16)
    plt.ylabel("Queue", fontsize=12)
    plt.xlabel("Count", fontsize=12)
    plt.tight_layout()
    plt.show()
