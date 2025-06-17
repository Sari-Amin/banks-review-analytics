from transformers import pipeline
import pandas as pd
from tqdm import tqdm

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        print("Loading model...")
        self.model = pipeline("sentiment-analysis", model=model_name)

    def analyze_sentiment(self, df: pd.DataFrame, text_col: str = "review") -> pd.DataFrame:
        sentiments = []
        scores = []
        tqdm.pandas(desc="Analyzing Sentiment")
        results = df[text_col].progress_apply(lambda x: self.model(x)[0])

        for r in results:
            sentiments.append(r['label'].lower())  # 'POSITIVE' -> 'positive'
            scores.append(r['score'])

        df["sentiment_label"] = sentiments
        df["sentiment_score"] = scores
        return df
