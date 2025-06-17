from nlp.sentiment_analyzer import SentimentAnalyzer
import pandas as pd


BANKS = ["CBE", "BOA", "Dashen"]

def main():
    analyzer = SentimentAnalyzer()

    for bank in BANKS:
        print(f"\nProcessing {bank}...")
        df = pd.read_csv(f"data/processed/{bank.lower()}_reviews_clean.csv")
        df_sent = analyzer.analyze_sentiment(df)
        df_sent.to_csv(f"data/processed_sentiment/{bank.lower()}_sentiment.csv", index=False)

if __name__ == "__main__":
    main()
