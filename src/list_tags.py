# src/list_tags.py
import json
import os

file_path = "data/raw/apple_companyfacts.json"

# ✅ 1️⃣ Check file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found: {file_path}")

# ✅ 2️⃣ Load JSON
with open(file_path) as f:
    data = json.load(f)

print(f"✅ Loaded JSON for {data.get('entityName')}")

# ✅ 3️⃣ Extract all US-GAAP tags
us_gaap_data = data.get("facts", {}).get("us-gaap", {})
all_tags = list(us_gaap_data.keys())

# ✅ 4️⃣ Display stats
print(f"📊 Total number of US-GAAP tags found: {len(all_tags)}\n")

# ✅ 5️⃣ Preview tags
print("📝 Sample tags:")
for t in all_tags[:30]:
    print("-", t)

# ✅ 6️⃣ Optional: Save to text file for manual review
with open("data/processed/apple_tags_list.txt", "w") as f:
    for t in all_tags:
        f.write(t + "\n")

print("\n📁 Saved full tag list to data/processed/apple_tags_list.txt")