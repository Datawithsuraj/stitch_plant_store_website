import os
import re
from bs4 import BeautifulSoup

def clean_and_enhance_html(html, active_nav='sanctuary', page_title='Verdant Haven — Artisanal Botanical Boutique'):
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Update title if needed
    if soup.title:
        soup.title.string = page_title
    else:
        new_title = soup.new_tag('title')
        new_title.string = page_title
        soup.head.append(new_title)

    # 2. Inject store.js and nav.js into head
    store_script = soup.new_tag('script', src='js/store.js')
    nav_script = soup.new_tag('script', src='js/nav.js')
    soup.head.append(store_script)
    soup.head.append(nav_script)

    # 3. Add base styles for smoother animations and interactions
    custom_style = soup.new_tag('style')
    custom_style.string = """
      html { scroll-behavior: smooth; }
      .fade-in { animation: fadeIn 0.4s ease-in-out; }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      .btn-hover-lift { transition: transform 0.2s ease, box-shadow 0.2s ease; }
      .btn-hover-lift:hover { transform: translateY(-2px); box-shadow: 0 8px 20px -4px rgba(0,54,41,0.15); }
    """
    soup.head.append(custom_style)

    # 4. Standardize navigation links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        data_path = a.get('data-path', '')

        # Home / Sanctuary
        if data_path == 'sanctuary' or href in ['#sanctuary', 'index.html', '#']:
            if 'Shop Plants' not in a.text and 'Curated' not in a.text and 'Verdant Haven' in a.text:
                a['href'] = 'index.html'

        # Shop / Catalog
        if data_path in ['shop-plants', 'botanical-catalog'] or 'Shop Plants' in a.text or 'Botanical Catalog' in a.text or href == '#curated-catalog':
            a['href'] = 'catalog.html'

        # Product Detail
        if data_path == 'rare-finds' or 'Rare Finds' in a.text or 'Monstera Deliciosa' in a.text:
            if a.get('href') == '#':
                a['href'] = 'product.html'

        # Care Lab
        if data_path in ['care-lab', 'plant-care-lab-provenance'] or 'Care Lab' in a.text:
            a['href'] = 'care-lab.html'

        # Provenance / Passport
        if data_path in ['provenance', 'living-passport-digital-herbarium', 'sustainability'] or 'Passport' in a.text or 'Herbarium' in a.text:
            a['href'] = 'passport.html'

        # Reviews
        if data_path in ['reviews-feedback', 'reviews-and-feedback', 'botanical-reviews'] or 'Reviews' in a.text:
            a['href'] = 'reviews.html'

        # Checkup
        if data_path in ['acclimation-journal', '30-day-root-vitality-checkup-booking'] or '30-Day' in a.text or 'Checkup' in a.text:
            a['href'] = 'vitality-checkup.html'

        # Consultation
        if data_path in ['virtual-consultation', 'live-horticulturist-video-consultation-root-health-audit'] or 'Plant Doctor' in a.text:
            a['href'] = 'consultation.html'

        # Plant Quiz
        if data_path == 'plant-quiz' or 'Plant Quiz' in a.text or 'Take 2-Min Plant Quiz' in a.text:
            a['href'] = '#quiz'
            a['data-open-quiz'] = 'true'

        # Cart
        if data_path == 'cart' or 'cart' in href or a.get('aria-label') == 'Shopping Cart':
            a['href'] = '#cart'
            a['class'] = (a.get('class', []) if isinstance(a.get('class'), list) else [a.get('class')]) + ['cart-toggle']
            a['onclick'] = 'openCartDrawer(); return false;'

    return str(soup)

print("Builder helper loaded.")
