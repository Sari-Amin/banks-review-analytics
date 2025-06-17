import pandas as pd

class Preprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean(self):
        self.df = self.df.drop_duplicates(subset="content")
        self.df["at"] = pd.to_datetime(self.df["at"]).dt.date
        self.df.rename(columns={"content": "review", "score": "rating", "at": "date"}, inplace=True)
        return self.df[["review", "rating", "date"]]
