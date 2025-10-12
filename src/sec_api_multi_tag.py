import requests
import pandas as pd
import time

CIK = "0000320193"
TAGS = ["Revenues", "NetIncomeLoss", "Assets"]
USER_AGENT = "Santhosh Narayanan (santhosh@example.com)"
headers = {"User-Agent": USER_AGENT}

all_data = pd.DataFrame()

for tag in TAGS:
    print(f"🔍 Fetching {tag} ...")
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK}/us-gaap/{tag}.json"
    r = requests.get(url, headers=headers)
    time.sleep(0.5)

    if r.status_code != 200:
        print(f"⚠️ {tag}: failed ({r.status_code})")
        continue

    j = r.json()
    units = j.get("units", {}).get("USD", [])
    if not units:
        continue

    df = pd.DataFrame(units)[["end", "val"]]
    df.rename(columns={"val": tag}, inplace=True)
    df["end"] = pd.to_datetime(df["end"], errors="coerce")

    if all_data.empty:
        all_data = df
    else:
        all_data = pd.merge(all_data, df, on="end", how="outer")

print(f"\n✅ Final merged dataset: {all_data.shape}")
print(all_data.sort_values("end").head(10))
all_data.to_csv("data/processed/apple_api_sample.csv", index=False)
print("📁 Saved to data/processed/apple_api_sample.csv")