# src/search_tags.py
import os

TAG_FILE = "data/processed/apple_tags_list.txt"

# ✅ 1️⃣ Check file exists
if not os.path.exists(TAG_FILE):
    raise FileNotFoundError(f"❌ Tag list file not found: {TAG_FILE}")

# ✅ 2️⃣ Load tags
with open(TAG_FILE, "r") as f:
    tags = [line.strip() for line in f if line.strip()]

print(f"✅ Loaded {len(tags)} tags from {TAG_FILE}\n")

# ✅ 3️⃣ Ask user for one or more keywords (comma-separated)
keywords_input = input("🔍 Enter keywords (comma-separated): ").strip().lower()
keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]

# ✅ 4️⃣ Search each keyword
for keyword in keywords:
    matches = [tag for tag in tags if keyword in tag.lower()]
    
    print("\n" + "="*80)
    print(f"🔍 Keyword: '{keyword}'")
    if matches:
        print(f"📊 Found {len(matches)} matching tags:\n")
        for tag in matches:
            print("-", tag)
    else:
        print(f"⚠️ No tags found for keyword '{keyword}'")
print("="*80)