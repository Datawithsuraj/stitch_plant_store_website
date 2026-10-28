import glob
import os
from bs4 import BeautifulSoup

html_files = sorted(glob.glob('*.html'))
print(f"Total HTML files verified: {len(html_files)}\n")

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
    
    scripts = [s.get('src') for s in soup.find_all('script') if s.get('src')]
    has_store = 'js/store.js' in scripts
    has_nav = 'js/nav.js' in scripts
    title = soup.title.string.strip() if soup.title else "No Title"
    
    # Check internal links in this page
    links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
    local_links = [l for l in links if l.endswith('.html')]
    missing_links = [l for l in local_links if not os.path.exists(l.split('?')[0])]
    
    print(f"{fpath:25} | Store:{str(has_store):5} | Nav:{str(has_nav):5} | Missing Links: {len(missing_links)} | Title: {title[:45]}")

print("\nAll verification complete.")
