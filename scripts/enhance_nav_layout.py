with open('js/nav.js', 'r', encoding='utf-8') as f:
    nav_code = f.read()

# Replace SITE_PAGES with rich image-enabled version
old_pages = """const SITE_PAGES = [
  { id: 'home', file: 'index.html', title: 'Sanctuary Storefront', icon: 'storefront', section: 'Store', desc: 'Editorial homepage, rare drops & habitat curation' },
  { id: 'catalog', file: 'catalog.html', title: 'Curated Botanical Catalog', icon: 'potted_plant', section: 'Store', desc: 'Living cultivar archive, filters & search' },
  { id: 'product', file: 'product.html', title: 'Monstera Pot Customizer', icon: 'palette', section: 'Store', desc: 'Handcrafted vessels, sizing & seasonal care' },
  { id: 'checkout', file: 'checkout.html', title: 'Greenhouse Dispatch Checkout', icon: 'shopping_cart_checkout', section: 'Checkout', desc: 'Multi-step shipping, split pay & settlement' },
  { id: 'tracker', file: 'order-confirmation.html', title: 'Live Specimen Dispatch Tracker', icon: 'local_shipping', section: 'Logistics', desc: 'Courier milestones & real-time telemetry' },
  { id: 'invoice', file: 'invoice.html', title: 'Certificate of Provenance & Invoice', icon: 'receipt_long', section: 'Logistics', desc: 'Archival accession ledger & cryptographic seal' },
  { id: 'invoice-print', file: 'invoice-print.html', title: 'Dedicated Archival Print Mode', icon: 'print', section: 'Logistics', desc: 'High-res printable document preview' },
  { id: 'mailing-label', file: 'mailing-label.html', title: 'Archival Specimen Mailing Label', icon: 'mail', section: 'Logistics', desc: 'Greenhouse packaging label & customs declaration' },
  { id: 'care-lab', file: 'care-lab.html', title: 'Conservatory Care Lab & Doctor', icon: 'biotech', section: 'Care & Tele-Botany', desc: 'Foliar biometric triage & custom prescriptions' },
  { id: 'passport', file: 'passport.html', title: 'Living Plant Passport & Herbarium', icon: 'token', section: 'Care & Tele-Botany', desc: 'Digital herbarium, NFC sync & root scans' },
  { id: 'consultation', file: 'consultation.html', title: '1:1 Horticulturist Booking', icon: 'calendar_month', section: 'Care & Tele-Botany', desc: 'Schedule private unboxing & acclimation session' },
  { id: 'video-call', file: 'video-call.html', title: 'Live Tele-Horticulture Call Room', icon: 'videocam', section: 'Care & Tele-Botany', desc: 'Split-screen video call with Master Botanist' },
  { id: 'vitality', file: 'vitality-checkup.html', title: '30-Day Root Vitality Checkup', icon: 'vital_signs', section: 'Care & Tele-Botany', desc: 'Acclimation log & 90-day warranty extension' },
  { id: 'vitality-conf', file: 'vitality-confirmed.html', title: 'Vitality Checkup Confirmed', icon: 'task_alt', section: 'Care & Tele-Botany', desc: 'Appointment calendar invite & prep checklist' },
  { id: 'reviews', file: 'reviews.html', title: 'Client Feedback & Reviews', icon: 'reviews', section: 'Community', desc: 'Verified customer ratings & community photos' },
  { id: 'login', file: 'login.html', title: 'Sanctuary Member Sign In', icon: 'login', section: 'Vault Portal', desc: 'Vault authentication & 1-click demo access' },
  { id: 'account-link', file: 'account-link.html', title: 'Specimen Passport Linking', icon: 'link', section: 'Vault Portal', desc: 'Link accession NFC tags to personal account' },
  { id: 'dashboard', file: 'dashboard.html', title: 'Sanctuary Member Dashboard', icon: 'dashboard', section: 'Vault Portal', desc: 'Personal collection, live telemetry & care reminders' }
];"""

new_pages = """const SITE_PAGES = [
  { id: 'home', file: 'index.html', title: 'Sanctuary Storefront', icon: 'storefront', section: 'Store', desc: 'Editorial homepage, rare drops & habitat curation', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAt36WBgyJO7QXC-kMTNR6NBCKWAw8kBUecsgIosooxNcgAMvpdOe-dHlQ7XFPOL91mgNHtNhp1sm1Wi36yn55Txs59X5irrIk9F5z88lZX-ImweQ7ThfGz5rKlsAya4hJq9XQcL4j2q5birG76TPhR0uRP3qc0yC8AByfIyh5eUV-yzN2pE5fkemXcYMC6upnn0LR02FchS3-OdxOAdkFlS2GatZMIxjI4yqMa4u-14uLQdzEo9tLeiQ' },
  { id: 'catalog', file: 'catalog.html', title: 'Curated Botanical Catalog', icon: 'potted_plant', section: 'Store', desc: 'Living cultivar archive, filters & search', img: 'https://images.unsplash.com/photo-1545241047-6083a3684587?auto=format&fit=crop&w=400&q=80' },
  { id: 'product', file: 'product.html', title: 'Monstera Pot Customizer', icon: 'palette', section: 'Store', desc: 'Handcrafted vessels, sizing & seasonal care', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuChvYkunOOEVd-SSsdh7tWtQPCLADQecqR98ATlI2v5HybaDVCHqAEfQWL7WjPxI-I7HkDPhwincKGBjwewVjwpbVYStTDg-ezjui9B05HGUOSm48oketNy_IKtmQcFd7xA57BjsPK3dnrtpgXJ6bITqLiFfstnG0oo9U5nWieEt9zLo5DXK72qEglmC05OVzjWA_3eE85boa9YmxRL1ckKSNtiGTl8gStkI_DV35RMDdP0uC5QKSSfNQ' },
  { id: 'checkout', file: 'checkout.html', title: 'Greenhouse Dispatch Checkout', icon: 'shopping_cart_checkout', section: 'Checkout', desc: 'Multi-step shipping, split pay & settlement', img: 'https://images.unsplash.com/photo-1592150621744-aca64f48394a?auto=format&fit=crop&w=400&q=80' },
  { id: 'tracker', file: 'order-confirmation.html', title: 'Live Specimen Dispatch Tracker', icon: 'local_shipping', section: 'Logistics', desc: 'Courier milestones & real-time telemetry', img: 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=400&q=80' },
  { id: 'invoice', file: 'invoice.html', title: 'Certificate of Provenance & Invoice', icon: 'receipt_long', section: 'Logistics', desc: 'Archival accession ledger & cryptographic seal', img: 'https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=400&q=80' },
  { id: 'invoice-print', file: 'invoice-print.html', title: 'Dedicated Archival Print Mode', icon: 'print', section: 'Logistics', desc: 'High-res printable document preview', img: 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?auto=format&fit=crop&w=400&q=80' },
  { id: 'mailing-label', file: 'mailing-label.html', title: 'Archival Specimen Mailing Label', icon: 'mail', section: 'Logistics', desc: 'Greenhouse packaging label & customs declaration', img: 'https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=400&q=80' },
  { id: 'care-lab', file: 'care-lab.html', title: 'Conservatory Care Lab & Doctor', icon: 'biotech', section: 'Care & Tele-Botany', desc: 'Foliar biometric triage & custom prescriptions', img: 'https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?auto=format&fit=crop&w=400&q=80' },
  { id: 'passport', file: 'passport.html', title: 'Living Plant Passport & Herbarium', icon: 'token', section: 'Care & Tele-Botany', desc: 'Digital herbarium, NFC sync & root scans', img: 'https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=400&q=80' },
  { id: 'consultation', file: 'consultation.html', title: '1:1 Horticulturist Booking', icon: 'calendar_month', section: 'Care & Tele-Botany', desc: 'Schedule private unboxing & acclimation session', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCDumUoz5fK9nmtPAxxXKYUv5Y0n29maE6tsFDE6P3U-N41xuFIIVcyb6MCwqNT0gvlCjZUrnSjZnN0NdrF4SY8g7Twtc3dpbtt4Jqvuc_h3tV8CxrqxrWe2AIJcu4fKAeCvb0sQ53eRBA8Rmtb1G0GgcHErI1Q3pGc5M7xqnaWDX0cInByvZRS1vDLm_imwP3KVUSrYkMg1ULee7DLZjtQOZQ0OrwZDN4ERqrSGH1g1CPmFV1XRyDwUw' },
  { id: 'video-call', file: 'video-call.html', title: 'Live Tele-Horticulture Call Room', icon: 'videocam', section: 'Care & Tele-Botany', desc: 'Split-screen video call with Master Botanist', img: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80' },
  { id: 'vitality', file: 'vitality-checkup.html', title: '30-Day Root Vitality Checkup', icon: 'vital_signs', section: 'Care & Tele-Botany', desc: 'Acclimation log & 90-day warranty extension', img: 'https://images.unsplash.com/photo-1512428813834-c702c7702b78?auto=format&fit=crop&w=400&q=80' },
  { id: 'vitality-conf', file: 'vitality-confirmed.html', title: 'Vitality Checkup Confirmed', icon: 'task_alt', section: 'Care & Tele-Botany', desc: 'Appointment calendar invite & prep checklist', img: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80' },
  { id: 'reviews', file: 'reviews.html', title: 'Client Feedback & Reviews', icon: 'reviews', section: 'Community', desc: 'Verified customer ratings & community photos', img: 'https://images.unsplash.com/photo-1463936575829-25148e1db1b8?auto=format&fit=crop&w=400&q=80' },
  { id: 'login', file: 'login.html', title: 'Sanctuary Member Sign In', icon: 'login', section: 'Vault Portal', desc: 'Vault authentication & 1-click demo access', img: 'https://images.unsplash.com/photo-1470058869958-2a77ade41c02?auto=format&fit=crop&w=400&q=80' },
  { id: 'account-link', file: 'account-link.html', title: 'Specimen Passport Linking', icon: 'link', section: 'Vault Portal', desc: 'Link accession NFC tags to personal account', img: 'https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?auto=format&fit=crop&w=400&q=80' },
  { id: 'dashboard', file: 'dashboard.html', title: 'Sanctuary Member Dashboard', icon: 'dashboard', section: 'Vault Portal', desc: 'Personal collection, live telemetry & care reminders', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAsJdodqr88vCr-S-oOyPeMqoDOqhS4fvvXGL_1L4h3pKASw0EJR135p9gi0LrTwNbS6xKLEN_oinVaaROwPcsvxxvmG4w-ibAlVzOXQo_QJpfjwYM7rt5pgeXcvPv13d5-ajgM7I4DKBqFoyN3xkBWTJIo59iiaTtDqB9HMuNnG9ygCr9gfGquUuDB2N8QOqjOzToz2Gbp33kLLLC0DoEY6auzqYKD6BFR9DeQto64XLRvlSgzWb7teA' }
];"""

# Replace injectNextPageBanner with grand layout
old_banner = """function injectNextPageBanner() {
  // Only inject if not already present and if main exists
  const main = document.querySelector('main');
  if (!main || document.getElementById('verdant-next-page-section')) return;

  const currentIdx = getCurrentPageIndex();
  const next = SITE_PAGES[(currentIdx + 1) % SITE_PAGES.length];
  const prev = SITE_PAGES[(currentIdx - 1 + SITE_PAGES.length) % SITE_PAGES.length];

  const section = document.createElement('section');
  section.id = 'verdant-next-page-section';
  section.className = 'w-full py-12 px-margin max-w-[1320px] mx-auto border-t border-primary/10 mt-12 mb-8';

  section.innerHTML = `
    <div class="relative bg-gradient-to-r from-surface-container-low via-surface-container to-surface-container-low rounded-2xl p-8 md:p-10 shadow-sm border border-primary/10 flex flex-col md:flex-row md:items-center justify-between gap-6 overflow-hidden">
      <div class="space-y-1.5 max-w-xl z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-surface-container-lowest text-secondary text-xs uppercase tracking-widest font-bold shadow-sm">
          <span class="w-2 h-2 rounded-full bg-secondary"></span>
          Sanctuary Journey • Step ${currentIdx + 1} of ${SITE_PAGES.length}
        </div>
        <h3 class="font-headline-sm text-primary font-serif">Continue to ${next.title}</h3>
        <p class="font-body-sm text-on-surface-variant">${next.desc}. Experience the complete architectural botanical sanctuary.</p>
      </div>

      <div class="flex items-center gap-3 z-10 shrink-0">
        <a href="${prev.file}" class="px-5 py-3 rounded-xl bg-surface-container-lowest text-on-surface font-label-lg text-sm hover:bg-surface shadow-sm transition-all flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">arrow_back</span>
          <span>Previous</span>
        </a>
        <a href="${next.file}" class="px-7 py-3 rounded-xl bg-primary text-on-primary font-label-lg text-sm hover:bg-primary-container shadow-md hover:shadow-lg transition-all flex items-center gap-2">
          <span>Proceed to ${next.title.split(' ')[0]}</span>
          <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
        </a>
      </div>

      <!-- Subtle background foliage watermark -->
      <div class="absolute right-0 bottom-0 top-0 w-64 opacity-5 pointer-events-none flex items-center justify-end pr-4">
        <span class="material-symbols-outlined text-[180px] text-primary">potted_plant</span>
      </div>
    </div>
  `;

  // Append before footer
  main.appendChild(section);
}"""

new_banner = """function injectNextPageBanner() {
  const main = document.querySelector('main');
  if (!main || document.getElementById('verdant-next-page-section')) return;

  const currentIdx = getCurrentPageIndex();
  const current = SITE_PAGES[currentIdx];
  const next = SITE_PAGES[(currentIdx + 1) % SITE_PAGES.length];
  const prev = SITE_PAGES[(currentIdx - 1 + SITE_PAGES.length) % SITE_PAGES.length];
  const progressPct = Math.round(((currentIdx + 1) / SITE_PAGES.length) * 100);

  const section = document.createElement('section');
  section.id = 'verdant-next-page-section';
  section.className = 'w-full py-16 px-margin-mobile md:px-margin max-w-[1320px] mx-auto border-t border-primary/10 mt-16 mb-12';

  section.innerHTML = `
    <!-- ARCHITECTURAL NEXT CHAPTER HERO CARD -->
    <div class="relative bg-gradient-to-br from-surface-container-lowest via-surface-container-low to-surface-container rounded-3xl p-6 sm:p-10 lg:p-12 shadow-xl border border-primary/15 overflow-hidden">
      <!-- Top Journey Meta & Step Tracker -->
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-8 border-b border-primary/10 relative z-10">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold font-serif text-sm shadow-sm">
            ${currentIdx + 1}
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-widest text-secondary font-mono">Sanctuary Journey Roadmap</span>
              <span class="text-outline text-xs">•</span>
              <span class="text-[11px] font-semibold text-primary">Step ${currentIdx + 1} of ${SITE_PAGES.length}</span>
            </div>
            <h4 class="font-headline-sm text-base text-primary font-serif font-bold">Currently Viewing: ${current.title}</h4>
          </div>
        </div>

        <!-- Progress Tracker Bar -->
        <div class="flex items-center gap-3 w-full sm:w-auto">
          <div class="w-36 h-2 rounded-full bg-surface-container-highest overflow-hidden hidden sm:block">
            <div class="h-full bg-gradient-to-r from-secondary to-primary rounded-full transition-all duration-700" style="width: ${progressPct}%;"></div>
          </div>
          <span class="text-xs font-bold text-secondary font-mono">${progressPct}% Complete</span>
          <button onclick="openSiteMapDrawer()" class="px-3 py-1.5 rounded-full bg-surface-container text-primary hover:bg-surface-container-high text-xs font-semibold flex items-center gap-1 transition-all">
            <span class="material-symbols-outlined text-[15px]">grid_view</span>
            <span>All Pages</span>
          </button>
        </div>
      </div>

      <!-- Main Next Page Architectural Preview Layout -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center pt-8 relative z-10">
        <!-- Left: High-Res Next Destination Thumbnail Preview -->
        <a href="${next.file}" class="lg:col-span-5 relative group overflow-hidden rounded-2xl shadow-lg aspect-[16/10] bg-surface-container block">
          <img src="${next.img}" alt="${next.title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
          <div class="absolute inset-0 bg-gradient-to-t from-primary/80 via-primary/20 to-transparent"></div>
          <div class="absolute top-4 left-4">
            <span class="px-3 py-1 rounded-full bg-surface/90 backdrop-blur-md text-primary text-xs font-bold uppercase tracking-wider shadow-sm flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[15px] text-secondary">${next.icon}</span>
              <span>Up Next • ${next.section}</span>
            </span>
          </div>
          <div class="absolute bottom-4 left-4 right-4 text-on-primary">
            <h3 class="font-headline-sm text-lg font-serif font-bold leading-tight drop-shadow-sm">${next.title}</h3>
            <p class="text-xs text-on-primary/90 mt-1 line-clamp-1 drop-shadow-sm">${next.desc}</p>
          </div>
          <div class="absolute bottom-4 right-4 w-9 h-9 rounded-full bg-on-primary text-primary flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity shadow-lg">
            <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
          </div>
        </a>

        <!-- Right: Guided Editorial Narrative & Big Action Buttons -->
        <div class="lg:col-span-7 flex flex-col justify-between space-y-6">
          <div class="space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-secondary-container/60 text-on-secondary-fixed text-xs font-bold uppercase tracking-widest">
              <span class="w-2 h-2 rounded-full bg-secondary"></span>
              Recommended Next Sanctuary Chapter
            </div>
            <h2 class="font-headline-lg text-headline-sm sm:text-headline-md text-primary font-serif">
              Continue Your Exploration to <span class="italic text-primary-container">${next.title}</span>
            </h2>
            <p class="font-body-md text-sm text-on-surface-variant leading-relaxed">
              ${next.desc}. Step inside our continuous living botanical workflow — connecting glasshouse sourcing, customized terracotta potting, courier telemetry, foliar care labs, and collector member dashboards.
            </p>
          </div>

          <!-- Dual Navigation Actions -->
          <div class="flex flex-wrap items-center gap-3 pt-2">
            <a href="${prev.file}" class="px-5 py-3.5 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-lg text-sm font-semibold transition-all flex items-center gap-2 active:scale-95">
              <span class="material-symbols-outlined text-[18px]">arrow_back</span>
              <span>Back: ${prev.title.split(' ')[0]}</span>
            </a>
            <a href="${next.file}" class="px-8 py-3.5 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-lg text-sm font-bold shadow-lg hover:shadow-xl transition-all flex items-center gap-2.5 active:scale-95">
              <span>Proceed to ${next.title}</span>
              <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Atmospheric background foliage watermark -->
      <div class="absolute -right-10 -bottom-10 opacity-[0.035] pointer-events-none select-none">
        <span class="material-symbols-outlined text-[320px] text-primary">eco</span>
      </div>
    </div>
  `;

  main.appendChild(section);
}"""

if old_pages in nav_code and old_banner in nav_code:
    nav_code = nav_code.replace(old_pages, new_pages).replace(old_banner, new_banner)
    with open('js/nav.js', 'w', encoding='utf-8') as f:
        f.write(nav_code)
    print("Successfully enhanced js/nav.js with rich next page layout and images!")
else:
    print("Could not find exact strings in js/nav.js")
