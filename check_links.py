from bs4 import BeautifulSoup
import glob

for filename in sorted(glob.glob('*.html')):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    dead_links = []
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.text.strip().replace('\n', ' ')
        if href in ['#', '', 'javascript:void(0)'] and not a.get('onclick') and not a.get('data-open-quiz'):
            dead_links.append((text[:25], href, a.get('data-path')))
            
    print(f"{filename:25} | Dead/unwired links: {len(dead_links)}")
    if dead_links[:3]:
        for dl in dead_links[:3]:
            print(f"    -> text='{dl[0]}' href='{dl[1]}' path='{dl[2]}'")
