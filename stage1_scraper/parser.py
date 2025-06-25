import json
import pandas as pd
from pathlib import Path

RAW_FILE = Path(__file__).parent / "raw_outputs.json"
JSON_OUT = Path(__file__).parent / "results.json"
CSV_OUT = Path(__file__).parent / "results.csv"

brands = ["Nike", "Adidas", "Hoka", "New Balance", "Jordan"]

def count_mentions(text, brand):
    # Case-insensitive match of whole word
    return text.lower().split().count(brand.lower())

def main():
    with open(RAW_FILE, "r") as f:
        data = json.load(f)

    results = []
    for entry in data:
        prompt = entry["prompt"]
        response = entry["response"]
        result = {"prompt": prompt}
        for brand in brands:
            result[brand] = count_mentions(response, brand)
        results.append(result)

    with open(JSON_OUT, "w") as f:
        json.dump(results, f, indent=2)

    df = pd.DataFrame(results)
    df.to_csv(CSV_OUT, index=False)

    print(f"Parsed {len(results)} responses. Saved to:\n- {JSON_OUT}\n- {CSV_OUT}")

if __name__ == "__main__":
    main()