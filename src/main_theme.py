from nlp.theme_extractor import ThemeExtractor
import pandas as pd
import os

INPUT_DIR = "data/processed_sentiment/"
OUTPUT_DIR = "data/processed_themes/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BANKS = ["CBE", "BOA", "Dashen"]

def main():
    extractor = ThemeExtractor()

    for bank in BANKS:
        print(f"\nExtracting themes for {bank}")
        df = pd.read_csv(f"{INPUT_DIR}{bank.lower()}_sentiment.csv")
        df = extractor.extract_keywords(df)
        themes = extractor.suggest_themes(df)

        df.to_csv(f"{OUTPUT_DIR}{bank.lower()}_themes.csv", index=False)
        print("Top themes:")
        for t, count in themes:
            print(f"  - {t}: {count} mentions")

if __name__ == "__main__":
    main()
