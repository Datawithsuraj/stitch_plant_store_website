import os
import re
from bs4 import BeautifulSoup

def read_source(folder_name):
    path = os.path.join(folder_name, 'code.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def inject_common(html, active_page='', title='Verdant Haven — Artisanal Botanical Boutique'):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Title
    if soup.title:
        soup.title.string = title
    else:
        t = soup.new_tag('title')
        t.string = title
        soup.head.append(t)

    # Injections into head
    has_store = any('js/store.js' in str(s) for s in soup.find_all('script'))
    if not has_store:
        s1 = soup.new_tag('script', src='js/store.js')
        s2 = soup.new_tag('script', src='js/nav.js')
        soup.head.append(s1)
        soup.head.append(s2)

    # Global custom style
    custom_style = soup.new_tag('style')
    custom_style.string = """
      html { scroll-behavior: smooth; }
      .fade-in { animation: fadeIn 0.35s ease-in-out; }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      .btn-hover-lift { transition: transform 0.2s ease, box-shadow 0.2s ease; }
      .btn-hover-lift:hover { transform: translateY(-2px); box-shadow: 0 8px 20px -4px rgba(0,54,41,0.15); }
      .glass-panel { background: rgba(250, 249, 244, 0.85); backdrop-filter: blur(12px); }
    """
    soup.head.append(custom_style)

    # Standardize links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        data_path = a.get('data-path', '')

        # Home
        if data_path == 'sanctuary' or href in ['#sanctuary', 'index.html', '#']:
            if 'Shop Plants' not in a.text and 'Verdant Haven' in a.text:
                a['href'] = 'index.html'

        # Catalog
        if data_path in ['shop-plants', 'botanical-catalog'] or 'Shop Plants' in a.text or 'Botanical Catalog' in a.text or href == '#curated-catalog':
            a['href'] = 'catalog.html'

        # Rare finds / product
        if data_path == 'rare-finds' or 'Rare Finds' in a.text or 'Monstera Deliciosa' in a.text:
            if a.get('href') == '#':
                a['href'] = 'product.html'

        # Care Lab
        if data_path in ['care-lab', 'plant-care-lab-provenance'] or 'Care Lab' in a.text or 'Clinical Triage' in a.text:
            a['href'] = 'care-lab.html'

        # Passport
        if data_path in ['provenance', 'living-passport-digital-herbarium'] or 'Passport' in a.text or 'Herbarium' in a.text:
            a['href'] = 'passport.html'

        # Reviews
        if data_path in ['reviews-feedback', 'reviews-and-feedback', 'botanical-reviews'] or 'Reviews' in a.text:
            a['href'] = 'reviews.html'

        # Checkup
        if data_path in ['acclimation-journal', '30-day-root-vitality-checkup-booking'] or '30-Day Root Checkup' in a.text or 'Acclimation Journal' in a.text:
            a['href'] = 'vitality-checkup.html'

        # Plant Doctor / Video Consult
        if data_path in ['virtual-consultation', 'live-horticulturist-video-consultation-root-health-audit'] or 'Plant Doctor' in a.text or 'Book a Plant Doctor' in a.text:
            a['href'] = 'consultation.html'

        # Plant Quiz
        if data_path == 'plant-quiz' or 'Plant Quiz' in a.text or 'Take 2-Min Plant Quiz' in a.text:
            a['href'] = '#quiz'
            a['data-open-quiz'] = 'true'

        # Cart
        if data_path == 'cart' or href == '#cart' or a.get('aria-label') == 'Shopping Cart':
            a['href'] = '#cart'
            a['onclick'] = 'openCartDrawer(); return false;'

        # Wishlist
        if data_path == 'wishlist' or a.get('aria-label') == 'Wishlist':
            a['href'] = '#wishlist'
            a['onclick'] = "VerdantStore.showToast('Botanical Wishlist', 'You have ' + VerdantStore.getWishlist().length + ' specimens saved in your sanctuary.', 'favorite', 'success'); return false;"

    # Highlight active link in header nav
    for nav_a in soup.find_all('nav'):
        for a in nav_a.find_all('a'):
            href = a.get('href', '')
            if (active_page == 'home' and href == 'index.html') or \
               (active_page == 'catalog' and href == 'catalog.html') or \
               (active_page == 'product' and href == 'product.html') or \
               (active_page == 'care-lab' and href == 'care-lab.html') or \
               (active_page == 'passport' and href == 'passport.html') or \
               (active_page == 'reviews' and href == 'reviews.html') or \
               (active_page == 'consultation' and href == 'consultation.html') or \
               (active_page == 'vitality' and href == 'vitality-checkup.html'):
                a['class'] = (a.get('class', []) if isinstance(a.get('class'), list) else a.get('class', '').split()) + ['text-primary', 'font-semibold', 'border-b-2', 'border-primary']

    return str(soup)

# --------------------------------------------------------------------------
# 4. CHECKOUT.HTML (Full Multi-step checkout with modals and transitions)
# --------------------------------------------------------------------------
def build_checkout():
    print("Building checkout.html...")
    raw_step1 = read_source('botanical_checkout_multi_step_greenhouse_dispatch')
    soup1 = BeautifulSoup(raw_step1, 'html.parser')

    # Read Step 2 forms
    raw_step2 = read_source('botanical_checkout_payment_settlement')
    soup2 = BeautifulSoup(raw_step2, 'html.parser')

    # Read Step 3 review
    raw_step3 = read_source('botanical_checkout_order_review_final_confirmation')
    soup3 = BeautifulSoup(raw_step3, 'html.parser')

    # Read Step 4 success
    raw_step4 = read_source('botanical_checkout_order_processing_settlement_success')
    soup4 = BeautifulSoup(raw_step4, 'html.parser')

    # Read split card modal
    raw_split = read_source('botanical_checkout_add_card_split_payment_modal')
    soup_split = BeautifulSoup(raw_split, 'html.parser')
    split_modal = soup_split.find('div', id='split-card-modal')

    # Extract forms
    step1_form = soup1.find('section', class_=lambda c: c and 'lg:col-span-7' in c)
    step2_form = soup2.find('div', class_=lambda c: c and 'lg:col-span-7' in c)
    step3_form = soup3.find('div', class_=lambda c: c and 'lg:col-span-7' in c)
    step4_full = soup4.find('main')

    # Combine into step containers
    checkout_script = """
      <script>
        let currentCheckoutStep = 1;

        function goToStep(step) {
          currentCheckoutStep = step;

          // Toggle visibility of step sections
          document.getElementById('checkout-step-1')?.classList.toggle('hidden', step !== 1);
          document.getElementById('checkout-step-2')?.classList.toggle('hidden', step !== 2);
          document.getElementById('checkout-step-3')?.classList.toggle('hidden', step !== 3);
          document.getElementById('checkout-step-4')?.classList.toggle('hidden', step !== 4);

          // Update Stepper Navigation Indicators
          const stepper = document.getElementById('checkout-stepper');
          if (stepper) {
            stepper.querySelectorAll('.stepper-pill').forEach((pill, idx) => {
              const pillStep = idx + 1;
              const num = pill.querySelector('.stepper-num');
              if (pillStep === step) {
                pill.className = 'stepper-pill flex items-center gap-space-sm bg-primary/10 p-space-xs px-space-sm rounded-xl font-semibold text-primary';
                if (num) num.className = 'stepper-num w-7 h-7 rounded-full bg-primary text-on-primary flex items-center justify-center font-label-sm shadow-sm';
              } else if (pillStep < step) {
                pill.className = 'stepper-pill flex items-center gap-space-sm p-space-xs px-space-sm rounded-xl text-secondary';
                if (num) {
                  num.className = 'stepper-num w-7 h-7 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center font-label-sm';
                  num.innerHTML = '<span class="material-symbols-outlined text-[16px]">check</span>';
                }
              } else {
                pill.className = 'stepper-pill flex items-center gap-space-sm p-space-xs px-space-sm rounded-xl opacity-60 text-on-surface-variant';
                if (num) {
                  num.className = 'stepper-num w-7 h-7 rounded-full bg-surface-container text-on-surface-variant flex items-center justify-center font-label-sm';
                  num.textContent = pillStep;
                }
              }
            });
          }

          // Scroll to top
          window.scrollTo({ top: 0, behavior: 'smooth' });

          // If step 4 (Success), start animation and generate order
          if (step === 4) {
            initSettlementSuccess();
          }
        }

        function initSettlementSuccess() {
          const cart = VerdantStore.getCart();
          const subtotal = VerdantStore.getCartSubtotal();
          const orderId = 'VH-' + Math.floor(10000 + Math.random() * 90000);
          
          // Save order to history
          const order = {
            orderId: orderId,
            date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
            items: cart,
            subtotal: subtotal,
            shipping: subtotal >= 120 ? 0 : 15,
            total: subtotal + (subtotal >= 120 ? 0 : 15),
            status: 'Reserved in Glasshouse Bay 4G'
          };
          sessionStorage.setItem('verdant_latest_order', JSON.stringify(order));
          VerdantStore.clearCart();

          // Update order id badges
          document.querySelectorAll('.order-id-display').forEach(el => el.textContent = orderId);
        }

        document.addEventListener('DOMContentLoaded', () => {
          // Wire Step 1 -> Step 2
          const step1Btn = document.querySelector('#checkout-step-1 button[type="submit"], #checkout-step-1 button:has-text("Continue to Payment"), #checkout-step-1 a[href*="payment"], #to-step-2');
          if (step1Btn) {
            step1Btn.addEventListener('click', (e) => {
              e.preventDefault();
              goToStep(2);
            });
          }

          // Wire Step 2 -> Step 3
          const step2Btn = document.querySelector('#to-step-3');
          if (step2Btn) {
            step2Btn.addEventListener('click', (e) => {
              e.preventDefault();
              goToStep(3);
            });
          }

          // Wire Step 3 -> Step 4
          const placeOrderBtn = document.querySelector('#place-order-btn');
          if (placeOrderBtn) {
            placeOrderBtn.addEventListener('click', (e) => {
              e.preventDefault();
              goToStep(4);
            });
          }

          // Populate Step 3 Cart Items
          const reviewItemsContainer = document.getElementById('step3-cart-items');
          if (reviewItemsContainer) {
            const cart = VerdantStore.getCart();
            reviewItemsContainer.innerHTML = cart.map(item => `
              <div class="flex items-center gap-space-md py-space-sm border-b border-outline-variant/30">
                <img src="${item.image}" class="w-16 h-20 rounded-lg object-cover" />
                <div class="flex-1 min-w-0">
                  <h4 class="font-title-md text-primary font-serif">${item.name}</h4>
                  <p class="font-body-sm text-[12px] text-on-surface-variant">${item.size || 'Medium'} • ${item.vessel || 'Terracotta Natural'}</p>
                  <span class="text-xs text-secondary font-semibold">Qty: ${item.quantity}</span>
                </div>
                <span class="font-title-md text-primary font-bold">${VerdantStore.formatPrice(item.price * item.quantity)}</span>
              </div>
            `).join('');

            const subtotal = VerdantStore.getCartSubtotal();
            const ship = subtotal >= 120 ? 0 : 15;
            document.getElementById('step3-subtotal').textContent = VerdantStore.formatPrice(subtotal);
            document.getElementById('step3-shipping').textContent = ship === 0 ? 'Complimentary' : VerdantStore.formatPrice(ship);
            document.getElementById('step3-total').textContent = VerdantStore.formatPrice(subtotal + ship);
          }
        });
      </script>
    """

    # Assemble HTML
    html = read_source('botanical_checkout_multi_step_greenhouse_dispatch')
    soup = BeautifulSoup(html, 'html.parser')

    # Update stepper nav
    stepper_div = soup.find('nav', {'aria-label': 'Checkout Progress'})
    if stepper_div:
      stepper_div.clear()
      stepper_div.append(BeautifulSoup("""
        <div id="checkout-stepper" class="flex flex-wrap items-center justify-between gap-space-sm bg-surface-container-low px-space-lg py-space-md rounded-xl">
          <div class="stepper-pill flex items-center gap-space-sm bg-primary/10 p-space-xs px-space-sm rounded-xl font-semibold text-primary cursor-pointer" onclick="goToStep(1)">
            <div class="stepper-num w-7 h-7 rounded-full bg-primary text-on-primary flex items-center justify-center font-label-sm shadow-sm">1</div>
            <div class="flex flex-col">
              <span class="font-label-lg tracking-wide">Sanctuary Shipping</span>
              <span class="font-label-sm text-secondary hidden sm:inline text-xs">Courier Protocol</span>
            </div>
          </div>
          <div class="h-[2px] w-8 sm:w-16 bg-primary-fixed-dim/40 rounded-full"></div>
          <div class="stepper-pill flex items-center gap-space-sm p-space-xs px-space-sm rounded-xl opacity-60 text-on-surface-variant cursor-pointer" onclick="goToStep(2)">
            <div class="stepper-num w-7 h-7 rounded-full bg-surface-container text-on-surface-variant flex items-center justify-center font-label-sm">2</div>
            <div class="flex flex-col">
              <span class="font-label-lg font-medium">Payment Settlement</span>
              <span class="font-label-sm text-outline hidden sm:inline text-xs">Sanctuary Vault</span>
            </div>
          </div>
          <div class="h-[2px] w-8 sm:w-16 bg-surface-container-highest rounded-full"></div>
          <div class="stepper-pill flex items-center gap-space-sm p-space-xs px-space-sm rounded-xl opacity-60 text-on-surface-variant cursor-pointer" onclick="goToStep(3)">
            <div class="stepper-num w-7 h-7 rounded-full bg-surface-container text-on-surface-variant flex items-center justify-center font-label-sm">3</div>
            <div class="flex flex-col">
              <span class="font-label-lg font-medium">Review & Custody</span>
              <span class="font-label-sm text-outline hidden sm:inline text-xs">Final Transfer</span>
            </div>
          </div>
        </div>
      """, 'html.parser'))

    # Wrap main sections
    main_section = soup.find('section', class_=lambda c: c and 'lg:col-span-7' in c)
    if main_section:
      main_section['id'] = 'checkout-step-1'
      
      # Add Continue to Payment button at bottom of Step 1
      cont_btn = BeautifulSoup("""
        <div class="pt-4 flex items-center justify-between">
          <a href="catalog.html" class="flex items-center gap-1 text-sm text-on-surface-variant hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[16px]">arrow_back</span> Return to Catalog
          </a>
          <button id="to-step-2" type="button" onclick="goToStep(2)" class="px-8 py-4 bg-primary hover:bg-primary-container text-on-primary font-label-lg text-label-lg rounded-xl shadow-md hover:shadow-lg transition-all flex items-center gap-2">
            <span>Continue to Payment Settlement</span>
            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
          </button>
        </div>
      """, 'html.parser')
      main_section.append(cont_btn)

      # Create Step 2 Container
      step2_container = soup.new_tag('section', id='checkout-step-2', **{'class': 'lg:col-span-7 flex flex-col gap-space-xl hidden'})
      step2_content = soup2.find('div', class_=lambda c: c and 'lg:col-span-7' in c)
      if step2_content:
        # replace inner content
        step2_container.append(BeautifulSoup(str(step2_content), 'html.parser'))
        step2_nav_btns = BeautifulSoup("""
          <div class="pt-4 flex items-center justify-between">
            <button type="button" onclick="goToStep(1)" class="flex items-center gap-1 text-sm text-on-surface-variant hover:text-primary transition-colors">
              <span class="material-symbols-outlined text-[16px]">arrow_back</span> Back to Shipping
            </button>
            <button id="to-step-3" type="button" onclick="goToStep(3)" class="px-8 py-4 bg-primary hover:bg-primary-container text-on-primary font-label-lg text-label-lg rounded-xl shadow-md hover:shadow-lg transition-all flex items-center gap-2">
              <span>Review Botanical Dispatch Order</span>
              <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
            </button>
          </div>
        """, 'html.parser')
        step2_container.append(step2_nav_btns)
      main_section.parent.append(step2_container)

      # Create Step 3 Container
      step3_container = soup.new_tag('section', id='checkout-step-3', **{'class': 'lg:col-span-7 flex flex-col gap-space-xl hidden'})
      step3_container.append(BeautifulSoup("""
        <div class="bg-surface-container-lowest p-space-lg rounded-xl shadow-sm flex flex-col gap-space-md">
          <div class="flex items-center justify-between border-b border-outline-variant/30 pb-3">
            <h2 class="font-headline-sm text-primary flex items-center gap-2">
              <span class="material-symbols-outlined text-[24px]">verified</span>
              Review Specimen Custody & Dispatch
            </h2>
            <span class="text-xs uppercase tracking-wider font-semibold text-secondary">Ready for Authorization</span>
          </div>

          <!-- Items list -->
          <div id="step3-cart-items" class="flex flex-col gap-3 py-2">
            <!-- Dynamic Cart Items -->
          </div>

          <!-- Address & Method Recap -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 p-4 bg-surface-container-low rounded-xl">
            <div>
              <span class="text-xs uppercase font-bold text-outline">Dispatch Address</span>
              <p class="text-sm font-semibold text-on-surface mt-0.5">Clara Vance</p>
              <p class="text-xs text-on-surface-variant">742 Evergreen Conservatory Row, Portland, OR 97201</p>
              <button onclick="goToStep(1)" class="text-xs text-primary underline mt-1">Edit Address</button>
            </div>
            <div>
              <span class="text-xs uppercase font-bold text-outline">Payment Instrument</span>
              <p class="text-sm font-semibold text-on-surface mt-0.5">Visa ending in •••• 9104</p>
              <p class="text-xs text-on-surface-variant">Sanctuary Vault Encrypted</p>
              <button onclick="goToStep(2)" class="text-xs text-primary underline mt-1">Edit Payment</button>
            </div>
          </div>

          <!-- Pricing Recap -->
          <div class="space-y-2 pt-2 text-sm border-t border-outline-variant/30">
            <div class="flex justify-between">
              <span>Specimens Subtotal</span>
              <span id="step3-subtotal" class="font-semibold text-on-surface">$0.00</span>
            </div>
            <div class="flex justify-between">
              <span>Greenhouse Climate Courier</span>
              <span id="step3-shipping" class="font-semibold text-secondary">Complimentary</span>
            </div>
            <div class="flex justify-between text-base font-bold text-primary font-serif pt-2 border-t border-outline-variant/30">
              <span>Total Settlement</span>
              <span id="step3-total">$0.00</span>
            </div>
          </div>

          <!-- Authorize Button -->
          <div class="pt-4 flex items-center justify-between">
            <button type="button" onclick="goToStep(2)" class="flex items-center gap-1 text-sm text-on-surface-variant hover:text-primary transition-colors">
              <span class="material-symbols-outlined text-[16px]">arrow_back</span> Back to Payment
            </button>
            <button id="place-order-btn" type="button" onclick="goToStep(4)" class="px-8 py-4 bg-primary hover:bg-primary-container text-on-primary font-label-lg text-label-lg rounded-xl shadow-lg hover:shadow-xl transition-all flex items-center gap-2">
              <span class="material-symbols-outlined text-[20px]">lock</span>
              <span>Authorize & Place Botanical Order</span>
            </button>
          </div>
        </div>
      """, 'html.parser'))
      main_section.parent.append(step3_container)

      # Create Step 4 Container (Settlement Success)
      step4_container = soup.new_tag('section', id='checkout-step-4', **{'class': 'lg:col-span-12 flex flex-col gap-space-xl hidden'})
      step4_container.append(BeautifulSoup("""
        <div class="max-w-3xl mx-auto w-full bg-surface-container-lowest p-8 md:p-12 rounded-2xl shadow-xl text-center flex flex-col items-center gap-6 border border-primary/10">
          <div class="w-20 h-20 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center shadow-lg">
            <span class="material-symbols-outlined text-[42px] animate-pulse">eco</span>
          </div>

          <div class="space-y-2">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-xs uppercase tracking-widest font-bold">
              <span class="w-2 h-2 rounded-full bg-secondary animate-ping"></span>
              Living Specimen Custody Secured
            </div>
            <h2 class="font-headline-lg text-primary font-serif">Botanical Order Authorized!</h2>
            <p class="font-body-lg text-on-surface-variant max-w-lg mx-auto">
              Your order <strong class="order-id-display text-primary font-semibold">#VH-84920</strong> has been recorded in the Sauvie Island Glasshouse ledger. Specimen harvest & biometric preparation is underway.
            </p>
          </div>

          <!-- Milestones Card -->
          <div class="w-full bg-surface-container-low p-6 rounded-xl text-left space-y-4">
            <h4 class="font-title-md text-primary font-serif flex items-center gap-2">
              <span class="material-symbols-outlined text-secondary">verified_user</span>
              Provenance & Courier Protocol Active
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
              <div class="p-3 bg-surface-container-lowest rounded-lg">
                <span class="text-outline uppercase font-bold block">Specimen Tag</span>
                <span class="font-semibold text-primary text-sm">#MD-2025-V7</span>
                <span class="text-secondary block mt-0.5">Biometric Root Scan OK</span>
              </div>
              <div class="p-3 bg-surface-container-lowest rounded-lg">
                <span class="text-outline uppercase font-bold block">Climate Courier</span>
                <span class="font-semibold text-primary text-sm">Greenhouse Express</span>
                <span class="text-secondary block mt-0.5">72h Thermal Casing</span>
              </div>
              <div class="p-3 bg-surface-container-lowest rounded-lg">
                <span class="text-outline uppercase font-bold block">Target Delivery</span>
                <span class="font-semibold text-primary text-sm">Thursday, 2:00 PM</span>
                <span class="text-secondary block mt-0.5">Optimal 68°F Window</span>
              </div>
            </div>
          </div>

          <!-- Actions -->
          <div class="flex flex-wrap items-center justify-center gap-4 pt-2">
            <a href="order-confirmation.html" class="px-8 py-3.5 bg-primary text-on-primary rounded-xl font-label-lg text-label-lg shadow-md hover:bg-primary-container transition-all flex items-center gap-2">
              <span>Track Live Specimen Dispatch</span>
              <span class="material-symbols-outlined text-[18px]">local_shipping</span>
            </a>
            <a href="invoice.html" class="px-6 py-3.5 bg-surface text-primary border border-primary/20 rounded-xl font-label-lg text-label-lg hover:bg-surface-container transition-all flex items-center gap-2">
              <span>View Certificate & Invoice</span>
              <span class="material-symbols-outlined text-[18px]">receipt_long</span>
            </a>
            <a href="consultation.html" class="px-6 py-3.5 bg-surface-container text-on-surface rounded-xl font-label-lg text-label-lg hover:bg-surface-container-high transition-all flex items-center gap-2">
              <span>Schedule Unboxing Consult</span>
              <span class="material-symbols-outlined text-[18px]">videocam</span>
            </a>
          </div>
        </div>
      """, 'html.parser'))
      main_section.parent.append(step4_container)

    # Append split modal if found
    if split_modal:
      soup.body.append(BeautifulSoup(str(split_modal), 'html.parser'))

    # Final HTML string
    final_html = inject_common(str(soup), active_page='checkout', title='Greenhouse Dispatch & Settlement — Verdant Haven')
    final_html = final_html.replace('</body>', f'{checkout_script}</body>')

    with open('checkout.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("checkout.html created.")

# --------------------------------------------------------------------------
# 5. ORDER-CONFIRMATION.HTML (Live Specimen Dispatch Tracker)
# --------------------------------------------------------------------------
def build_order_confirmation():
    print("Building order-confirmation.html...")
    raw = read_source('botanical_order_confirmation_specimen_dispatch_tracker')
    html = inject_common(raw, active_page='', title='Specimen Dispatch Tracker & Live Telemetry — Verdant Haven')

    tracker_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire Action Buttons
          document.querySelectorAll('button').forEach(btn => {
            const txt = btn.textContent.trim();
            if (txt.includes('Plant Passport (PDF)') || txt.includes('Passport')) {
              btn.onclick = () => window.location.href = 'passport.html';
            } else if (txt.includes('Print') || txt.includes('Receipt')) {
              btn.onclick = () => window.location.href = 'invoice.html';
            } else if (txt.includes('Calendar') || txt.includes('Sync Weather')) {
              btn.onclick = () => VerdantStore.showToast('Calendar Synced', 'Greenhouse transit window added to your calendar.', 'event_available', 'success');
            }
          });

          // Live Telemetry Simulation
          setInterval(() => {
            const tempEl = document.querySelector('[data-temp-metric]');
            if (tempEl) {
              const base = 21.8;
              const delta = (Math.random() * 0.4 - 0.2).toFixed(1);
              tempEl.textContent = (base + parseFloat(delta)).toFixed(1) + '°C';
            }
          }, 3500);
        });
      </script>
    """
    html = html.replace('</body>', f'{tracker_script}</body>')

    with open('order-confirmation.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("order-confirmation.html created.")

# --------------------------------------------------------------------------
# 6. INVOICE.HTML & INVOICE-PRINT.HTML
# --------------------------------------------------------------------------
def build_invoice():
    print("Building invoice.html & invoice-print.html...")
    raw = read_source('botanical_invoice_certificate_of_provenance')
    html = inject_common(raw, active_page='', title='Botanical Invoice & Certificate of Provenance — Verdant Haven')

    invoice_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire print button
          document.querySelectorAll('button').forEach(btn => {
            if (btn.textContent.includes('Print') || btn.textContent.includes('Export')) {
              btn.onclick = () => window.print();
            }
            if (btn.textContent.includes('Envelope') || btn.textContent.includes('Mailing Label')) {
              btn.onclick = () => window.location.href = 'mailing-label.html';
            }
          });
        });
      </script>
    """
    html = html.replace('</body>', f'{invoice_script}</body>')

    with open('invoice.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("invoice.html created.")

    # Dedicated print preview
    raw_print = read_source('botanical_certificate_invoice_dedicated_print_preview_mode')
    html_print = inject_common(raw_print, active_page='', title='Print Certificate of Provenance — Verdant Haven')
    with open('invoice-print.html', 'w', encoding='utf-8') as f:
        f.write(html_print)
    print("invoice-print.html created.")

# --------------------------------------------------------------------------
# 7. MAILING-LABEL.HTML
# --------------------------------------------------------------------------
def build_mailing_label():
    print("Building mailing-label.html...")
    raw = read_source('archival_envelope_mailing_label_template')
    html = inject_common(raw, active_page='', title='Archival Greenhouse Mailing Label — Verdant Haven')
    with open('mailing-label.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("mailing-label.html created.")

# --------------------------------------------------------------------------
# 8. CARE-LAB.HTML (Foliar Diagnostic Tool & Plant Doctor)
# --------------------------------------------------------------------------
def build_care_lab():
    print("Building care-lab.html...")
    raw = read_source('conservatory_care_lab_foliar_diagnostic_tool')
    html = inject_common(raw, active_page='care-lab', title='Conservatory Care Lab & Foliar Diagnostic Triage — Verdant Haven')

    care_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Interactive Foliar AI Analysis Simulation
          const triageBtn = document.querySelector('button:has-text("Emergency Triage"), button.bg-primary:has-text("Triage")') || document.querySelectorAll('button.bg-primary')[0];
          
          if (triageBtn) {
            triageBtn.addEventListener('click', runFoliarScan);
          }

          function runFoliarScan() {
            VerdantStore.showToast('Foliar AI Biometric Engine', 'Scanning chlorophyll density and stomatal conductance...', 'biotech', 'info');

            setTimeout(() => {
              VerdantStore.showToast('Analysis Complete', 'Diagnosis: Mild Root Hypoxia. Diluted organic mycorrhizae feed prescribed.', 'task_alt', 'success');
            }, 1800);
          }

          // Wire Consultation buttons
          document.querySelectorAll('a, button').forEach(el => {
            if (el.textContent.includes('Doctor') || el.textContent.includes('Elena') || el.textContent.includes('Arborist')) {
              if (el.tagName === 'A') el.href = 'consultation.html';
            }
          });
        });
      </script>
    """
    html = html.replace('</body>', f'{care_script}</body>')

    with open('care-lab.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("care-lab.html created.")

# --------------------------------------------------------------------------
# 9. PASSPORT.HTML (Living Plant Passport & Digital Herbarium)
# --------------------------------------------------------------------------
def build_passport():
    print("Building passport.html...")
    raw = read_source('living_plant_passport_digital_herbarium')
    html = inject_common(raw, active_page='passport', title='Living Plant Passport & Digital Herbarium — Verdant Haven')

    passport_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire search or export buttons
          document.querySelectorAll('button').forEach(btn => {
            if (btn.textContent.includes('Export Herbarium Dossier')) {
              btn.onclick = () => {
                window.print();
              };
            } else if (btn.textContent.includes('Order Tailored Nutrient')) {
              btn.onclick = () => {
                VerdantStore.addToCart({
                  id: 'formula-a7',
                  name: 'Formula A-7 Organic Mycorrhizae Feed',
                  binomial: 'Bio-Substrate Elixir 500ml',
                  price: 28,
                  quantity: 1,
                  size: '500ml Bottle',
                  vessel: 'Amber Glass Vessel',
                  image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBFozqNo4T_xhfNVgAnqgnpcHzTwow7HxLwxOe0iJPti0ROf9HCuKvGGsqRJlwN-ki8FKaLYJYG5MoKfL0HEyLjRR8oaKcBHOH_ZwPZdR1CaIah049rfbj_g_Ov4cNqC34FkC8b1pNbj_ceYWG45QRsoMV3JJlmgu3bmQ2EPVj2P2W6jeU0Q3PTRxQ-iOuADPuoAcsQ1HBSjLMuEYB97ztA4xCZGTfFW6A0aC3eBv0sfwWFpDxojIHTCw'
                });
                openCartDrawer();
              };
            }
          });
        });
      </script>
    """
    html = html.replace('</body>', f'{passport_script}</body>')

    with open('passport.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("passport.html created.")

# --------------------------------------------------------------------------
# 10. CONSULTATION.HTML (Schedule 1:1 Video Consultation)
# --------------------------------------------------------------------------
def build_consultation():
    print("Building consultation.html...")
    raw = read_source('horticulturist_video_consultation_specimen_unboxing_scheduling')
    html = inject_common(raw, active_page='consultation', title='Schedule 1:1 Video Consultation — Verdant Haven')

    consult_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Calendar & Slot selection logic
          let selectedDate = 'Thursday, May 22';
          let selectedTime = '10:30 AM PST';

          document.querySelectorAll('.time-slot-btn, button[class*="slot"]').forEach(btn => {
            btn.addEventListener('click', (e) => {
              document.querySelectorAll('.time-slot-btn, button[class*="slot"]').forEach(b => {
                b.classList.remove('bg-primary', 'text-on-primary');
              });
              btn.classList.add('bg-primary', 'text-on-primary');
              selectedTime = btn.textContent.trim();
            });
          });

          // Confirm button
          const confirmBtn = Array.from(document.querySelectorAll('button')).find(b => 
            b.textContent.includes('Confirm') || b.textContent.includes('Schedule') || b.textContent.includes('Reserve')
          );

          if (confirmBtn) {
            confirmBtn.addEventListener('click', (e) => {
              e.preventDefault();
              VerdantStore.showToast('Consultation Reserved', `Appointment confirmed for ${selectedDate} at ${selectedTime}.`, 'video_camera_front', 'success');
              setTimeout(() => {
                window.location.href = 'video-call.html';
              }, 1200);
            });
          }
        });
      </script>
    """
    html = html.replace('</body>', f'{consult_script}</body>')

    with open('consultation.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("consultation.html created.")

# --------------------------------------------------------------------------
# 11. VIDEO-CALL.HTML (Live Horticulturist Video Call)
# --------------------------------------------------------------------------
def build_video_call():
    print("Building video-call.html...")
    raw = read_source('live_horticulturist_video_consultation_root_health_audit')
    html = inject_common(raw, active_page='consultation', title='Live Root Health Audit & Tele-Horticulture — Verdant Haven')

    video_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Live Timer Countdown
          let seconds = 504; // 8:24
          const timerEl = document.getElementById('session-timer');
          if (timerEl) {
            setInterval(() => {
              if (seconds > 0) {
                seconds--;
                const m = Math.floor(seconds / 60);
                const s = seconds % 60;
                timerEl.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
              }
            }, 1000);
          }

          // Mic and Camera Toggles
          document.querySelectorAll('.material-symbols-outlined').forEach(icon => {
            if (icon.textContent === 'mic') {
              const btn = icon.closest('button');
              if (btn) {
                btn.onclick = () => {
                  const isMuted = icon.textContent === 'mic_off';
                  icon.textContent = isMuted ? 'mic' : 'mic_off';
                  btn.classList.toggle('bg-error', !isMuted);
                  btn.classList.toggle('text-white', !isMuted);
                  VerdantStore.showToast(isMuted ? 'Microphone On' : 'Microphone Muted', '', isMuted ? 'mic' : 'mic_off');
                };
              }
            } else if (icon.textContent === 'videocam') {
              const btn = icon.closest('button');
              if (btn) {
                btn.onclick = () => {
                  const isOff = icon.textContent === 'videocam_off';
                  icon.textContent = isOff ? 'videocam' : 'videocam_off';
                  btn.classList.toggle('bg-error', !isOff);
                  btn.classList.toggle('text-white', !isOff);
                  VerdantStore.showToast(isOff ? 'Camera On' : 'Camera Off', '', isOff ? 'videocam' : 'videocam_off');
                };
              }
            } else if (icon.textContent === 'photo_camera') {
              const btn = icon.closest('button');
              if (btn) {
                btn.onclick = () => {
                  VerdantStore.showToast('Leaf Snapshot Captured', 'Saved 4K high-res specimen frame to clinical dossier.', 'camera');
                };
              }
            }
          });

          // End call button
          const endBtn = Array.from(document.querySelectorAll('button')).find(b => 
            b.textContent.includes('End Session') || b.textContent.includes('Leave') || b.textContent.includes('End Call')
          );
          if (endBtn) {
            endBtn.onclick = () => {
              if (confirm('Conclude the tele-horticulture audit with Dr. Elena?')) {
                window.location.href = 'dashboard.html';
              }
            };
          }
        });
      </script>
    """
    html = html.replace('</body>', f'{video_script}</body>')

    with open('video-call.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("video-call.html created.")

# --------------------------------------------------------------------------
# 12. VITALITY-CHECKUP.HTML & VITALITY-CONFIRMED.HTML
# --------------------------------------------------------------------------
def build_vitality():
    print("Building vitality-checkup.html & vitality-confirmed.html...")
    raw = read_source('30_day_root_vitality_checkup_booking_acclimation_log')
    html = inject_common(raw, active_page='vitality', title='30-Day Root Vitality Checkup & Acclimation Log — Verdant Haven')

    vitality_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const form = document.querySelector('form');
          const submitBtn = Array.from(document.querySelectorAll('button')).find(b => 
            b.textContent.includes('Book') || b.textContent.includes('Submit') || b.textContent.includes('Acclimation')
          );

          if (submitBtn) {
            submitBtn.addEventListener('click', (e) => {
              e.preventDefault();
              VerdantStore.showToast('Acclimation Log Saved', '30-Day Checkup scheduled with conservatory arborists.', 'task_alt', 'success');
              setTimeout(() => {
                window.location.href = 'vitality-confirmed.html';
              }, 1000);
            });
          }
        });
      </script>
    """
    html = html.replace('</body>', f'{vitality_script}</body>')

    with open('vitality-checkup.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("vitality-checkup.html created.")

    # Confirmation page
    raw_conf = read_source('30_day_root_vitality_checkup_appointment_confirmation')
    html_conf = inject_common(raw_conf, active_page='vitality', title='Root Vitality Checkup Confirmed — Verdant Haven')
    with open('vitality-confirmed.html', 'w', encoding='utf-8') as f:
        f.write(html_conf)
    print("vitality-confirmed.html created.")

# --------------------------------------------------------------------------
# 13. REVIEWS.HTML (Client Feedback & Botanical Reviews)
# --------------------------------------------------------------------------
def build_reviews():
    print("Building reviews.html...")
    raw = read_source('client_feedback_botanical_specimen_reviews')
    html = inject_common(raw, active_page='reviews', title='Client Feedback & Specimen Reviews — Verdant Haven')

    reviews_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Thumbs up helpful buttons
          document.querySelectorAll('.material-symbols-outlined').forEach(icon => {
            if (icon.textContent === 'thumb_up') {
              const btn = icon.closest('button');
              if (btn) {
                btn.onclick = () => {
                  const countEl = btn.querySelector('span:last-child');
                  if (countEl) {
                    let num = parseInt(countEl.textContent) || 0;
                    countEl.textContent = num + 1;
                    btn.classList.add('text-primary', 'font-bold');
                    VerdantStore.showToast('Helpful Feedback', 'Thank you for rating this review.', 'thumb_up', 'success');
                  }
                };
              }
            }
          });

          // Write a review modal trigger
          const writeReviewBtn = Array.from(document.querySelectorAll('button')).find(b => 
            b.textContent.includes('Write a Review') || b.textContent.includes('Share Feedback')
          );
          if (writeReviewBtn) {
            writeReviewBtn.onclick = () => {
              const reviewText = prompt('Share your botanical experience with your specimen:');
              if (reviewText) {
                VerdantStore.showToast('Review Submitted', 'Your review has been verified and added to the conservatory ledger.', 'rate_review', 'success');
              }
            };
          }
        });
      </script>
    """
    html = html.replace('</body>', f'{reviews_script}</body>')

    with open('reviews.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("reviews.html created.")

# --------------------------------------------------------------------------
# 14. LOGIN.HTML, ACCOUNT-LINK.HTML, DASHBOARD.HTML
# --------------------------------------------------------------------------
def build_auth_and_dashboard():
    print("Building login.html, account-link.html & dashboard.html...")
    
    # Login
    raw_login = read_source('sanctuary_portal_sign_in_account_creation')
    html_login = inject_common(raw_login, active_page='portal', title='Sanctuary Portal — Sign In & Account Minting — Verdant Haven')
    
    login_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire login buttons to proceed to dashboard
          document.querySelectorAll('button[type="submit"], form button').forEach(btn => {
            btn.onclick = (e) => {
              e.preventDefault();
              VerdantStore.showToast('Welcome to Sanctuary', 'Signed in as Clara Vance.', 'login', 'success');
              setTimeout(() => {
                window.location.href = 'dashboard.html';
              }, 800);
            };
          });

          // Quick One-Click Demo Login button injection
          const card = document.querySelector('.bg-surface-container-lowest, form');
          if (card) {
            const demoBtn = document.createElement('button');
            demoBtn.type = 'button';
            demoBtn.className = 'w-full py-2.5 px-4 mb-4 rounded-lg bg-secondary/10 hover:bg-secondary/20 text-secondary text-xs font-semibold uppercase tracking-wider transition-colors flex items-center justify-center gap-1.5';
            demoBtn.innerHTML = '<span class="material-symbols-outlined text-[16px]">bolt</span> Quick Demo 1-Click Access (Clara Vance)';
            demoBtn.onclick = () => {
              window.location.href = 'dashboard.html';
            };
            card.prepend(demoBtn);
          }
        });
      </script>
    """
    html_login = html_login.replace('</body>', f'{login_script}</body>')
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(html_login)
    print("login.html created.")

    # Account Link
    raw_link = read_source('sanctuary_portal_create_account_specimen_linking')
    html_link = inject_common(raw_link, active_page='portal', title='Specimen Passport Linking — Verdant Haven')
    with open('account-link.html', 'w', encoding='utf-8') as f:
        f.write(html_link)
    print("account-link.html created.")

    # Dashboard
    raw_dash = read_source('sanctuary_portal_account_created_welcome_state')
    html_dash = inject_common(raw_dash, active_page='portal', title='Sanctuary Portal Dashboard — Clara Vance — Verdant Haven')
    
    dash_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire dashboard buttons
          document.querySelectorAll('a, button').forEach(el => {
            const txt = el.textContent.trim();
            if (txt.includes('Book Consultation') || txt.includes('Video')) {
              el.onclick = () => window.location.href = 'consultation.html';
            } else if (txt.includes('Root Vitality') || txt.includes('Checkup')) {
              el.onclick = () => window.location.href = 'vitality-checkup.html';
            } else if (txt.includes('Foliar Diagnostic') || txt.includes('Care Lab')) {
              el.onclick = () => window.location.href = 'care-lab.html';
            } else if (txt.includes('Plant Passport') || txt.includes('Herbarium')) {
              el.onclick = () => window.location.href = 'passport.html';
            } else if (txt.includes('Invoice') || txt.includes('Certificate')) {
              el.onclick = () => window.location.href = 'invoice.html';
            }
          });
        });
      </script>
    """
    html_dash = html_dash.replace('</body>', f'{dash_script}</body>')
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_dash)
    print("dashboard.html created.")

def run():
    build_checkout()
    build_order_confirmation()
    build_invoice()
    build_mailing_label()
    build_care_lab()
    build_passport()
    build_consultation()
    build_video_call()
    build_vitality()
    build_reviews()
    build_auth_and_dashboard()
    print("All 18 website pages built successfully!")

if __name__ == '__main__':
    run()
