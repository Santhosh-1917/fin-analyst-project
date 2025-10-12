import requests
import json

# === SETTINGS ===
CIK = "0000320193"  # Apple Inc.
TAG = "Revenues"    # test tag
URL = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK}/us-gaap/{TAG}.json"
HEADERS = {"User-Agent": "Santhosh Narayanan (santhosh.nb02@gmail.com)"}

print(f"🔍 Requesting: {URL}")
response = requests.get(URL, headers=HEADERS)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"✅ Successfully fetched '{TAG}' data for Apple.")
    print(f"Available units: {list(data['units'].keys())[:5]}")
    
    # show small preview of the numeric data
    usd_data = data['units'].get('USD', [])
    print(f"\n🔹 Sample entries (first 3):")
    print(json.dumps(usd_data[:3], indent=2))
else:
    print("❌ Failed to fetch data.")
    print(response.text)