import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

class InsightsVisualizer:
    def __init__(self, bank_name, data_path, output_dir="../figures/"):
        self.bank_name = bank_name
        self.data_path = data_path
        self.output_dir = output_dir
        self.df = pd.read_csv(data_path)

        os.makedirs(output_dir, exist_ok=True)

    def plot_sentiment_distribution(self):
        plt.figure(figsize=(6,4))
        sns.countplot(x='sentiment_label', data=self.df, order=["positive", "neutral", "negative"])
        plt.title(f"{self.bank_name} - Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Review Count")
        path = f"{self.output_dir}{self.bank_name.lower()}_sentiment_distribution.png"
        plt.tight_layout()
        plt.savefig(path)
        plt.show()

    def plot_ratings_sentiment_hist(self):
        plt.figure(figsize=(6,4))
        sns.histplot(data=self.df, x="rating", hue="sentiment_label", multiple="stack", bins=5)
        plt.title(f"{self.bank_name} - Ratings vs Sentiment")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        path = f"{self.output_dir}{self.bank_name.lower()}_ratings_sentiment.png"
        plt.tight_layout()
        plt.savefig(path)
        plt.show()

    def plot_sentiment_heatmap(self):
        heat_data = self.df.groupby(["rating", "sentiment_label"]).size().unstack().fillna(0)
        heat_data = heat_data.reindex(index=[1, 2, 3, 4, 5])  # ensure row order

        plt.figure(figsize=(8, 5))
        sns.heatmap(heat_data, annot=True, fmt='g', cmap="YlGnBu")
        plt.title(f"{self.bank_name} - Sentiment by Rating Heatmap")
        plt.xlabel("Sentiment")
        plt.ylabel("Rating")
        path = f"{self.output_dir}{self.bank_name.lower()}_sentiment_heatmap.png"
        plt.tight_layout()
        plt.savefig(path)
        plt.show()

    def plot_wordcloud(self):
        keywords = " ".join(self.df["keywords"].dropna())
        wc = WordCloud(width=800, height=400, background_color="white").generate(keywords)

        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title(f"{self.bank_name} - Keyword WordCloud")
        path = f"{self.output_dir}{self.bank_name.lower()}_wordcloud.png"
        plt.tight_layout()
        plt.savefig(path)
        plt.show()

    def run_all(self):
        self.plot_sentiment_distribution()
        self.plot_ratings_sentiment_hist()
        self.plot_sentiment_heatmap()
        self.plot_wordcloud()
        print(f"Plots saved for {self.bank_name}")
