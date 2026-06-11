import os
import re

def clean_secrets():
    notebooks_dir = r"C:\Users\fagon\Loxi\submission_notebooks"
    
    # Common GitHub PAT pattern: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # or github_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    pat_pattern = re.compile(r'(ghp_[a-zA-Z0-9]{36,40}|github_pat_[a-zA-Z0-9_]{82,100})')
    
    cleaned_count = 0
    # Walk recursively through all directories
    for root, dirs, files in os.walk(notebooks_dir):
        for filename in files:
            if filename.endswith(".ipynb") or filename.endswith(".html") or filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    matches = pat_pattern.findall(content)
                    if matches:
                        print(f"Found {len(matches)} secrets in {os.path.relpath(filepath, notebooks_dir)}:")
                        for m in set(matches):
                            print(f"  - {m[:10]}...")
                        
                        # Replace with placeholder
                        new_content = pat_pattern.sub('"YOUR_GITHUB_TOKEN"', content)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        cleaned_count += 1
                except Exception as e:
                    print(f"Error cleaning {filename}: {e}")
                
    print(f"\nSuccessfully cleaned secrets from {cleaned_count} files recursively.")

if __name__ == '__main__':
    clean_secrets()
