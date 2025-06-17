from eda.visualizer import InsightsVisualizer

BANKS = {
    "CBE": "data/processed_themes/cbe_themes.csv",
    "BOA": "data/processed_themes/boa_themes.csv",
    "Dashen": "data/processed_themes/dashen_themes.csv"
}

def main():
    for bank, path in BANKS.items():
        viz = InsightsVisualizer(bank_name=bank, data_path=path)
        viz.run_all()

if __name__ == "__main__":
    main()
