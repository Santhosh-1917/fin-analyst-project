# src/parse_apple.py
import json
import pandas as pd
import os

# Load the Apple JSON file
file_path = "data/raw/apple_companyfacts.json"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Apple JSON not found at {file_path}")

with open(file_path) as f:
    data = json.load(f)

print(f"✅ Loaded Apple JSON for {data.get('entityName')}")

# Helper to extract time series data for a given US GAAP tag
def extract_facts(tag):
    try:
        facts = data['facts']['us-gaap'][tag]['units']['USD']
        df = pd.DataFrame(facts)
        df['tag'] = tag
        return df[['end', 'val', 'tag']]
    except KeyError:
        print(f"⚠️ Tag {tag} not found")
        return pd.DataFrame(columns=['end', 'val', 'tag'])

# Common financial metrics to extract
tags = ["Revenues", "NetIncomeLoss", "EarningsPerShareBasic"]

frames = [extract_facts(tag) for tag in tags]
combined_df = pd.concat(frames, ignore_index=True)

# Clean and sort
combined_df['end'] = pd.to_datetime(combined_df['end'])
combined_df = combined_df.sort_values(['tag', 'end'])

# Save processed CSV
os.makedirs("data/processed", exist_ok=True)
csv_path = "data/processed/apple_financials.csv"
combined_df.to_csv(csv_path, index=False)

print(f"📊 Extracted {len(combined_df)} data points")
print(f"✅ Saved processed CSV to {csv_path}")
print(combined_df.head(10))