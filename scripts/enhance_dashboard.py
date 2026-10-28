import re
from bs4 import BeautifulSoup

def enhance_dashboard():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the main grid
    main_grid = soup.find('div', class_=re.compile(r'grid-cols-1 lg:grid-cols-12 gap-gutter'))
    if not main_grid:
        print("Main grid not found in dashboard.html")
        return

    # Create Tab Navigation Element
    tabs_html = '''
    <!-- DASHBOARD ARCHITECTURAL TAB NAVIGATION -->
    <div class="w-full bg-surface-container-low p-2 rounded-2xl mb-space-lg border border-primary/10 shadow-sm">
      <div class="flex flex-wrap items-center justify-between gap-2" id="dashboard-tablist" role="tablist">
        <button id="tab-btn-collection" onclick="switchDashboardTab('collection')" class="dash-tab active flex items-center gap-2 px-5 py-3 rounded-xl bg-primary text-on-primary font-label-lg text-sm font-semibold shadow-md transition-all active:scale-95" role="tab" aria-selected="true">
          <span class="material-symbols-outlined text-[18px]">potted_plant</span>
          <span>My Specimen Vault (3)</span>
        </button>
        <button id="tab-btn-telemetry" onclick="switchDashboardTab('telemetry')" class="dash-tab flex items-center gap-2 px-5 py-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-lg text-sm transition-all active:scale-95" role="tab" aria-selected="false">
          <span class="material-symbols-outlined text-[18px]">sensors</span>
          <span>Live Sensors &amp; Telemetry</span>
        </button>
        <button id="tab-btn-calendar" onclick="switchDashboardTab('calendar')" class="dash-tab flex items-center gap-2 px-5 py-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-lg text-sm transition-all active:scale-95" role="tab" aria-selected="false">
          <span class="material-symbols-outlined text-[18px]">calendar_month</span>
          <span>Care Schedule &amp; Tasks (3)</span>
        </button>
        <button id="tab-btn-orders" onclick="switchDashboardTab('orders')" class="dash-tab flex items-center gap-2 px-5 py-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-lg text-sm transition-all active:scale-95" role="tab" aria-selected="false">
          <span class="material-symbols-outlined text-[18px]">receipt_long</span>
          <span>Dispatches &amp; Invoices (2)</span>
        </button>
      </div>
    </div>
    '''

    tab_soup = BeautifulSoup(tabs_html, 'html.parser')
    main_grid.insert_before(tab_soup)

    # Tag main_grid as panel-collection
    main_grid['id'] = 'panel-collection'
    main_grid['class'] = main_grid.get('class', []) + ['dash-panel']

    # Add extra specimens to left column
    extra_specimens = '''
    <!-- Additional Specimen 2: Ficus Audrey -->
    <div class="relative bg-surface-container-lowest rounded-2xl shadow-md p-space-lg overflow-hidden border border-outline-variant/30 mt-space-md">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-space-md">
        <div class="flex items-center gap-space-md">
          <img src="https://images.unsplash.com/photo-1545241047-6083a3684587?auto=format&fit=crop&w=300&q=80" class="w-20 h-20 rounded-xl object-cover shadow-sm" />
          <div>
            <span class="text-xs uppercase tracking-wider text-secondary font-bold">Specimen #FA-09-COL</span>
            <h4 class="font-headline-sm text-lg text-primary font-serif italic">Ficus Audrey Standard</h4>
            <p class="text-xs text-on-surface-variant">Pacific Grove Glasshouse • 10" Unglazed Planter</p>
            <div class="flex items-center gap-2 mt-1">
              <span class="px-2 py-0.5 rounded-full bg-secondary-container text-on-secondary-fixed text-[11px] font-bold">Acclimated Day 112</span>
              <span class="text-[11px] text-outline">VWC: 36% • Turgor Prime</span>
            </div>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <a href="passport.html" class="px-4 py-2 rounded-lg bg-surface-container hover:bg-surface-container-high text-primary text-xs font-semibold">View Passport</a>
          <a href="care-lab.html" class="px-4 py-2 rounded-lg bg-primary text-on-primary hover:bg-primary-container text-xs font-semibold">Care Lab Triage</a>
        </div>
      </div>
    </div>

    <!-- Additional Specimen 3: Philodendron Spiritus Sancti -->
    <div class="relative bg-surface-container-lowest rounded-2xl shadow-md p-space-lg overflow-hidden border border-outline-variant/30 mt-space-md">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-space-md">
        <div class="flex items-center gap-space-md">
          <img src="https://images.unsplash.com/photo-1512428813834-c702c7702b78?auto=format&fit=crop&w=300&q=80" class="w-20 h-20 rounded-xl object-cover shadow-sm" />
          <div>
            <span class="text-xs uppercase tracking-wider text-tertiary-container font-bold">Archival Drop #PSS-8812</span>
            <h4 class="font-headline-sm text-lg text-primary font-serif italic">Philodendron Spiritus Sancti</h4>
            <p class="text-xs text-on-surface-variant">Espírito Santo F1 Clone • 8" Basalt Vessel</p>
            <div class="flex items-center gap-2 mt-1">
              <span class="px-2 py-0.5 rounded-full bg-primary-fixed text-on-primary-fixed text-[11px] font-bold">Rare Vault Specimen</span>
              <span class="text-[11px] text-secondary font-semibold">Full Cryptographic Ledger</span>
            </div>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <a href="passport.html" class="px-4 py-2 rounded-lg bg-surface-container hover:bg-surface-container-high text-primary text-xs font-semibold">View Passport</a>
          <a href="consultation.html" class="px-4 py-2 rounded-lg bg-primary text-on-primary hover:bg-primary-container text-xs font-semibold">Doctor Audit</a>
        </div>
      </div>
    </div>
    '''
    left_col = main_grid.find('div', class_=re.compile(r'lg:col-span-7'))
    if left_col:
        left_col.append(BeautifulSoup(extra_specimens, 'html.parser'))

    # Add Panels 2, 3, 4 after main_grid
    panels_html = '''
    <!-- PANEL 2: TELEMETRY & LIVE SENSORS -->
    <div id="panel-telemetry" class="dash-panel hidden w-full mb-space-xl flex-col gap-space-lg">
      <div class="bg-surface-container-lowest rounded-2xl shadow-md p-space-lg md:p-space-xl border border-primary/10">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between pb-space-md border-b border-primary/10 gap-4">
          <div>
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-secondary-container/40 text-secondary text-xs uppercase font-bold tracking-wider mb-1">
              <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
              Live BLE &amp; NFC Hydro-Telemetry Hub
            </div>
            <h3 class="font-headline-md text-primary font-serif">Specimen Biometric Telemetry Matrix</h3>
            <p class="text-xs text-on-surface-variant">Continuous cellular turgor, root moisture, and photoperiod calibration for Clara's collection.</p>
          </div>
          <a href="care-lab.html" class="px-5 py-2.5 rounded-xl bg-primary text-on-primary text-xs font-bold hover:bg-primary-container shadow-md flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px]">biotech</span>
            <span>Launch Care Lab Diagnostics</span>
          </a>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          <div class="p-5 rounded-xl bg-surface-container-low border border-primary/5 flex flex-col justify-between">
            <div class="flex items-center justify-between text-secondary">
              <span class="text-xs font-bold uppercase tracking-wider">Substrate VWC</span>
              <span class="material-symbols-outlined text-[20px]">water_drop</span>
            </div>
            <div class="my-3">
              <span class="text-3xl font-headline-md text-primary font-serif font-bold">42.8%</span>
              <span class="text-xs text-secondary font-semibold ml-1">Optimal</span>
            </div>
            <p class="text-[11px] text-on-surface-variant">Terracotta aeration maintains balanced rhizosphere hydration.</p>
          </div>
          <div class="p-5 rounded-xl bg-surface-container-low border border-primary/5 flex flex-col justify-between">
            <div class="flex items-center justify-between text-secondary">
              <span class="text-xs font-bold uppercase tracking-wider">Ambient RH</span>
              <span class="material-symbols-outlined text-[20px]">humidity_mid</span>
            </div>
            <div class="my-3">
              <span class="text-3xl font-headline-md text-primary font-serif font-bold">66.4%</span>
              <span class="text-xs text-secondary font-semibold ml-1">Target 65%</span>
            </div>
            <p class="text-[11px] text-on-surface-variant">East-facing conservatory humidity envelope stable.</p>
          </div>
          <div class="p-5 rounded-xl bg-surface-container-low border border-primary/5 flex flex-col justify-between">
            <div class="flex items-center justify-between text-secondary">
              <span class="text-xs font-bold uppercase tracking-wider">Daily Light (DLI)</span>
              <span class="material-symbols-outlined text-[20px]">wb_sunny</span>
            </div>
            <div class="my-3">
              <span class="text-3xl font-headline-md text-primary font-serif font-bold">14.2</span>
              <span class="text-xs text-on-surface-variant ml-1">mol/m²/d</span>
            </div>
            <p class="text-[11px] text-on-surface-variant">Morning indirect sun exposure without UV blade scorch.</p>
          </div>
          <div class="p-5 rounded-xl bg-surface-container-low border border-primary/5 flex flex-col justify-between">
            <div class="flex items-center justify-between text-secondary">
              <span class="text-xs font-bold uppercase tracking-wider">Rhizosphere Temp</span>
              <span class="material-symbols-outlined text-[20px]">thermostat</span>
            </div>
            <div class="my-3">
              <span class="text-3xl font-headline-md text-primary font-serif font-bold">69.8°F</span>
              <span class="text-xs text-secondary font-semibold ml-1">Pristine</span>
            </div>
            <p class="text-[11px] text-on-surface-variant">Root thermal buffer supported by 16mm Tuscan clay.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- PANEL 3: CARE SCHEDULE & TASKS -->
    <div id="panel-calendar" class="dash-panel hidden w-full mb-space-xl flex-col gap-space-lg">
      <div class="bg-surface-container-lowest rounded-2xl shadow-md p-space-lg md:p-space-xl border border-primary/10">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between pb-space-md border-b border-primary/10 gap-4">
          <div>
            <h3 class="font-headline-md text-primary font-serif">Prescribed Sanctuary Care Tasks</h3>
            <p class="text-xs text-on-surface-variant">Tailored cultivation rhythm supervised by Dr. Elena Alvarez.</p>
          </div>
          <button onclick="VerdantStore.showToast('Schedule Synced', 'All tasks synchronized with Google Calendar and Apple Reminders.', 'sync', 'success')" class="px-4 py-2 rounded-xl bg-surface-container text-primary text-xs font-bold hover:bg-surface-container-high flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">sync</span>
            <span>Sync with Calendar (.ics)</span>
          </button>
        </div>

        <div class="space-y-3 mt-6" id="dashboardTaskList">
          <div class="flex items-center justify-between p-4 rounded-xl bg-surface-container-low border border-primary/5 hover:border-primary/20 transition-all">
            <label class="flex items-center gap-3 cursor-pointer select-none">
              <input type="checkbox" onchange="toggleDashTask(this, 'Hydration Routine')" class="w-5 h-5 rounded accent-primary cursor-pointer" />
              <div>
                <span class="font-title-md text-sm text-primary font-bold">Deep Soak Root Hydration (Monstera Deliciosa)</span>
                <p class="text-xs text-on-surface-variant">Flush pot with 1.2L distilled rainwater. Empty drainage tray after 30 mins.</p>
              </div>
            </label>
            <span class="px-3 py-1 rounded-full bg-secondary-container text-on-secondary-fixed text-xs font-bold shrink-0">Due Friday</span>
          </div>

          <div class="flex items-center justify-between p-4 rounded-xl bg-surface-container-low border border-primary/5 hover:border-primary/20 transition-all">
            <label class="flex items-center gap-3 cursor-pointer select-none">
              <input type="checkbox" onchange="toggleDashTask(this, 'Foliar Rotation')" class="w-5 h-5 rounded accent-primary cursor-pointer" />
              <div>
                <span class="font-title-md text-sm text-primary font-bold">Foliar Micro-Mist &amp; 90° Clockwise Rotation</span>
                <p class="text-xs text-on-surface-variant">Clean adaxial cuticle with microfiber cloth and atomized demineralized mist.</p>
              </div>
            </label>
            <span class="px-3 py-1 rounded-full bg-surface-container text-on-surface-variant text-xs font-bold shrink-0">Due Sunday</span>
          </div>

          <div class="flex items-center justify-between p-4 rounded-xl bg-secondary/5 border border-secondary/20 hover:border-secondary/40 transition-all">
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary text-[24px]">vital_signs</span>
              <div>
                <span class="font-title-md text-sm text-primary font-bold">30-Day Root Vitality Tele-Audit with Dr. Elena</span>
                <p class="text-xs text-on-surface-variant">Scheduled clinical video inspection to certify root acclimation and extend living guarantee.</p>
              </div>
            </div>
            <a href="video-call.html" class="px-4 py-2 rounded-xl bg-primary text-on-primary hover:bg-primary-container text-xs font-bold shrink-0 flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px]">videocam</span>
              <span>Join Call Room</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- PANEL 4: DISPATCHES & INVOICES -->
    <div id="panel-orders" class="dash-panel hidden w-full mb-space-xl flex-col gap-space-lg">
      <div class="bg-surface-container-lowest rounded-2xl shadow-md p-space-lg md:p-space-xl border border-primary/10">
        <div class="pb-space-md border-b border-primary/10">
          <h3 class="font-headline-md text-primary font-serif">Botanical Dispatches &amp; Archival Records</h3>
          <p class="text-xs text-on-surface-variant">Complete provenance records, bills of sale, and courier dispatch logs for your account.</p>
        </div>

        <div class="space-y-4 mt-6">
          <div class="p-5 rounded-2xl bg-surface-container-low border border-primary/10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs uppercase font-bold tracking-wider text-secondary">Delivered &amp; Sealed</span>
                <span class="text-xs text-outline">•</span>
                <span class="text-xs font-semibold text-primary">Order #VH-84920</span>
                <span class="text-xs text-outline">•</span>
                <span class="text-xs text-on-surface-variant">Dispatched Jun 18, 2025</span>
              </div>
              <h4 class="font-headline-sm text-base text-primary font-serif">Monstera Deliciosa Liebm. + Tuscan Terracotta Planter</h4>
              <p class="text-xs text-on-surface-variant mt-0.5">Total Settlement: <strong>$227.00 USD</strong> • Tracked via Thermal Express Courier</p>
            </div>
            <div class="flex flex-wrap items-center gap-2 shrink-0">
              <a href="order-confirmation.html" class="px-3.5 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-primary text-xs font-semibold flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">local_shipping</span>
                <span>Live Tracker</span>
              </a>
              <a href="invoice.html" class="px-3.5 py-2 rounded-xl bg-primary text-on-primary hover:bg-primary-container text-xs font-semibold flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                <span>Provenance Invoice</span>
              </a>
              <a href="mailing-label.html" class="px-3.5 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface text-xs font-semibold flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">mail</span>
                <span>Courier Label</span>
              </a>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-surface-container-low border border-primary/10 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs uppercase font-bold tracking-wider text-outline">Archived Record</span>
                <span class="text-xs text-outline">•</span>
                <span class="text-xs font-semibold text-primary">Order #VH-81042</span>
                <span class="text-xs text-outline">•</span>
                <span class="text-xs text-on-surface-variant">Apr 12, 2025</span>
              </div>
              <h4 class="font-headline-sm text-base text-primary font-serif">Artisanal Earthenware Pot 10" + Substrate Formula A-7</h4>
              <p class="text-xs text-on-surface-variant mt-0.5">Total Settlement: <strong>$68.00 USD</strong> • Standard Eco Ground</p>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <a href="invoice.html" class="px-3.5 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-primary text-xs font-semibold flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                <span>Archival Invoice</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    '''

    main_grid.insert_after(BeautifulSoup(panels_html, 'html.parser'))

    # Add JavaScript for tab switching
    dash_script = '''
    <script>
      function switchDashboardTab(tabId) {
        document.querySelectorAll('.dash-tab').forEach(b => {
          b.classList.remove('bg-primary', 'text-on-primary', 'shadow-md', 'active');
          b.classList.add('bg-surface-container', 'text-on-surface');
          b.setAttribute('aria-selected', 'false');
        });

        const activeBtn = document.getElementById(`tab-btn-${tabId}`);
        if (activeBtn) {
          activeBtn.classList.remove('bg-surface-container', 'text-on-surface');
          activeBtn.classList.add('bg-primary', 'text-on-primary', 'shadow-md', 'active');
          activeBtn.setAttribute('aria-selected', 'true');
        }

        document.querySelectorAll('.dash-panel').forEach(p => {
          p.classList.add('hidden');
          p.classList.remove('flex');
        });

        const activePanel = document.getElementById(`panel-${tabId}`);
        if (activePanel) {
          activePanel.classList.remove('hidden');
          if (tabId === 'collection') {
            activePanel.style.display = 'grid';
          } else {
            activePanel.classList.add('flex');
            activePanel.style.display = 'flex';
          }
        }

        const tabNames = {
          collection: 'Living Specimen Vault',
          telemetry: 'Real-time Substrate & Photoperiod Telemetry',
          calendar: 'Prescribed Care Rhythm & Acclimation',
          orders: 'Archival Orders & Flora Certificates'
        };
        VerdantStore.showToast(tabNames[tabId] || 'Sanctuary View', 'Dashboard view updated.', 'dashboard', 'success');
      }

      function toggleDashTask(checkbox, taskName) {
        const row = checkbox.closest('div');
        if (checkbox.checked) {
          row.style.opacity = '0.5';
          VerdantStore.showToast('Task Completed', `${taskName} recorded in living botanical ledger.`, 'check_circle', 'success');
        } else {
          row.style.opacity = '1';
        }
      }
    </script>
    '''

    soup.body.append(BeautifulSoup(dash_script, 'html.parser'))

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced dashboard.html successfully!")

if __name__ == '__main__':
    enhance_dashboard()
