import re
import glob
from bs4 import BeautifulSoup

def fix_links_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Fix navigation and footer links
    for a in soup.find_all('a'):
        path = a.get('data-path', '')
        href = a.get('href', '')
        text = a.get_text(strip=True).lower()

        if path == 'greenhouse-locations' or 'our nurseries' in text:
            a['href'] = 'catalog.html'
            a['title'] = 'Glasshouse Cultivars & Nursery Locations'
        elif path in ['sustainability', 'sustainability-pledge'] or 'botanical guarantee' in text or 'our botanical pledge' in text:
            a['href'] = 'passport.html'
            a['title'] = 'Sanctuary Botanical Guarantee & Provenance'
        elif path in ['shop-plants', 'botanical-catalog'] or text in ['shop plants', 'botanical catalog'] or href == '#curated-catalog':
            a['href'] = 'catalog.html'
        elif path == 'rare-finds' or text in ['rare finds', 'monstera deliciosa']:
            a['href'] = 'product.html'
        elif path == 'planters-and-care' or text == 'planters & care':
            a['href'] = 'catalog.html?category=vessels'
        elif path in ['care-lab', 'plant-care-lab-provenance'] or 'care lab' in text or 'plant doctor' in text:
            if 'book a plant doctor' in text or 'live-horticulturist' in path:
                a['href'] = 'consultation.html'
            else:
                a['href'] = 'care-lab.html'
        elif path in ['provenance', 'living-passport-digital-herbarium'] or 'passport' in text or 'herbarium' in text:
            a['href'] = 'passport.html'
        elif path == 'workshops' or text == 'workshops':
            a['href'] = 'consultation.html'
        elif path == 'about' or text == 'about':
            a['href'] = 'passport.html'
        elif path in ['reviews-feedback', 'reviews-and-feedback', 'botanical-reviews'] or 'reviews' in text:
            a['href'] = 'reviews.html'
        elif path in ['acclimation-journal', '30-day-root-vitality-checkup-booking'] or '30-day root checkup' in text or 'acclimation journal' in text:
            a['href'] = 'vitality-checkup.html'
        elif path in ['shipping-and-tracking'] or 'shipping & greenhouse transit' in text or 'delivery concierge' in text:
            a['href'] = 'order-confirmation.html'
        elif path == 'order-history' or 'return to order' in text or 'back to order' in text:
            a['href'] = 'order-confirmation.html'
        elif path == 'sustainable-packaging' or 'zero-plastic packaging' in text:
            a['href'] = 'mailing-label.html'
        elif path == 'privacy-policy' or 'privacy policy' in text:
            a['href'] = 'javascript:void(0)'
            a['onclick'] = "openPolicyModal('Sanctuary Privacy & Telemetry Protocol'); return false;"
        elif path == 'terms-of-service' or 'terms of service' in text:
            a['href'] = 'javascript:void(0)'
            a['onclick'] = "openPolicyModal('Sanctuary Terms & Horticultural Assurance'); return false;"
        elif any(g in text for g in ['assessing natural light', 'the art of root hydration', 'substrates & repotting', 'organic pest defense']):
            a['href'] = 'care-lab.html'
        elif 'pet-friendly houseplants' in text:
            a['href'] = 'catalog.html?filter=pet-safe'
        elif path in ['corporate-gifting', 'contact'] or 'customer inquiries' in text or 'concierge chat' in text:
            a['href'] = 'consultation.html'
        elif path == 'pot-recycling' or 'vessel reuse initiative' in text:
            a['href'] = 'product.html'
        elif href == '#' and text in ['home', 'sanctuary', 'verdant haven']:
            a['href'] = 'index.html'
        elif href == '#' and 'catalog' in text:
            a['href'] = 'catalog.html'
        elif href == '#' and 'records' in text:
            a['href'] = 'invoice.html'
        elif href == '#' and 'print' in text:
            a['href'] = 'invoice-print.html'
        elif href == '#' and 'aroids & epiphytes' in text:
            a['href'] = 'catalog.html'
        elif href == '#' and 'sanctuary collections' in text:
            a['href'] = 'catalog.html'
        elif href == '#' and 'low-light & climbers' in text:
            a['href'] = 'catalog.html'
        elif href == '#' and 'drainage protocol' in text:
            a['href'] = 'catalog.html?category=vessels'
        elif href == '#' and 'vector gallery' in text:
            a['href'] = 'passport.html'
        elif href == '#' and 'contact concierge' in text:
            a['href'] = 'consultation.html'
        elif href == '#' and 'browse botanical' in text:
            a['href'] = 'catalog.html'
        elif href == '#' and 'book a 30-day' in text:
            a['href'] = 'vitality-checkup.html'

    # Save modified HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Patched links in {filepath}")

def run_all():
    files = sorted(glob.glob('*.html'))
    for f in files:
        fix_links_in_file(f)

if __name__ == '__main__':
    run_all()
