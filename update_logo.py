import os

files = [
    "index.html", "about.html", "facilities.html", 
    "worship.html", "ministry.html", "next_gen.html", "directions.html"
]

target_text = '<a href="index.html" class="logo">해남성결교회</a>'
replacement_text = '<a href="index.html" class="logo">\n                <img src="assets/교회로고.png" alt="해남성결교회">\n            </a>'

base_path = r"c:/Users/Pastor Y/Desktop/홈페이지"

for file_name in files:
    file_path = os.path.join(base_path, file_name)
    if os.path.exists(file_path):
        try:
            # Read with utf-8
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if replacement is needed
            if target_text in content:
                new_content = content.replace(target_text, replacement_text)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file_name}")
            else:
                print(f"Skipped {file_name} (Target not found)")
                
        except Exception as e:
            print(f"Failed to update {file_name}: {e}")
