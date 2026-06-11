
import os

files = [
    "index.html",
    "about.html",
    "facilities.html",
    "worship.html",
    "ministry.html",
    "next_gen.html",
    "directions.html"
]

base_dir = r"c:\Users\Pastor Y\Desktop\홈페이지"

for file_name in files:
    file_path = os.path.join(base_dir, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(">사역안내</a>", ">제자훈련</a>")
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_name}")
        else:
            print(f"No match in {file_name}")
            
    except Exception as e:
        print(f"Error updating {file_name}: {e}")
