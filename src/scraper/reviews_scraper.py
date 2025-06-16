from google_play_scraper import reviews, Sort, app
import pandas as pd
import time

class ReviewScraper:
    def __init__(self, app_id: str, bank_name: str, source: str = "Google Play"):
        self.app_id = app_id
        self.bank_name = bank_name
        self.source = source
        self.reviews_df = pd.DataFrame()

    def fetch_reviews(self, total_count=400, batch_size=100, sleep_time=1.5):
        result = app(
            app_id=self.app_id,
            lang='en',
            country='us' 
            )
        total_count = result['reviews'] if 'reviews' in result else 400
        print(self.bank_name, total_count)
        all_reviews = []
        continuation_token = None

        while len(all_reviews) < total_count:
            count = min(batch_size, total_count - len(all_reviews))
            result, continuation_token = reviews(
                self.app_id,
                lang='en',
                country='us',
                count=count,
                sort=Sort.NEWEST,
                continuation_token=continuation_token
            )
            all_reviews.extend(result)

            # If there's no more data, break
            if not continuation_token:
                break

            time.sleep(sleep_time)  # be respectful to servers

        self.reviews_df = pd.DataFrame(all_reviews)
        return self.reviews_df

    def save_reviews(self, path: str):
        if self.reviews_df.empty:
            raise ValueError("No reviews to save. Please run fetch_reviews first.")
        self.reviews_df.to_csv(path, index=False)
