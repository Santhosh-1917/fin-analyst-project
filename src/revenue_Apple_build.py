import json
import pandas as pd

# Paths
RAW_JSON_PATH = "data/raw/apple_companyfacts.json"
OUTPUT_CSV_PATH = "data/processed/apple_revenue_tags.csv"

# Revenue-related tags to extract
revenue_tags = [
    'RevenueFromContractWithCustomerExcludingAssessedTax',
    'Revenues',
    'SalesRevenueNet',
    'SalesRevenueServicesGross',
    'ContractWithCustomerLiabilityRevenueRecognized',
    'DeferredRevenueCurrent',
    'DeferredRevenueNoncurrent',
    'IncreaseDecreaseInDeferredRevenue'
]

# Load JSON
with open(RAW_JSON_PATH, 'r') as f:
    company_facts = json.load(f)

facts = company_facts.get("facts", {}).get("us-gaap", {})
df_main = pd.DataFrame()

# Extract each tag’s time series
for tag in revenue_tags:
    if tag in facts:
        units = facts[tag]["units"]
        # pick USD if available, otherwise just first unit
        unit_key = "USD" if "USD" in units else list(units.keys())[0]
        tag_data = pd.DataFrame(units[unit_key])
        tag_data = tag_data[['end', 'val']].rename(columns={'val': tag})
        tag_data['end'] = pd.to_datetime(tag_data['end'])
        df_main = pd.merge(df_main, tag_data, on='end', how='outer') if not df_main.empty else tag_data
        print(f"✅ Extracted {tag} ({len(tag_data)} records)")
    else:
        print(f"⚠️ Tag not found in JSON: {tag}")

# Sort chronologically
df_main = df_main.sort_values('end').reset_index(drop=True)

# Save to CSV
df_main.to_csv(OUTPUT_CSV_PATH, index=False)
print(f"\n💾 Saved revenue tags dataset to: {OUTPUT_CSV_PATH}")
print(f"📊 Final shape: {df_main.shape}")