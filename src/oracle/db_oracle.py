import oracledb
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from config import DB_CONFIG

class OracleDatabaseManager:
    def __init__(self):
        self.conn = oracledb.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    def insert_bank(self, bank_name):
        self.cursor.execute("""
            MERGE INTO banks b USING (SELECT :name AS name FROM dual) src
            ON (b.name = src.name)
            WHEN NOT MATCHED THEN INSERT (name) VALUES (:name)
        """, [bank_name, bank_name])
        self.conn.commit()

    def get_bank_id(self, bank_name):
        self.cursor.execute("SELECT id FROM banks WHERE name = :name", [bank_name])
        return self.cursor.fetchone()[0]

    def insert_reviews(self, review_rows):
        for row in review_rows:
            try:
                self.cursor.execute("""
                                        INSERT INTO reviews (
                                        bank_id, review, rating, review_date, source, 
                                        sentiment_label, sentiment_score, keywords) 
                                        VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8)
                                        """, row)
            except Exception as e:
                print(row[7])

                print(f"can't insert this row! {row} due to {e}")
            
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
