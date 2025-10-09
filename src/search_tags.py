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

# ✅ 3️⃣ Ask user for a keyword
keyword = input("🔍 Enter keyword to search in tags: ").strip().lower()

# ✅ 4️⃣ Filter tags
matches = [tag for tag in tags if keyword in tag.lower()]

# ✅ 5️⃣ Show results
if matches:
    print(f"\n📊 Found {len(matches)} matching tags for keyword '{keyword}':\n")
    for tag in matches:
        print("-", tag)
else:
    print(f"\n⚠️ No tags found for keyword '{keyword}'")