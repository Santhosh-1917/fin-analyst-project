import json
import pandas as pd
from pathlib import Path

# ---------- Paths ----------
RAW_JSON_PATH = Path("data/raw/apple_companyfacts.json")      # original Apple JSON file
TAG_FILE_PATH = Path("data/config/apple_selected_tags.txt")    # selected tags list
OUTPUT_CSV_PATH = Path("data/processed/apple_selected_financials.csv")  # final dataset

# ---------- Load Selected Tags ----------
def load_selected_tags(filepath: Path):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]

# ---------- Load JSON ----------
def load_company_facts(json_path: Path):
    with open(json_path, "r") as f:
        return json.load(f)

# ---------- Extract Data ----------
def extract_facts(data, tags):
    records = []

    # Focus on US-GAAP taxonomy (most financial tags are here)
    facts = data.get("facts", {}).get("us-gaap", {})

    for tag in tags:
        if tag not in facts:
            print(f"⚠️ Tag not found: {tag}")
            continue

        for unit, details in facts[tag].get("units", {}).items():
            for fact in details:
                end_date = fact.get("end")
                val = fact.get("val")
                if end_date and val is not None:
                    records.append({
                        "end": end_date,
                        "tag": tag,
                        "unit": unit,
                        "val": val
                    })

    return pd.DataFrame(records)

# ---------- Pivot ----------
def pivot_dataframe(df):
    # Convert end date to datetime and keep latest per period/tag if duplicates
    df["end"] = pd.to_datetime(df["end"], errors="coerce")
    df = df.sort_values(["end"]).drop_duplicates(subset=["end", "tag"], keep="last")

    # Pivot: rows = date, columns = tags, values = val
    pivot_df = df.pivot(index="end", columns="tag", values="val")
    pivot_df = pivot_df.sort_index()
    return pivot_df

# ---------- Main ----------
def main():
    print("🚀 Building financial dataset from selected tags...")

    tags = load_selected_tags(TAG_FILE_PATH)
    print(f"✅ Loaded {len(tags)} selected tags.")

    data = load_company_facts(RAW_JSON_PATH)
    df = extract_facts(data, tags)

    if df.empty:
        print("❌ No data extracted. Check tags or JSON file.")
        return

    final_df = pivot_dataframe(df)
    OUTPUT_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(OUTPUT_CSV_PATH)

    print(f"📊 Final dataset shape: {final_df.shape}")
    print(f"✅ Saved CSV to {OUTPUT_CSV_PATH}")

if __name__ == "__main__":
    main()