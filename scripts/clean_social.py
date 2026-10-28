import glob
from bs4 import BeautifulSoup

def clean_social_and_remainders():
    files = sorted(glob.glob('*.html'))
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')

        for a in soup.find_all('a'):
            href = a.get('href', '')
            txt = a.get_text(strip=True).lower()
            aria = (a.get('aria-label') or '').lower()

            if 'photo_camera' in txt or 'instagram' in aria:
                a['href'] = 'https://instagram.com'
                a['target'] = '_blank'
                a['rel'] = 'noopener noreferrer'
            elif 'nature' in txt or 'pinterest' in aria:
                a['href'] = 'https://pinterest.com'
                a['target'] = '_blank'
                a['rel'] = 'noopener noreferrer'
            elif 'smart_display' in txt or 'video channel' in aria or 'youtube' in aria:
                a['href'] = 'https://youtube.com'
                a['target'] = '_blank'
                a['rel'] = 'noopener noreferrer'
            elif 'return to cart' in txt or 'return to shop' in txt or 'return' in txt and 'cart' in txt:
                a['href'] = 'catalog.html'
            elif 'launch immediate consultation' in txt:
                a['href'] = 'video-call.html'
            elif 'get the soil recipe' in txt:
                a['href'] = 'care-lab.html'
            elif 'return to records' in txt or 'return to print' in txt:
                a['href'] = 'invoice.html'
            elif href == '#':
                a['href'] = 'catalog.html'

        with open(f, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Final pass on {f}")

if __name__ == '__main__':
    clean_social_and_remainders()
