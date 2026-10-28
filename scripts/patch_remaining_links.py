import re
import glob
from bs4 import BeautifulSoup

def fix_all_links():
    mapping = {
        'ethical-sourcing': 'passport.html',
        'carbon-neutral': 'order-confirmation.html',
        'botanical-guarantee': 'passport.html',
        'botanical-certificate': '#certificate-section',
        'care-protocol': '#ledger-section',
        'order-invoice': '#invoice-section',
        'sanctuary': 'index.html',
    }

    files = sorted(glob.glob('*.html'))
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')

        # Add section IDs in invoice.html if present
        if f == 'invoice.html':
            for sec in soup.find_all('section'):
                if 'CERTIFICATE OF PROVENANCE' in str(sec) and not sec.get('id'):
                    sec['id'] = 'certificate-section'
            for art in soup.find_all(['section', 'article', 'div']):
                if 'Ledger Table of Line Items' in str(art) and not art.get('id'):
                    art['id'] = 'ledger-section'
                if 'Archival Invoice' in str(art) and not art.get('id'):
                    art['id'] = 'invoice-section'

        for a in soup.find_all('a'):
            href = a.get('href', '')
            path = a.get('data-path', '')
            txt = a.get_text(strip=True).lower()

            if path in mapping:
                a['href'] = mapping[path]
                continue

            if href == '#' or href.startswith('javascript:'):
                if 'already have a sanctuary' in txt or 'sign in' in txt:
                    a['href'] = 'login.html'
                elif 'forgot passcode' in txt or 'reset' in txt:
                    a['href'] = 'login.html'
                elif 'return to records' in txt or 'back to record' in txt or 'return to order' in txt:
                    a['href'] = 'invoice.html' if f in ['invoice-print.html', 'mailing-label.html'] else 'order-confirmation.html'
                elif 'browse all 48 field guide' in txt or 'read diagnostic' in txt or 'calibrate winter' in txt:
                    a['href'] = 'care-lab.html'
                elif 'view plant lineup' in txt or 'explore all low-light' in txt or 'browse rare' in txt or 'botanical sa' in txt:
                    a['href'] = 'catalog.html'
                elif 'enter sanctuary portal' in txt or 'client sanctuary' in txt:
                    a['href'] = 'dashboard.html'
                elif 'change time slot' in txt or 'contact atelier desk' in txt or 'contact con' in txt or 'learn about botanical doc' in txt or 'change' == txt:
                    a['href'] = 'consultation.html'
                elif 'view tele-room' in txt:
                    a['href'] = 'video-call.html'
                elif 'read journal entry' in txt or 'horticultural code' in txt:
                    a['href'] = 'passport.html'
                elif 'atelier protocol' in txt:
                    a['href'] = 'index.html'
                elif 'certificate of provenance' in txt:
                    a['href'] = '#certificate-section'
                    a['onclick'] = "switchInvoiceSection('certificate'); return false;"
                elif 'care ledger' in txt or 'horticultural care' in txt:
                    a['href'] = '#ledger-section'
                    a['onclick'] = "switchInvoiceSection('ledger'); return false;"
                elif 'archival invoice' in txt:
                    a['href'] = '#invoice-section'
                    a['onclick'] = "switchInvoiceSection('invoice'); return false;"

        with open(f, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Cleaned links in {f}")

if __name__ == '__main__':
    fix_all_links()
