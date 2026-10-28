from bs4 import BeautifulSoup

def enhance_account_link():
    with open('account-link.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the active lookup bar
    bar = soup.find('div', class_=lambda c: c and 'bg-surface-container-lowest rounded-lg p-space-sm' in c)
    if not bar:
        print("Lookup bar not found in account-link.html")
        return

    # Replace with 3 reactive panels
    panels_html = '''
    <div id="lookup-panels" class="w-full">
      <!-- PANEL 1: ORDER & ZIP -->
      <div id="lookup-panel-order" class="bg-surface-container-lowest rounded-xl p-space-md shadow-sm border border-primary/10 flex flex-col gap-3">
        <div class="flex items-center gap-space-sm">
          <div class="w-8 h-8 rounded bg-primary/10 text-primary flex items-center justify-center shrink-0">
            <span class="material-symbols-outlined text-[18px]">inventory_2</span>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-label-sm text-[11px] text-on-surface-variant uppercase tracking-wider block">Identified Order Batch</span>
            <span class="font-title-md text-[14px] text-on-surface font-semibold">#VH-84920 • 97201 (Portland, OR)</span>
          </div>
          <button onclick="VerdantStore.showToast('Order Verified', 'Linked to specimen Monstera Deliciosa (Batch #MD-2025-V7).', 'check_circle', 'success')" class="px-3 py-1.5 bg-primary text-on-primary hover:bg-primary-container rounded-lg text-xs font-semibold">
            Re-Verify
          </button>
        </div>
      </div>

      <!-- PANEL 2: NFC / PHYSICAL TAG -->
      <div id="lookup-panel-nfc" class="hidden bg-surface-container-lowest rounded-xl p-space-md shadow-sm border border-primary/10 flex flex-col items-center text-center gap-3">
        <div class="w-14 h-14 rounded-full bg-secondary-container/40 text-secondary flex items-center justify-center animate-pulse">
          <span class="material-symbols-outlined text-[28px]">contactless</span>
        </div>
        <div>
          <h4 class="font-headline-sm text-sm text-primary font-bold">Hold Device Near Terracotta Medallion</h4>
          <p class="text-[12px] text-on-surface-variant mt-0.5">Bring phone within 5cm of the embedded brass NFC chip on the planter rim.</p>
        </div>
        <button id="simulateNfcBtn" onclick="simulateNfcScan()" class="px-5 py-2 rounded-xl bg-secondary text-on-secondary hover:bg-secondary/90 text-xs font-bold shadow-md flex items-center gap-1.5 active:scale-95 transition-all">
          <span class="material-symbols-outlined text-[16px]">sensors</span>
          <span>Simulate NFC Medallion Tap (#MD-772)</span>
        </button>
      </div>

      <!-- PANEL 3: MANUAL ACCESSION ID -->
      <div id="lookup-panel-manual" class="hidden bg-surface-container-lowest rounded-xl p-space-md shadow-sm border border-primary/10 flex flex-col gap-3">
        <label class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider font-semibold">Enter Archival Specimen Accession ID</label>
        <div class="flex items-center gap-2">
          <input type="text" id="manualAccessionInput" value="MD-2025-V7" placeholder="e.g. MD-2025-V7 or FA-09-COL" class="flex-1 px-3 py-2 text-xs bg-surface-container-low border border-outline-variant rounded-lg font-mono uppercase focus:outline-none focus:ring-1 focus:ring-primary" />
          <button onclick="lookupManualAccession()" class="px-4 py-2 bg-primary text-on-primary hover:bg-primary-container rounded-lg text-xs font-semibold">
            Lookup
          </button>
        </div>
      </div>
    </div>
    '''

    bar.replace_with(BeautifulSoup(panels_html, 'html.parser'))

    # Update JavaScript
    script_tag = soup.find('script', text=lambda t: t and 'tabOrder' in t)
    new_script = '''
    <script>
      const tabOrder = document.getElementById('tab-order');
      const tabNfc = document.getElementById('tab-nfc');
      const tabManual = document.getElementById('tab-manual');

      function switchLookupTab(activeTab, panelId) {
        [tabOrder, tabNfc, tabManual].forEach(t => {
          if (t) {
            t.classList.remove('bg-surface-container-lowest', 'text-primary', 'shadow-sm', 'font-semibold');
            t.classList.add('text-on-surface-variant');
          }
        });
        if (activeTab) {
          activeTab.classList.remove('text-on-surface-variant');
          activeTab.classList.add('bg-surface-container-lowest', 'text-primary', 'shadow-sm', 'font-semibold');
        }

        ['lookup-panel-order', 'lookup-panel-nfc', 'lookup-panel-manual'].forEach(id => {
          const el = document.getElementById(id);
          if (el) el.classList.add('hidden');
        });

        const activePanel = document.getElementById(panelId);
        if (activePanel) activePanel.classList.remove('hidden');
      }

      if (tabOrder) tabOrder.onclick = () => switchLookupTab(tabOrder, 'lookup-panel-order');
      if (tabNfc) tabNfc.onclick = () => switchLookupTab(tabNfc, 'lookup-panel-nfc');
      if (tabManual) tabManual.onclick = () => switchLookupTab(tabManual, 'lookup-panel-manual');

      function simulateNfcScan() {
        const btn = document.getElementById('simulateNfcBtn');
        btn.innerHTML = '<span class="material-symbols-outlined text-[16px] animate-spin">refresh</span> Scanning NFC Chip...';
        setTimeout(() => {
          btn.innerHTML = '<span class="material-symbols-outlined text-[16px]">done</span> Medallion #MD-772 Authenticated!';
          btn.classList.remove('bg-secondary');
          btn.classList.add('bg-primary');
          VerdantStore.showToast('NFC Medallion Verified', 'Cryptographic tag #MD-772 linked to Monstera Deliciosa.', 'contactless', 'success');
        }, 800);
      }

      function lookupManualAccession() {
        const val = document.getElementById('manualAccessionInput').value.trim().toUpperCase();
        VerdantStore.showToast('Accession Found', `Found registered specimen: ${val} in Sauvie Island registry.`, 'verified', 'success');
      }
    </script>
    '''

    if script_tag:
        script_tag.replace_with(BeautifulSoup(new_script, 'html.parser'))
    else:
        soup.body.append(BeautifulSoup(new_script, 'html.parser'))

    with open('account-link.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced account-link.html with 3 reactive lookup tabs!")

if __name__ == '__main__':
    enhance_account_link()
