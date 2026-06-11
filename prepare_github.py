import os
import glob

base_dir = r"c:/Users/Pastor Y/Desktop/홈페이지"
assets_dir = os.path.join(base_dir, "assets")

rename_map = {
    "교회로고.png": "church_logo.png",
    "교회메인.JPG": "church_main.jpg",
    "기도자리.jpg": "prayer_room.jpg",
    "놀이터.jpg": "playground.jpg",
    "다음세대1.png": "nextgen_1.png",
    "다음세대2.png": "nextgen_2.png",
    "다음세대3.png": "nextgen_3.png",
    "담임목사.jpg": "senior_pastor.jpg",
    "본당.jpg": "main_chapel.jpg",
    "주차장.jpg": "parking_lot.jpg",
    "친교실.jpg": "fellowship_hall.jpg",
}

# 1. Rename files in assets
for old_name, new_name in rename_map.items():
    old_path = os.path.join(assets_dir, old_name)
    new_path = os.path.join(assets_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found for renaming: {old_name}")

# 2. Update references in html and css files
target_files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "styles", "*.css"))

for file_path in target_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old_name, new_name in rename_map.items():
            # URL encoded version might be needed if they were already encoded, but they were literal in HTML.
            # In CSS they might be inside url('')
            new_content = new_content.replace(old_name, new_name)
            
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated references in {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

print("GitHub Pages preparation complete.")
