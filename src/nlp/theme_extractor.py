import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import re

class ThemeExtractor:
    def __init__(self, max_features=100, ngram_range=(1, 2)):
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english", ngram_range=ngram_range)

    def clean_text(self, text):
        text = re.sub(r"[^a-zA-Z0-9\s]", "", str(text).lower())
        return text

    def extract_keywords(self, df: pd.DataFrame, text_col: str = "review") -> pd.DataFrame:
        df["clean_review"] = df[text_col].apply(self.clean_text)
        tfidf_matrix = self.vectorizer.fit_transform(df["clean_review"])
        feature_names = self.vectorizer.get_feature_names_out()

        # Get top TF-IDF terms for each review
        keywords = []
        for row in tfidf_matrix:
            row_data = row.toarray()[0]
            top_indices = row_data.argsort()[-3:][::-1]  # top 3 keywords
            top_keywords = [feature_names[i] for i in top_indices if row_data[i] > 0]
            keywords.append(", ".join(top_keywords))
        
        df["keywords"] = keywords
        return df

    def suggest_themes(self, df: pd.DataFrame) -> list:
        # Simple rule-based grouping based on frequent terms
        all_keywords = " ".join(df["keywords"].dropna().values).split(", ")
        freq = pd.Series(all_keywords).value_counts()

        themes = {
            "Login Issues": ["login", "password", "signin", "pin"],
            "Performance & Speed": ["slow", "delay", "loading", "hang", "lag"],
            "Transaction Errors": ["transfer", "payment", "fail", "error", "crash"],
            "UX & Interface": ["interface", "design", "ui", "easy"],
            "Customer Support": ["help", "support", "response", "service"]
        }

        theme_counts = {theme: 0 for theme in themes}
        for keyword in freq.index:
            for theme, terms in themes.items():
                if any(t in keyword for t in terms):
                    theme_counts[theme] += freq[keyword]

        # Return top 3–5 themes
        return sorted(theme_counts.items(), key=lambda x: -x[1])[:5]
