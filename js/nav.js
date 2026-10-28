// ==========================================================================
// Verdant Haven — Global Navigation, Tour Bar & Interactive Systems
// ==========================================================================

const SITE_PAGES = [
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
];

document.addEventListener('DOMContentLoaded', () => {
  initCartDrawer();
  initQuizModal();
  initPolicyModal();
  initGlobalHeaderAndLinks();
  initCurrencySwitcher();
  initSearchAutocomplete();
  updateHeaderBadges();
  injectFloatingTourBar();
  injectNextPageBanner();
});

// --------------------------------------------------------------------------
// 1. FLOATING SANCTUARY TOUR & NEXT PAGE BAR
// --------------------------------------------------------------------------
function getCurrentPageIndex() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const idx = SITE_PAGES.findIndex(p => p.file === currentPath);
  return idx > -1 ? idx : 0;
}

function injectFloatingTourBar() {
  if (document.getElementById('verdant-tour-bar')) return;

  const currentIdx = getCurrentPageIndex();
  const current = SITE_PAGES[currentIdx];
  const prev = SITE_PAGES[(currentIdx - 1 + SITE_PAGES.length) % SITE_PAGES.length];
  const next = SITE_PAGES[(currentIdx + 1) % SITE_PAGES.length];

  const bar = document.createElement('div');
  bar.id = 'verdant-tour-bar';
  bar.className = 'fixed bottom-5 left-1/2 -translate-x-1/2 z-[9970] flex items-center gap-1.5 p-1.5 bg-primary/95 text-on-primary rounded-full shadow-[0_8px_32px_rgba(0,54,41,0.35)] backdrop-blur-xl border border-primary-fixed/25 transition-all duration-300';
  
  bar.innerHTML = `
    <!-- Prev Page -->
    <a href="${prev.file}" title="Previous: ${prev.title}" class="flex items-center gap-1 px-3 py-1.5 rounded-full hover:bg-primary-container text-xs font-semibold text-on-primary/90 hover:text-on-primary transition-colors">
      <span class="material-symbols-outlined text-[16px]">arrow_back</span>
      <span class="hidden md:inline">${prev.title.split(' ')[0]}</span>
    </a>

    <!-- Current Page Pill & Site Drawer Trigger -->
    <button id="openSiteDrawerBtn" class="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-surface-container-lowest text-primary text-xs font-bold shadow-sm hover:bg-surface transition-all">
      <span class="w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
      <span class="truncate max-w-[140px] sm:max-w-[200px]">${current.title}</span>
      <span class="material-symbols-outlined text-[15px] text-secondary">grid_view</span>
    </button>

    <!-- Next Page -->
    <a href="${next.file}" title="Next: ${next.title}" class="flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-secondary-fixed text-on-secondary-fixed hover:bg-secondary-fixed-dim text-xs font-bold shadow-md transition-all active:scale-95">
      <span>Next: <span class="hidden sm:inline">${next.title}</span><span class="sm:hidden">Page</span></span>
      <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
    </a>
  `;

  document.body.appendChild(bar);

  // Inject Full Site Map Drawer
  injectSiteMapDrawer();

  const openDrawerBtn = document.getElementById('openSiteDrawerBtn');
  if (openDrawerBtn) {
    openDrawerBtn.addEventListener('click', () => {
      openSiteMapDrawer();
    });
  }
}

function injectSiteMapDrawer() {
  if (document.getElementById('siteMapDrawer')) return;

  const drawerWrap = document.createElement('div');
  drawerWrap.innerHTML = `
    <div id="siteMapBackdrop" class="fixed inset-0 bg-inverse-surface/60 backdrop-blur-sm z-[9985] opacity-0 pointer-events-none transition-opacity duration-300"></div>
    <div id="siteMapDrawer" class="fixed bottom-0 left-0 right-0 max-h-[85vh] z-[9990] bg-background rounded-t-3xl shadow-2xl p-6 md:p-8 overflow-y-auto transform translate-y-full transition-transform duration-300 ease-out border-t border-primary/10">
      <div class="max-w-5xl mx-auto flex flex-col gap-6">
        <!-- Header -->
        <div class="flex items-center justify-between pb-4 border-b border-primary/10">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-primary text-on-primary flex items-center justify-center">
              <span class="material-symbols-outlined text-[22px]">explore</span>
            </div>
            <div>
              <h3 class="font-headline-sm text-primary font-serif">Verdant Haven Sanctuary Map</h3>
              <p class="font-label-sm text-on-surface-variant">Access all 18 functional pages across our botanical atelier</p>
            </div>
          </div>
          <button id="closeSiteDrawerBtn" class="w-9 h-9 rounded-full bg-surface-container text-on-surface-variant hover:text-primary flex items-center justify-center transition-colors">
            <span class="material-symbols-outlined text-[20px]">close</span>
          </button>
        </div>

        <!-- Pages Grid by Section -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4" id="siteMapGrid">
          ${SITE_PAGES.map((p, idx) => {
            const isCurrent = (window.location.pathname.split('/').pop() || 'index.html') === p.file;
            return `
              <a href="${p.file}" class="p-4 rounded-xl border ${isCurrent ? 'border-primary bg-primary/5 ring-2 ring-primary/20' : 'border-outline-variant/40 bg-surface-container-lowest hover:border-primary'} transition-all flex flex-col justify-between group">
                <div class="flex items-start justify-between gap-2 mb-2">
                  <div class="w-8 h-8 rounded-lg ${isCurrent ? 'bg-primary text-on-primary' : 'bg-surface-container text-primary group-hover:bg-primary group-hover:text-on-primary'} flex items-center justify-center transition-colors">
                    <span class="material-symbols-outlined text-[18px]">${p.icon}</span>
                  </div>
                  <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full ${isCurrent ? 'bg-primary text-on-primary' : 'bg-surface-container text-secondary'}">
                    ${isCurrent ? 'Current' : p.section}
                  </span>
                </div>
                <div>
                  <h4 class="font-title-md text-sm text-primary font-bold group-hover:text-primary-container transition-colors">${p.title}</h4>
                  <p class="font-body-sm text-[11px] text-on-surface-variant mt-0.5 line-clamp-1">${p.desc}</p>
                </div>
              </a>
            `;
          }).join('')}
        </div>
      </div>
    </div>
  `;

  document.body.appendChild(drawerWrap);

  const closeBtn = document.getElementById('closeSiteDrawerBtn');
  const backdrop = document.getElementById('siteMapBackdrop');
  if (closeBtn) closeBtn.onclick = closeSiteMapDrawer;
  if (backdrop) backdrop.onclick = closeSiteMapDrawer;
}

function openSiteMapDrawer() {
  const drawer = document.getElementById('siteMapDrawer');
  const backdrop = document.getElementById('siteMapBackdrop');
  if (!drawer || !backdrop) return;
  backdrop.classList.remove('opacity-0', 'pointer-events-none');
  backdrop.classList.add('opacity-100', 'pointer-events-auto');
  drawer.classList.remove('translate-y-full');
}

function closeSiteMapDrawer() {
  const drawer = document.getElementById('siteMapDrawer');
  const backdrop = document.getElementById('siteMapBackdrop');
  if (!drawer || !backdrop) return;
  backdrop.classList.remove('opacity-100', 'pointer-events-auto');
  backdrop.classList.add('opacity-0', 'pointer-events-none');
  drawer.classList.add('translate-y-full');
}

// --------------------------------------------------------------------------
// 2. IN-PAGE "NEXT SANCTUARY STAGE" EDITORIAL BANNER
// --------------------------------------------------------------------------
function injectNextPageBanner() {
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
}

// --------------------------------------------------------------------------
// 3. CART DRAWER COMPONENT
// --------------------------------------------------------------------------
function initCartDrawer() {
  let drawer = document.getElementById('cartDrawer');
  let backdrop = document.getElementById('cartBackdrop');

  if (!drawer) {
    const drawerWrapper = document.createElement('div');
    drawerWrapper.innerHTML = `
      <div id="cartBackdrop" class="fixed inset-0 bg-inverse-surface/50 backdrop-blur-sm z-[9990] opacity-0 pointer-events-none transition-opacity duration-300"></div>
      <aside id="cartDrawer" class="fixed top-0 right-0 h-full w-full max-w-[500px] z-[9995] bg-background shadow-2xl flex flex-col justify-between overflow-hidden transform translate-x-full transition-transform duration-300 ease-out">
        <!-- 1. HEADER & FREE SHIPPING METER -->
        <div class="bg-surface-container-low px-space-lg pt-space-lg pb-space-md shrink-0 shadow-sm border-b border-primary/5">
          <div class="flex items-center justify-between pb-space-sm">
            <div class="flex items-center gap-space-xs">
              <span class="material-symbols-outlined text-primary text-[22px]">local_florist</span>
              <h2 class="font-headline-sm text-headline-sm text-primary font-serif tracking-tight">Botanical Bag</h2>
              <span id="drawerCartCount" class="px-2.5 py-0.5 rounded-full bg-primary-fixed text-on-primary-fixed font-label-sm text-label-sm font-semibold tracking-wide ml-1">0 Items</span>
            </div>
            <button id="closeCartBtn" class="w-9 h-9 rounded-full bg-surface hover:bg-surface-container-highest text-on-surface-variant hover:text-primary transition-colors flex items-center justify-center">
              <span class="material-symbols-outlined text-[20px]">close</span>
            </button>
          </div>
          <!-- Shipping Milestone Progress Module -->
          <div class="mt-space-xs bg-surface-container-lowest rounded-xl p-space-sm flex flex-col gap-space-xs border border-primary/5">
            <div class="flex items-center justify-between font-label-sm text-label-sm">
              <div class="flex items-center gap-1.5 text-primary font-medium">
                <span class="material-symbols-outlined text-[16px] text-secondary">mode_heat</span>
                <span>Greenhouse Thermal Express Shipping</span>
              </div>
              <span id="shippingNoticeText" class="text-tertiary font-bold tracking-tight">$26.00 to unlock</span>
            </div>
            <div class="w-full h-2 rounded-full bg-surface-container overflow-hidden relative">
              <div id="shippingProgressBar" class="h-full bg-gradient-to-r from-secondary to-primary-container rounded-full transition-all duration-500 ease-out" style="width: 0%;"></div>
            </div>
            <p class="font-body-sm text-[12px] text-on-surface-variant flex items-center justify-between pt-0.5">
              <span>Current: <strong id="progressCartAmount" class="text-on-surface font-semibold">$0.00</strong></span>
              <span class="text-outline">Tier Target: $120.00</span>
            </p>
          </div>
        </div>

        <!-- 2. SCROLLABLE CART CONTENTS -->
        <div id="drawerCartItems" class="flex-1 overflow-y-auto px-space-lg py-space-md flex flex-col gap-space-md">
          <!-- Dynamically populated -->
        </div>

        <!-- 3. FOOTER & CHECKOUT SUMMARY -->
        <div class="bg-surface-container-low/90 backdrop-blur-md px-space-lg py-space-md shrink-0 shadow-[0_-4px_20px_rgba(0,0,0,0.05)] border-t border-primary/5 flex flex-col gap-space-sm">
          <!-- Heat pack add-on -->
          <label class="flex items-center gap-2 p-2 bg-surface-container-lowest rounded-lg cursor-pointer text-[13px] text-on-surface select-none">
            <input type="checkbox" id="thermalPackToggle" checked class="w-4 h-4 rounded text-primary accent-primary" />
            <span class="material-symbols-outlined text-[18px] text-secondary">thermostat</span>
            <span class="flex-1">Add Thermal Insulation & 72h UniHeat Pack</span>
            <span class="font-semibold text-primary">+$4.50</span>
          </label>

          <!-- Promo code toggle -->
          <div class="flex items-center gap-2">
            <input type="text" id="drawerPromoInput" placeholder="Promo code (try VERDANT10)" class="flex-1 px-3 py-1.5 text-xs bg-surface-container-lowest border border-outline-variant/60 rounded-lg uppercase tracking-wider focus:outline-none focus:ring-1 focus:ring-primary" />
            <button id="applyPromoBtn" class="px-3 py-1.5 bg-surface text-primary text-xs font-semibold rounded-lg hover:bg-surface-container transition-colors">Apply</button>
          </div>
          <div id="promoSuccessMessage" class="hidden text-[12px] text-secondary font-semibold flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">check</span> 10% Botanical Privilege Applied!
          </div>

          <!-- Financial breakdown -->
          <div class="flex flex-col gap-1 pt-1 border-t border-outline-variant/30 text-body-sm text-on-surface-variant text-[13px]">
            <div class="flex justify-between">
              <span>Specimens Subtotal</span>
              <span id="drawerSubtotal" class="font-medium text-on-surface">$0.00</span>
            </div>
            <div id="drawerDiscountRow" class="hidden flex justify-between text-secondary">
              <span>Sanctuary Discount (10%)</span>
              <span id="drawerDiscount">-$0.00</span>
            </div>
            <div class="flex justify-between">
              <span>Greenhouse Courier Transit</span>
              <span id="drawerShippingRate" class="font-medium text-secondary">Complimentary</span>
            </div>
            <div class="flex justify-between pt-1 border-t border-outline-variant/30 text-base font-bold text-primary font-serif">
              <span>Estimated Settlement</span>
              <span id="drawerFinalTotal">$0.00</span>
            </div>
          </div>

          <!-- Checkout CTA -->
          <a href="checkout.html" id="proceedToCheckoutBtn" class="w-full py-3.5 px-6 bg-primary hover:bg-primary-container text-on-primary font-label-lg text-label-lg rounded-xl shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2 mt-1">
            <span>Proceed to Greenhouse Dispatch</span>
            <span class="material-symbols-outlined text-[18px]">lock</span>
          </a>
          <p class="text-center font-body-sm text-[11px] text-on-surface-variant flex items-center justify-center gap-1">
            <span class="material-symbols-outlined text-[13px] text-secondary">security</span>
            30-Day Guaranteed Arrive-Alive Sanctuary Protocol
          </p>
        </div>
      </aside>
    `;
    document.body.appendChild(drawerWrapper);
    drawer = document.getElementById('cartDrawer');
    backdrop = document.getElementById('cartBackdrop');
  }

  // Event Listeners for Open / Close
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-path="cart"], a[href="#cart"], a[href="cart.html"], .cart-toggle, [aria-label="Shopping Cart"]');
    if (trigger) {
      e.preventDefault();
      openCartDrawer();
    }
  });

  const closeBtn = document.getElementById('closeCartBtn');
  if (closeBtn) closeBtn.addEventListener('click', closeCartDrawer);
  if (backdrop) backdrop.addEventListener('click', closeCartDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeCartDrawer();
  });

  // Promo Code
  const promoBtn = document.getElementById('applyPromoBtn');
  if (promoBtn) {
    promoBtn.addEventListener('click', () => {
      const input = document.getElementById('drawerPromoInput');
      const msg = document.getElementById('promoSuccessMessage');
      if (input && input.value.trim().toUpperCase() === 'VERDANT10') {
        sessionStorage.setItem('verdant_promo_code', 'VERDANT10');
        if (msg) msg.classList.remove('hidden');
        VerdantStore.showToast('Promo Code Applied', '10% privilege discount activated.', 'percent', 'success');
        renderCartDrawerItems();
      } else {
        VerdantStore.showToast('Invalid Code', 'Try "VERDANT10" for 10% botanical discount.', 'error', 'error');
      }
    });
  }

  const thermalToggle = document.getElementById('thermalPackToggle');
  if (thermalToggle) {
    thermalToggle.addEventListener('change', () => {
      renderCartDrawerItems();
    });
  }

  // Listen to store updates
  window.addEventListener('verdant:cart-updated', () => {
    renderCartDrawerItems();
    updateHeaderBadges();
  });

  window.addEventListener('verdant:currency-updated', () => {
    renderCartDrawerItems();
  });

  renderCartDrawerItems();
}

function openCartDrawer() {
  const drawer = document.getElementById('cartDrawer');
  const backdrop = document.getElementById('cartBackdrop');
  if (!drawer || !backdrop) return;

  renderCartDrawerItems();

  backdrop.classList.remove('opacity-0', 'pointer-events-none');
  backdrop.classList.add('opacity-100', 'pointer-events-auto');
  drawer.classList.remove('translate-x-full');
  document.body.style.overflow = 'hidden';
}

function closeCartDrawer() {
  const drawer = document.getElementById('cartDrawer');
  const backdrop = document.getElementById('cartBackdrop');
  if (!drawer || !backdrop) return;

  backdrop.classList.remove('opacity-100', 'pointer-events-auto');
  backdrop.classList.add('opacity-0', 'pointer-events-none');
  drawer.classList.add('translate-x-full');
  document.body.style.overflow = '';
}

function renderCartDrawerItems() {
  const container = document.getElementById('drawerCartItems');
  if (!container) return;

  const cart = VerdantStore.getCart();
  const count = VerdantStore.getCartCount();
  const subtotal = VerdantStore.getCartSubtotal();

  const countBadge = document.getElementById('drawerCartCount');
  if (countBadge) countBadge.textContent = `${count} ${count === 1 ? 'Item' : 'Items'}`;

  // Shipping progress calculation (Target $120)
  const shippingTarget = 120;
  const progressPct = Math.min(100, (subtotal / shippingTarget) * 100);
  const progressBar = document.getElementById('shippingProgressBar');
  const progressAmount = document.getElementById('progressCartAmount');
  const noticeText = document.getElementById('shippingNoticeText');

  if (progressBar) progressBar.style.width = `${progressPct}%`;
  if (progressAmount) progressAmount.textContent = VerdantStore.formatPrice(subtotal);

  if (noticeText) {
    if (subtotal >= shippingTarget) {
      noticeText.textContent = 'Unlocked! Complimentary Express';
      noticeText.classList.remove('text-tertiary');
      noticeText.classList.add('text-secondary');
    } else {
      const diff = shippingTarget - subtotal;
      noticeText.textContent = `${VerdantStore.formatPrice(diff)} to unlock`;
      noticeText.classList.remove('text-secondary');
      noticeText.classList.add('text-tertiary');
    }
  }

  // Empty state
  if (cart.length === 0) {
    container.innerHTML = `
      <div class="flex-1 flex flex-col items-center justify-center text-center p-8">
        <div class="w-16 h-16 rounded-full bg-surface-container flex items-center justify-center text-primary/40 mb-3">
          <span class="material-symbols-outlined text-[32px]">potted_plant</span>
        </div>
        <h3 class="font-headline-sm text-primary font-serif">Your Botanical Bag is Empty</h3>
        <p class="font-body-sm text-on-surface-variant max-w-xs mt-1 mb-6">Explore our curated glasshouse collection and select acclimated specimens for your home sanctuary.</p>
        <a href="catalog.html" onclick="closeCartDrawer()" class="px-6 py-2.5 bg-primary text-on-primary rounded-lg font-label-lg text-label-lg shadow-sm hover:bg-primary-container transition-colors">
          Browse Specimen Archive
        </a>
      </div>
    `;
    const checkoutBtn = document.getElementById('proceedToCheckoutBtn');
    if (checkoutBtn) checkoutBtn.classList.add('opacity-50', 'pointer-events-none');
    updateFinancialSummary(0);
    return;
  }

  const checkoutBtn = document.getElementById('proceedToCheckoutBtn');
  if (checkoutBtn) checkoutBtn.classList.remove('opacity-50', 'pointer-events-none');

  container.innerHTML = cart.map((item, idx) => `
    <div class="bg-surface-container-lowest rounded-xl p-space-md shadow-sm border border-primary/5 flex flex-col gap-2 relative group hover:shadow-md transition-shadow">
      <div class="flex gap-space-md">
        <div class="w-20 h-24 rounded-lg bg-surface-container-low overflow-hidden shrink-0 relative">
          <img src="${item.image}" alt="${item.name}" class="w-full h-full object-cover" />
          <span class="absolute bottom-1 left-1 px-1.5 py-0.2 rounded bg-primary/90 text-on-primary font-label-sm text-[9px] uppercase font-bold tracking-wider">
            Acclimated
          </span>
        </div>
        <div class="flex-1 min-w-0 flex flex-col justify-between">
          <div>
            <div class="flex items-start justify-between gap-1">
              <div>
                <h3 class="font-title-md text-[16px] text-primary font-serif leading-snug truncate">${item.name}</h3>
                <p class="font-body-sm text-[12px] text-on-surface-variant italic">${item.binomial || 'Cultivar Specimen'}</p>
              </div>
              <button aria-label="Remove specimen" onclick="VerdantStore.removeFromCart(${idx})" class="text-outline hover:text-error transition-colors p-1 -mr-1">
                <span class="material-symbols-outlined text-[18px]">delete_outline</span>
              </button>
            </div>
            <div class="flex flex-wrap gap-1 mt-1 text-[11px] font-label-sm text-secondary">
              <span class="bg-secondary/10 px-1.5 py-0.5 rounded">${item.size || 'Medium'}</span>
              <span class="bg-surface-container px-1.5 py-0.5 rounded text-on-surface-variant">${item.vessel || 'Terracotta Natural'}</span>
              ${item.drainageTray ? '<span class="bg-surface-container px-1.5 py-0.5 rounded text-on-surface-variant">+ Saucer</span>' : ''}
            </div>
          </div>
          <div class="flex items-center justify-between pt-2">
            <span class="font-title-md text-primary font-bold">${VerdantStore.formatPrice(item.price * item.quantity)}</span>
            <div class="flex items-center border border-outline-variant/60 rounded-lg bg-surface-container-low">
              <button onclick="VerdantStore.updateQuantity(${idx}, -1)" class="w-7 h-7 flex items-center justify-center text-on-surface-variant hover:text-primary transition-colors text-sm font-bold">-</button>
              <span class="w-8 text-center text-xs font-semibold text-on-surface">${item.quantity}</span>
              <button onclick="VerdantStore.updateQuantity(${idx}, 1)" class="w-7 h-7 flex items-center justify-center text-on-surface-variant hover:text-primary transition-colors text-sm font-bold">+</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  `).join('');

  updateFinancialSummary(subtotal);
}

function updateFinancialSummary(subtotal) {
  const drawerSubtotal = document.getElementById('drawerSubtotal');
  const drawerShipping = document.getElementById('drawerShippingRate');
  const drawerFinal = document.getElementById('drawerFinalTotal');
  const discountRow = document.getElementById('drawerDiscountRow');
  const discountAmount = document.getElementById('drawerDiscount');
  const thermalToggle = document.getElementById('thermalPackToggle');

  const hasPromo = sessionStorage.getItem('verdant_promo_code') === 'VERDANT10';
  const discount = hasPromo ? subtotal * 0.10 : 0;
  const thermal = (thermalToggle && thermalToggle.checked && subtotal > 0) ? 4.50 : 0;
  const shipping = subtotal >= 120 || subtotal === 0 ? 0 : 15.00;

  if (drawerSubtotal) drawerSubtotal.textContent = VerdantStore.formatPrice(subtotal);

  if (discountRow) {
    if (hasPromo && subtotal > 0) {
      discountRow.classList.remove('hidden');
      if (discountAmount) discountAmount.textContent = `-${VerdantStore.formatPrice(discount)}`;
    } else {
      discountRow.classList.add('hidden');
    }
  }

  if (drawerShipping) {
    drawerShipping.textContent = shipping === 0 ? 'Complimentary' : VerdantStore.formatPrice(shipping);
  }

  const finalTotal = Math.max(0, subtotal - discount + thermal + shipping);
  if (drawerFinal) drawerFinal.textContent = VerdantStore.formatPrice(finalTotal);
}

// --------------------------------------------------------------------------
// 4. PLANT QUIZ MODAL
// --------------------------------------------------------------------------
function initQuizModal() {
  let modal = document.getElementById('plantQuizModal');
  if (!modal) {
    const modalWrap = document.createElement('div');
    modalWrap.innerHTML = `
      <div id="plantQuizModal" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 bg-inverse-surface/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
        <div class="bg-background w-full max-w-xl rounded-2xl shadow-2xl overflow-hidden border border-primary/10 flex flex-col transform scale-95 transition-transform duration-300" id="quizCard">
          <div class="bg-surface-container-low p-6 border-b border-primary/5 flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-secondary/10 flex items-center justify-center text-secondary">
                <span class="material-symbols-outlined text-[22px]">psychology_alt</span>
              </div>
              <div>
                <h3 class="font-headline-sm text-primary font-serif">Botanical Sanctuary Quiz</h3>
                <p class="font-label-sm text-on-surface-variant">Find the ideal specimen tailored to your light & lifestyle</p>
              </div>
            </div>
            <button id="closeQuizBtn" class="w-8 h-8 rounded-full bg-surface text-outline hover:text-primary flex items-center justify-center transition-colors">
              <span class="material-symbols-outlined text-[18px]">close</span>
            </button>
          </div>

          <div class="px-6 pt-4 flex items-center gap-2" id="quizStepsIndicator">
            <div class="flex-1 h-1.5 rounded-full bg-primary transition-all step-bar-1"></div>
            <div class="flex-1 h-1.5 rounded-full bg-surface-container-highest transition-all step-bar-2"></div>
            <div class="flex-1 h-1.5 rounded-full bg-surface-container-highest transition-all step-bar-3"></div>
          </div>

          <div class="p-6 flex-1" id="quizBody">
            <div id="quizStep1" class="space-y-4">
              <span class="font-label-sm text-secondary uppercase tracking-widest font-bold">Step 1 of 3</span>
              <h4 class="font-title-lg text-primary">What natural lighting is available in your designated sanctuary space?</h4>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                <button onclick="selectQuizAnswer('light', 'low', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">nightlight</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Low Light</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">North-facing or recessed rooms</span>
                </button>
                <button onclick="selectQuizAnswer('light', 'medium', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">wb_twilight</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Bright Indirect</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">East/West sun filtered by curtains</span>
                </button>
                <button onclick="selectQuizAnswer('light', 'direct', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">wb_sunny</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Direct Sun</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">South-facing bay window floor</span>
                </button>
              </div>
            </div>

            <div id="quizStep2" class="space-y-4 hidden">
              <span class="font-label-sm text-secondary uppercase tracking-widest font-bold">Step 2 of 3</span>
              <h4 class="font-title-lg text-primary">What is your botanical experience & watering routine?</h4>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                <button onclick="selectQuizAnswer('care', 'easy', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">spa</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Beginner Friendly</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">Forgiving if I forget watering</span>
                </button>
                <button onclick="selectQuizAnswer('care', 'moderate', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">water_drop</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Conscientious</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">Happy with scheduled weekly soak</span>
                </button>
                <button onclick="selectQuizAnswer('care', 'advanced', this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex flex-col gap-1">
                  <span class="material-symbols-outlined text-secondary text-[24px]">biotech</span>
                  <span class="font-title-md text-primary text-[15px] font-bold">Master Collector</span>
                  <span class="font-body-sm text-[12px] text-on-surface-variant">Ready for humidity dome & telemetry</span>
                </button>
              </div>
            </div>

            <div id="quizStep3" class="space-y-4 hidden">
              <span class="font-label-sm text-secondary uppercase tracking-widest font-bold">Step 3 of 3</span>
              <h4 class="font-title-lg text-primary">Do you share your sanctuary with curious furry companions?</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                <button onclick="selectQuizAnswer('pet', true, this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex items-start gap-3">
                  <span class="material-symbols-outlined text-secondary text-[28px]">pets</span>
                  <div>
                    <span class="font-title-md text-primary text-[15px] font-bold block">100% Pet-Safe Required</span>
                    <span class="font-body-sm text-[12px] text-on-surface-variant">Non-toxic according to ASPCA verified criteria</span>
                  </div>
                </button>
                <button onclick="selectQuizAnswer('pet', false, this)" class="quiz-option p-4 rounded-xl border border-outline-variant/60 bg-surface-container-lowest hover:border-primary text-left transition-all flex items-start gap-3">
                  <span class="material-symbols-outlined text-secondary text-[28px]">yard</span>
                  <div>
                    <span class="font-title-md text-primary text-[15px] font-bold block">No Pets / Placed High</span>
                    <span class="font-body-sm text-[12px] text-on-surface-variant">Open to all architectural aroids and ficus</span>
                  </div>
                </button>
              </div>
            </div>

            <div id="quizResult" class="space-y-4 hidden text-center py-2">
              <div class="w-12 h-12 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center mx-auto">
                <span class="material-symbols-outlined text-[24px]">verified</span>
              </div>
              <span class="font-label-sm text-secondary uppercase tracking-widest font-bold block">Your Botanical Match</span>
              <h4 id="resultName" class="font-headline-md text-primary font-serif">Monstera Deliciosa</h4>
              <p id="resultDesc" class="font-body-sm text-on-surface-variant max-w-md mx-auto"></p>
              
              <div class="p-4 bg-surface-container-low rounded-xl flex items-center gap-4 text-left max-w-md mx-auto">
                <img id="resultImg" class="w-16 h-20 rounded-lg object-cover" src="" alt="Matched specimen" />
                <div class="flex-1 min-w-0">
                  <h5 id="resultBinomial" class="font-title-md text-primary italic text-sm"></h5>
                  <p id="resultTag" class="font-label-sm text-xs text-secondary"></p>
                  <p id="resultPrice" class="font-title-lg text-primary font-bold mt-1"></p>
                </div>
              </div>

              <div class="flex items-center justify-center gap-3 pt-2">
                <button id="resultAddBtn" class="px-6 py-2.5 bg-primary text-on-primary rounded-lg font-label-lg text-sm shadow hover:bg-primary-container transition-colors flex items-center gap-1.5">
                  <span class="material-symbols-outlined text-[16px]">shopping_bag</span> Add Specimen to Bag
                </button>
                <a id="resultLink" href="product.html" class="px-6 py-2.5 bg-surface text-primary border border-primary/20 rounded-lg font-label-lg text-sm hover:bg-surface-container transition-colors">
                  Customize Details
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modalWrap);
    modal = document.getElementById('plantQuizModal');
  }

  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-open-quiz], a[href*="quiz"], a[data-path="plant-quiz"]');
    if (trigger) {
      e.preventDefault();
      openQuizModal();
    }
  });

  const closeBtn = document.getElementById('closeQuizBtn');
  if (closeBtn) closeBtn.addEventListener('click', closeQuizModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeQuizModal();
  });
}

const quizAnswers = { light: null, care: null, pet: null };

function openQuizModal() {
  const modal = document.getElementById('plantQuizModal');
  const card = document.getElementById('quizCard');
  if (!modal || !card) return;

  quizAnswers.light = null;
  quizAnswers.care = null;
  quizAnswers.pet = null;
  showQuizStep(1);

  modal.classList.remove('opacity-0', 'pointer-events-none');
  modal.classList.add('opacity-100', 'pointer-events-auto');
  card.classList.remove('scale-95');
  card.classList.add('scale-100');
  document.body.style.overflow = 'hidden';
}

function closeQuizModal() {
  const modal = document.getElementById('plantQuizModal');
  const card = document.getElementById('quizCard');
  if (!modal || !card) return;

  modal.classList.remove('opacity-100', 'pointer-events-auto');
  modal.classList.add('opacity-0', 'pointer-events-none');
  card.classList.remove('scale-100');
  card.classList.add('scale-95');
  document.body.style.overflow = '';
}

function showQuizStep(stepNumber) {
  document.getElementById('quizStep1').classList.add('hidden');
  document.getElementById('quizStep2').classList.add('hidden');
  document.getElementById('quizStep3').classList.add('hidden');
  document.getElementById('quizResult').classList.add('hidden');

  const bar1 = document.querySelector('.step-bar-1');
  const bar2 = document.querySelector('.step-bar-2');
  const bar3 = document.querySelector('.step-bar-3');

  if (stepNumber === 1) {
    document.getElementById('quizStep1').classList.remove('hidden');
    bar1.className = 'flex-1 h-1.5 rounded-full bg-primary transition-all step-bar-1';
    bar2.className = 'flex-1 h-1.5 rounded-full bg-surface-container-highest transition-all step-bar-2';
    bar3.className = 'flex-1 h-1.5 rounded-full bg-surface-container-highest transition-all step-bar-3';
  } else if (stepNumber === 2) {
    document.getElementById('quizStep2').classList.remove('hidden');
    bar2.className = 'flex-1 h-1.5 rounded-full bg-primary transition-all step-bar-2';
  } else if (stepNumber === 3) {
    document.getElementById('quizStep3').classList.remove('hidden');
    bar3.className = 'flex-1 h-1.5 rounded-full bg-primary transition-all step-bar-3';
  } else if (stepNumber === 4) {
    document.getElementById('quizResult').classList.remove('hidden');
  }
}

function selectQuizAnswer(category, value, btn) {
  quizAnswers[category] = value;

  btn.parentElement.querySelectorAll('button').forEach(b => {
    b.classList.remove('border-primary', 'bg-primary/5', 'ring-1', 'ring-primary');
  });
  btn.classList.add('border-primary', 'bg-primary/5', 'ring-1', 'ring-primary');

  setTimeout(() => {
    if (category === 'light') {
      showQuizStep(2);
    } else if (category === 'care') {
      showQuizStep(3);
    } else if (category === 'pet') {
      calculateQuizResult();
    }
  }, 250);
}

function calculateQuizResult() {
  const products = VerdantStore.PRODUCTS;
  let matched = products[0];

  if (quizAnswers.pet === true) {
    matched = products.find(p => p.id === 'calathea-orbifolia') || matched;
  } else if (quizAnswers.light === 'direct') {
    matched = products.find(p => p.id === 'ficus-lyrata') || products.find(p => p.id === 'ficus-audrey') || matched;
  } else if (quizAnswers.care === 'advanced') {
    matched = products.find(p => p.id === 'philodendron-spiritus-sancti') || products.find(p => p.id === 'anthurium-regale') || matched;
  } else {
    matched = products.find(p => p.id === 'monstera-deliciosa') || matched;
  }

  document.getElementById('resultName').textContent = matched.name;
  document.getElementById('resultDesc').textContent = matched.description;
  document.getElementById('resultBinomial').textContent = matched.binomial;
  document.getElementById('resultTag').textContent = matched.tag;
  document.getElementById('resultPrice').textContent = VerdantStore.formatPrice(matched.price);
  document.getElementById('resultImg').src = matched.image;
  document.getElementById('resultLink').href = `product.html?id=${matched.id}`;

  const addBtn = document.getElementById('resultAddBtn');
  addBtn.onclick = () => {
    VerdantStore.addToCart(matched);
    closeQuizModal();
    openCartDrawer();
  };

  showQuizStep(4);
}

// --------------------------------------------------------------------------
// 5. PRIVACY & TERMS MODAL FOR FOOTER
// --------------------------------------------------------------------------
function initPolicyModal() {
  if (document.getElementById('policyModal')) return;

  const modalWrap = document.createElement('div');
  modalWrap.innerHTML = `
    <div id="policyModal" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 bg-inverse-surface/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
      <div class="bg-background w-full max-w-2xl rounded-2xl shadow-2xl overflow-hidden border border-primary/10 flex flex-col max-h-[80vh]">
        <div class="bg-surface-container-low p-6 border-b border-primary/5 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-primary text-[24px]">verified_user</span>
            <h3 id="policyModalTitle" class="font-headline-sm text-primary font-serif">Sanctuary Policies & Protocols</h3>
          </div>
          <button id="closePolicyBtn" class="w-8 h-8 rounded-full bg-surface text-outline hover:text-primary flex items-center justify-center transition-colors">
            <span class="material-symbols-outlined text-[18px]">close</span>
          </button>
        </div>
        <div class="p-6 overflow-y-auto space-y-4 font-body-sm text-on-surface-variant leading-relaxed" id="policyModalContent">
          <h4 class="font-title-md text-primary font-bold">1. Botanical Arrive-Alive Guarantee</h4>
          <p>Every specimen reared at Verdant Haven undergoes 28 days of bio-substrate hardening prior to release. Should your foliage show shock or transit stress within 30 days of courier handoff, our conservatory replaces the specimen without administrative hindrance.</p>
          <h4 class="font-title-md text-primary font-bold">2. Substrate & Soil Transparency</h4>
          <p>We do not extract wild virgin peat moss. All living substrates are formulated with sustainably harvested pine bark, perlite, horticultural charcoal, and organic worm mycorrhizae (Formula A-7 and Formula B-2).</p>
          <h4 class="font-title-md text-primary font-bold">3. Privacy & Horticultural Telemetry</h4>
          <p>Your NFC sensor telemetry and humidity logs are encrypted under 256-bit SSL protocols. We never commodify or transmit your sanctuary address or indoor climate data to third-party ad brokers.</p>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(modalWrap);

  const closeBtn = document.getElementById('closePolicyBtn');
  const modal = document.getElementById('policyModal');
  if (closeBtn) closeBtn.onclick = () => {
    modal.classList.add('opacity-0', 'pointer-events-none');
    modal.classList.remove('opacity-100', 'pointer-events-auto');
  };
  if (modal) modal.onclick = (e) => {
    if (e.target === modal) {
      modal.classList.add('opacity-0', 'pointer-events-none');
      modal.classList.remove('opacity-100', 'pointer-events-auto');
    }
  };
}

function openPolicyModal(title) {
  const modal = document.getElementById('policyModal');
  const titleEl = document.getElementById('policyModalTitle');
  if (!modal) return;
  if (titleEl && title) titleEl.textContent = title;
  modal.classList.remove('opacity-0', 'pointer-events-none');
  modal.classList.add('opacity-100', 'pointer-events-auto');
}

// --------------------------------------------------------------------------
// 6. GLOBAL HEADER & LINK NORMALIZATION
// --------------------------------------------------------------------------
function initGlobalHeaderAndLinks() {
  document.querySelectorAll('a').forEach(link => {
    const href = link.getAttribute('href') || '';
    const path = link.getAttribute('data-path') || '';
    const txt = link.textContent.trim().toLowerCase();

    // Fix dead links
    if (path === 'greenhouse-locations' || txt.includes('our nurseries')) {
      link.href = 'catalog.html';
      link.title = 'Explore Sauvie Island Glasshouse Cultivars';
    } else if (path === 'sustainability' || path === 'sustainability-pledge' || txt.includes('botanical guarantee') || txt.includes('our botanical pledge')) {
      link.href = 'passport.html';
      link.title = 'Sanctuary Botanical Guarantee & Provenance';
    } else if (path === 'shop-plants' || path === 'botanical-catalog' || txt === 'shop plants' || txt === 'botanical catalog' || href === '#curated-catalog') {
      link.href = 'catalog.html';
    } else if (path === 'rare-finds' || txt === 'rare finds' || txt === 'monstera deliciosa') {
      link.href = 'product.html';
    } else if (path === 'planters-and-care' || txt === 'planters & care') {
      link.href = 'catalog.html?category=vessels';
    } else if (path === 'care-lab' || path === 'plant-care-lab-provenance' || txt.includes('care lab') || txt.includes('plant doctor')) {
      link.href = 'care-lab.html';
    } else if (path === 'provenance' || path === 'living-passport-digital-herbarium' || txt.includes('passport') || txt.includes('herbarium')) {
      link.href = 'passport.html';
    } else if (path === 'workshops' || txt === 'workshops') {
      link.href = 'consultation.html';
    } else if (path === 'about' || txt === 'about') {
      link.href = 'passport.html';
    } else if (path === 'reviews-feedback' || path === 'reviews-and-feedback' || path === 'botanical-reviews' || txt.includes('reviews')) {
      link.href = 'reviews.html';
    } else if (path === 'acclimation-journal' || path === '30-day-root-vitality-checkup-booking' || txt.includes('30-day root checkup') || txt.includes('acclimation journal')) {
      link.href = 'vitality-checkup.html';
    } else if (path === 'virtual-consultation' || path === 'live-horticulturist-video-consultation-root-health-audit' || txt.includes('book a plant doctor')) {
      link.href = 'consultation.html';
    } else if (path === 'shipping-and-tracking' || txt.includes('shipping & greenhouse transit') || txt.includes('delivery concierge') || txt.includes('carbon-neutral delivery')) {
      link.href = 'order-confirmation.html';
    } else if (path === 'sustainable-packaging' || txt.includes('zero-plastic packaging')) {
      link.href = 'mailing-label.html';
    } else if (path === 'privacy-policy' || txt.includes('privacy policy')) {
      link.href = '#';
      link.onclick = (e) => { e.preventDefault(); openPolicyModal('Privacy & Telemetry Protocol'); };
    } else if (path === 'terms-of-service' || txt.includes('terms of service')) {
      link.href = '#';
      link.onclick = (e) => { e.preventDefault(); openPolicyModal('Sanctuary Terms & Horticultural Assurance'); };
    } else if (txt.includes('assessing natural light') || txt.includes('the art of root hydration') || txt.includes('substrates & repotting') || txt.includes('organic pest defense')) {
      link.href = 'care-lab.html';
    } else if (txt.includes('pet-friendly houseplants')) {
      link.href = 'catalog.html?filter=pet-safe';
    } else if (path === 'corporate-gifting' || path === 'contact' || txt.includes('customer inquiries') || txt.includes('concierge chat')) {
      link.href = 'consultation.html';
    } else if (path === 'pot-recycling' || txt.includes('vessel reuse initiative')) {
      link.href = 'product.html';
    } else if (href === '#' && (txt === 'home' || txt === 'sanctuary' || txt.includes('verdant haven'))) {
      link.href = 'index.html';
    }
  });

  // User Profile Icon
  document.querySelectorAll('.material-symbols-outlined').forEach(icon => {
    if (icon.textContent.trim() === 'person') {
      const container = icon.closest('div, a, button');
      if (container && !container.getAttribute('data-profile-wired')) {
        container.setAttribute('data-profile-wired', 'true');
        container.style.cursor = 'pointer';
        container.title = 'Sanctuary Member Dashboard (Clara Vance)';
        container.onclick = (e) => {
          e.preventDefault();
          window.location.href = 'dashboard.html';
        };
      }
    }
  });

  // Highlight current nav item
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('text-primary', 'font-semibold', 'border-b-2', 'border-primary');
    }
  });
}

function updateHeaderBadges() {
  const cartCount = VerdantStore.getCartCount();
  document.querySelectorAll('[data-path="cart"] span:last-child, a[aria-label="Shopping Cart"] span:last-child').forEach(badge => {
    if (badge && badge.classList.contains('rounded-full')) {
      badge.textContent = cartCount;
    }
  });

  const wishlistCount = VerdantStore.getWishlist().length;
  document.querySelectorAll('[data-path="wishlist"] span:last-child, a[aria-label="Wishlist"] span:last-child').forEach(badge => {
    if (badge && badge.classList.contains('rounded-full')) {
      badge.textContent = wishlistCount;
    }
  });
}

// --------------------------------------------------------------------------
// 7. CURRENCY SWITCHER
// --------------------------------------------------------------------------
function initCurrencySwitcher() {
  const current = VerdantStore.getCurrency();
  document.querySelectorAll('select[aria-label="Currency Switcher"]').forEach(select => {
    select.value = current;
    select.addEventListener('change', (e) => {
      VerdantStore.setCurrency(e.target.value);
    });
  });
}

// --------------------------------------------------------------------------
// 8. LIVE SEARCH AUTOCOMPLETE
// --------------------------------------------------------------------------
function initSearchAutocomplete() {
  document.querySelectorAll('input[type="search"]').forEach(input => {
    const parent = input.parentElement;
    parent.classList.add('relative');

    const dropdown = document.createElement('div');
    dropdown.className = 'absolute top-full left-0 right-0 mt-2 bg-surface-container-lowest rounded-xl shadow-2xl border border-primary/10 py-2 hidden z-[9990] max-h-80 overflow-y-auto';
    parent.appendChild(dropdown);

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      if (q.length < 2) {
        dropdown.classList.add('hidden');
        return;
      }

      const results = VerdantStore.PRODUCTS.filter(p => 
        p.name.toLowerCase().includes(q) || 
        p.binomial.toLowerCase().includes(q) || 
        p.category.toLowerCase().includes(q)
      );

      if (results.length === 0) {
        dropdown.innerHTML = `<div class="px-4 py-3 text-xs text-on-surface-variant text-center">No specimens found for "${q}".</div>`;
      } else {
        dropdown.innerHTML = results.map(p => `
          <a href="product.html?id=${p.id}" class="flex items-center gap-3 px-4 py-2 hover:bg-surface-container transition-colors">
            <img src="${p.image}" class="w-10 h-10 rounded-md object-cover" />
            <div class="flex-1 min-w-0">
              <h5 class="font-title-md text-sm text-primary truncate">${p.name}</h5>
              <p class="font-body-sm text-[11px] text-on-surface-variant italic truncate">${p.binomial}</p>
            </div>
            <span class="font-label-sm font-bold text-primary">${VerdantStore.formatPrice(p.price)}</span>
          </a>
        `).join('');
      }
      dropdown.classList.remove('hidden');
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const q = input.value.trim();
        window.location.href = `catalog.html?q=${encodeURIComponent(q)}`;
      }
    });

    document.addEventListener('click', (e) => {
      if (!parent.contains(e.target)) {
        dropdown.classList.add('hidden');
      }
    });
  });
}

// --------------------------------------------------------------------------
// 9. RE-INSPECT TABS ON CURRENT PAGE
// --------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  // 1. Generic Tab Switchers
  document.querySelectorAll('[role="tablist"]').forEach(tablist => {
    const tabs = tablist.querySelectorAll('[role="tab"]');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.setAttribute('aria-selected', 'false'));
        tab.setAttribute('aria-selected', 'true');
      });
    });
  });

  // 2. Reviews Tabs
  document.querySelectorAll('.filter-tab, button[data-rating-filter]').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => {
        b.classList.remove('bg-primary', 'text-on-primary');
        b.classList.add('bg-surface-container-low', 'text-on-surface');
      });
      btn.classList.remove('bg-surface-container-low', 'text-on-surface');
      btn.classList.add('bg-primary', 'text-on-primary');
    });
  });

  // 3. Size pills
  document.querySelectorAll('.size-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      pill.parentElement.querySelectorAll('.size-pill').forEach(p => {
        p.classList.remove('bg-primary', 'text-on-primary', 'active');
        p.classList.add('bg-surface-container-low');
      });
      pill.classList.remove('bg-surface-container-low');
      pill.classList.add('bg-primary', 'text-on-primary', 'active');
    });
  });
});

window.openCartDrawer = openCartDrawer;
window.closeCartDrawer = closeCartDrawer;
window.openQuizModal = openQuizModal;
window.closeQuizModal = closeQuizModal;
window.selectQuizAnswer = selectQuizAnswer;
window.openSiteMapDrawer = openSiteMapDrawer;
window.closeSiteMapDrawer = closeSiteMapDrawer;
window.openPolicyModal = openPolicyModal;
