import requests
import pandas as pd
import os
import time
import glob

# === SETTINGS ===
CIK = "0000320193"  # Apple Inc.
USER_AGENT = "Santhosh Narayanan (santhosh.nb02@gmail.com)"  # Replace with your email
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
CONFIG_PATH = "data/config/apple_selected_tags.txt"

# === Ensure directories exist ===
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# === LOAD TAGS FROM CONFIG FILE ===
with open(CONFIG_PATH, "r") as f:
    TAGS = [line.strip() for line in f.readlines() if line.strip()]

print(f"✅ Loaded {len(TAGS)} tags from {CONFIG_PATH}")

# === FUNCTION: Fetch company concept (one tag) ===
def fetch_company_concept(cik, tag, user_agent, retries=3):
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{tag}.json"
    headers = {"User-Agent": user_agent}
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=20)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                wait = 5 * (attempt + 1)
                print(f"⏳ Rate-limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"⚠️  {tag}: {response.status_code} — skipping.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"⚠️  Error fetching {tag}: {e}")
            time.sleep(2)
    return None

# === FUNCTION: Process JSON into DataFrame ===
def parse_json_to_df(json_data, tag):
    if not json_data or "units" not in json_data:
        return pd.DataFrame()
    units = json_data["units"].get("USD", [])
    if len(units) == 0:
        return pd.DataFrame()
    df = pd.DataFrame(units)[["end", "val"]]
    df.rename(columns={"val": tag}, inplace=True)
    df["end"] = pd.to_datetime(df["end"], errors="coerce")
    return df

# === MAIN EXECUTION ===
def main():
    for i, tag in enumerate(TAGS, 1):
        output_path = f"{PROCESSED_DIR}/apple_{tag}.csv"
        if os.path.exists(output_path):
            print(f"✅ Skipping {tag}, already exists.")
            continue

        print(f"🔍 [{i}/{len(TAGS)}] Fetching {tag} ...")
        json_data = fetch_company_concept(CIK, tag, USER_AGENT)
        time.sleep(1.5)

        if json_data:
            df = parse_json_to_df(json_data, tag)
            if not df.empty:
                df.to_csv(output_path, index=False)
                print(f"💾 Saved {tag} → {output_path} ({len(df)} rows)")
            else:
                print(f"⚠️ {tag} returned no USD data.")
        else:
            print(f"❌ {tag} not found or failed.")

    merge_tag_files()


# === SAFE MERGE FUNCTION ===
def merge_tag_files():
    print("\n🔄 Combining all tag CSVs (safe streaming merge)...")
    files = glob.glob(os.path.join(PROCESSED_DIR, "apple_*.csv"))
    files = [f for f in files if not f.endswith("apple_api_financials_combined.csv")]

    if not files:
        print("⚠️ No tag files found to merge.")
        return

    base_df = pd.read_csv(files[0])
    for file in files[1:]:
        try:
            df = pd.read_csv(file)
            if "end" not in df.columns:
                continue
            base_df = pd.merge(base_df, df, on="end", how="outer")
            base_df.to_csv(f"{PROCESSED_DIR}/apple_api_financials_combined.csv", index=False)
            print(f"✅ Merged {os.path.basename(file)}")
        except Exception as e:
            print(f"⚠️ Failed to merge {file}: {e}")
            continue

    base_df = base_df.sort_values("end").drop_duplicates("end")
    final_csv = f"{PROCESSED_DIR}/apple_api_financials_combined.csv"
    final_json = f"{RAW_DIR}/apple_api_data.json"
    base_df.to_csv(final_csv, index=False)
    base_df.to_json(final_json, orient="records", indent=2)

    print(f"\n✅ Final combined dataset saved → {final_csv}")
    print(f"📊 Rows: {len(base_df)} | Columns: {len(base_df.columns)}")

if __name__ == "__main__":
    main()