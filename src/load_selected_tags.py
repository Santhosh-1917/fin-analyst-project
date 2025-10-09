# src/load_selected_tags.py

def load_selected_tags(filepath="data/config/apple_selected_tags.txt"):
    """
    Load curated financial tags from a text file into a Python list.
    Each line in the file should contain one tag.
    """
    with open(filepath, "r") as f:
        tags = [line.strip() for line in f if line.strip()]
    return tags

if __name__ == "__main__":
    selected_tags = load_selected_tags()
    print(f"✅ Loaded {len(selected_tags)} selected tags:")
    print(selected_tags)