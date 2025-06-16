from src.scraper.reviews_scraper import ReviewScraper
from preprocessing.preprocessor import Preprocessor

def main():
    #commercial bank of ethiopia
    scraper = ReviewScraper(app_id="com.combanketh.mobilebanking", bank_name="CBE")
    raw_df = scraper.fetch_reviews()
    scraper.save_reviews("data/raw/cbe_reviews.csv")

    preprocessor = Preprocessor(raw_df)
    clean_df = preprocessor.clean()
    clean_df["bank"] = "CBE"
    clean_df["source"] = "Google Play"
    clean_df.to_csv("data/processed/cbe_reviews_clean.csv", index=False)


    #bank of abysinia
    scraper_boa = ReviewScraper(app_id="com.boa.boaMobileBanking", bank_name="BOA")
    raw_df = scraper_boa.fetch_reviews()
    scraper_boa.save_reviews("data/raw/boa_reviews.csv")

    preprocessor_boa = Preprocessor(raw_df)
    clean_df = preprocessor_boa.clean()
    clean_df["bank"] = "BOA"
    clean_df["source"] = "Google Play"
    clean_df.to_csv("data/processed/boa_reviews_clean.csv", index=False)

    #dashen bank
    scraper_dashen = ReviewScraper(app_id="com.dashen.dashensuperapp", bank_name="Dashen")
    raw_df = scraper_dashen.fetch_reviews()
    scraper_dashen.save_reviews("data/raw/dashen_reviews.csv")

    preprocessor_dashen = Preprocessor(raw_df)
    clean_df = preprocessor_dashen.clean()
    clean_df["bank"] = "Dashen"
    clean_df["source"] = "Google Play"
    clean_df.to_csv("data/processed/dashen_reviews_clean.csv", index=False)

if __name__ == "__main__":
    main()
