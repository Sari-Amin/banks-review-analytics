from src.scraper.reviews_scraper import ReviewScraper
from preprocessing.preprocessor import Preprocessor

def main():
    
    banks = {
        "CBE" : "com.combanketh.mobilebanking",
        "BOA" : "com.boa.boaMobileBanking",
        "Dashen" : "com.dashen.dashensuperapp"
    }

    for name, id in banks.items():
        scraper = ReviewScraper(app_id=id, bank_name=name)
        raw_df = scraper.fetch_reviews()
        scraper.save_reviews(f"data/raw/{name}_reviews.csv")

        preprocessor = Preprocessor(raw_df)
        clean_df = preprocessor.clean()
        clean_df["bank"] = name
        clean_df["source"] = "Google Play"
        clean_df.to_csv(f"data/processed/{name}_reviews_clean.csv", index=False)




if __name__ == "__main__":
    main()
