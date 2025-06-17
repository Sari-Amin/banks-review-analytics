import pandas as pd
from oracle.db_oracle import OracleDatabaseManager

INPUT_DIR = "data/processed_themes/"
BANKS = ["CBE", "BOA", "Dashen"]

def main():
    db = OracleDatabaseManager()

    for bank in BANKS:
        print(f"Inserting: {bank}")
        df = pd.read_csv(f"{INPUT_DIR}{bank.lower()}_themes.csv")
        db.insert_bank(bank)
        bank_id = db.get_bank_id(bank)

        rows = []

        for _, row in df.iterrows():

            rows.append((
                bank_id,
                row["review"],
                int(row["rating"]),
                row["date"],
                row["source"],
                row["sentiment_label"],
                float(row["sentiment_score"]) if pd.notna(row["sentiment_score"]) else 0.0,
                row['keywords'] if pd.notna(row['keywords']) else ""
            ))

        db.insert_reviews(rows)

    db.close()

if __name__ == "__main__":
    main()
