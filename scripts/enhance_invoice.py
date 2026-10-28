from bs4 import BeautifulSoup

def enhance_invoice():
    with open('invoice.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Add section IDs
    for sec in soup.find_all('section'):
        txt = sec.get_text()
        if 'CERTIFICATE OF PROVENANCE' in txt and not sec.get('id'):
            sec['id'] = 'certificate-section'
        elif 'Ledger' in txt and 'Line Items' in txt and not sec.get('id'):
            sec['id'] = 'ledger-section'
        elif 'Payment Summary' in txt or 'Archival Invoice' in txt and not sec.get('id'):
            sec['id'] = 'invoice-section'

    # Modal and Tab Script
    script_html = '''
    <div id="nfcLedgerModal" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 bg-inverse-surface/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
      <div class="bg-background w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden border border-primary/10 flex flex-col">
        <div class="bg-surface-container-low p-6 border-b border-primary/5 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-secondary text-[26px]">contactless</span>
            <div>
              <h3 class="font-headline-sm text-primary font-serif">NFC Medallion Cryptographic Seal</h3>
              <p class="font-label-sm text-on-surface-variant text-[11px]">Hardware Provenance Verification</p>
            </div>
          </div>
          <button onclick="closeNfcModal()" class="w-8 h-8 rounded-full bg-surface text-outline hover:text-primary flex items-center justify-center">
            <span class="material-symbols-outlined text-[18px]">close</span>
          </button>
        </div>
        <div class="p-6 space-y-4 font-body-sm text-on-surface-variant text-xs leading-relaxed">
          <div class="p-3 bg-secondary/10 border border-secondary/20 rounded-xl flex items-center gap-3 text-secondary">
            <span class="material-symbols-outlined text-[24px]">verified</span>
            <div>
              <strong class="text-primary block text-sm">Seal Authenticated • Master Registry Node</strong>
              <span>Brass Medallion #MD-772 embedded in 8" Tuscan Terracotta.</span>
            </div>
          </div>
          <div class="space-y-1.5 p-3 bg-surface-container-low rounded-xl font-mono text-[11px]">
            <div class="flex justify-between"><span>Hardware UID:</span> <span class="text-primary font-bold">04:A2:8F:B1:9C:33:80</span></div>
            <div class="flex justify-between"><span>Specimen ID:</span> <span class="text-primary font-bold">#MD-2025-V7</span></div>
            <div class="flex justify-between"><span>Batch Hash:</span> <span class="text-primary font-bold">e3b0c44298fc1c14...</span></div>
            <div class="flex justify-between"><span>Hardening Nursery:</span> <span class="text-primary font-bold">Sauvie Island Bay 04</span></div>
          </div>
          <p class="text-[11px] text-outline">This specimen has been certified under Verdant Haven's living botanical guarantee protocol. Tap anytime to view dynamic root metrics.</p>
        </div>
      </div>
    </div>

    <script>
      function switchInvoiceSection(secId) {
        document.querySelectorAll('nav[data-active-classes] a').forEach(a => {
          a.classList.remove('bg-primary-container', 'text-on-primary', 'rounded-lg');
          a.classList.add('text-on-surface-variant');
        });

        const activeLink = document.querySelector(`nav a[href="#${secId}-section"], nav a[data-path="botanical-${secId}"]`);
        if (activeLink) {
          activeLink.classList.add('bg-primary-container', 'text-on-primary', 'rounded-lg');
          activeLink.classList.remove('text-on-surface-variant');
        }

        const el = document.getElementById(`${secId}-section`) || document.getElementById(secId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }

      function openNfcModal() {
        const m = document.getElementById('nfcLedgerModal');
        if (m) {
          m.classList.remove('opacity-0', 'pointer-events-none');
          m.classList.add('opacity-100', 'pointer-events-auto');
        }
      }

      function closeNfcModal() {
        const m = document.getElementById('nfcLedgerModal');
        if (m) {
          m.classList.add('opacity-0', 'pointer-events-none');
          m.classList.remove('opacity-100', 'pointer-events-auto');
        }
      }

      document.addEventListener('DOMContentLoaded', () => {
        const btn = document.getElementById('nfcLedgerBtn');
        if (btn) btn.onclick = openNfcModal;
      });
    </script>
    '''

    soup.body.append(BeautifulSoup(script_html, 'html.parser'))

    with open('invoice.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced invoice.html tabs and NFC modal!")

if __name__ == '__main__':
    enhance_invoice()
