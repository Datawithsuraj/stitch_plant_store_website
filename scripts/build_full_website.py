import os
import re
from bs4 import BeautifulSoup

def read_source(folder_name):
    path = os.path.join(folder_name, 'code.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def inject_common(html, active_page='home', title='Verdant Haven — Artisanal Botanical Boutique'):
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

    # Style
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
        if data_path == 'rare-finds' or 'Rare Finds' in a.text:
            a['href'] = 'product.html'

        # Care Lab
        if data_path in ['care-lab', 'plant-care-lab-provenance'] or 'Care Lab' in a.text:
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

def build_index():
    print("Building index.html...")
    raw = read_source('botanical_boutique_plant_storefront')
    html = inject_common(raw, active_page='home', title='Verdant Haven — Artisanal Botanical Boutique & Sanctuary')
    
    # Custom interactive additions for index.html
    # Replace CTA links
    html = html.replace('href="#curated-catalog"', 'href="catalog.html"')
    html = html.replace('href="#plant-quiz-section"', 'href="#quiz" onclick="openQuizModal(); return false;"')
    
    # Replace Add to cart buttons to actually invoke VerdantStore
    add_to_cart_hook = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          // Wire product item clicks
          document.querySelectorAll('.product-item').forEach((item, index) => {
            const heading = item.querySelector('h3, h4');
            const name = heading ? heading.textContent.trim() : 'Botanical Specimen';
            const priceEl = item.querySelector('.font-title-lg, .font-title-md, [class*="price"]');
            const price = priceEl ? parseFloat(priceEl.textContent.replace(/[^0-9.]/g, '')) || 94 : 94;
            const img = item.querySelector('img');
            const imgSrc = img ? img.src : '';

            // Add To Bag button inside card
            const addBtn = item.querySelector('.add-to-cart-btn, button:last-of-type');
            if (addBtn && !addBtn.getAttribute('data-wired')) {
              addBtn.setAttribute('data-wired', 'true');
              addBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                VerdantStore.addToCart({
                  id: 'item-' + index,
                  name: name,
                  binomial: 'Conservatory Hardened Cultivar',
                  price: price,
                  quantity: 1,
                  size: 'Medium (8" Pot)',
                  vessel: 'Terracotta Natural',
                  image: imgSrc
                });
                openCartDrawer();
              });
            }

            // Wishlist heart button
            const heartBtn = item.querySelector('button[aria-label="Add to Wishlist"]');
            if (heartBtn && !heartBtn.getAttribute('data-wired')) {
              heartBtn.setAttribute('data-wired', 'true');
              heartBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const icon = heartBtn.querySelector('.material-symbols-outlined');
                const isSaved = VerdantStore.toggleWishlist('item-' + index);
                if (icon) {
                  icon.textContent = isSaved ? 'favorite' : 'favorite_border';
                  icon.classList.toggle('text-secondary', isSaved);
                }
              });
            }
          });
        });
      </script>
    """
    html = html.replace('</body>', f'{add_to_cart_hook}</body>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html created.")

def build_catalog():
    print("Building catalog.html...")
    raw = read_source('curated_botanical_catalog_specimen_archive')
    html = inject_common(raw, active_page='catalog', title='Curated Botanical Catalog & Cultivar Archive — Verdant Haven')

    # Add dynamic filtering script
    catalog_script = """
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const searchInput = document.querySelector('input[placeholder*="Search by botanical"]');
          const sortSelect = document.querySelector('select');
          const cards = Array.from(document.querySelectorAll('.lg\\:col-span-9 .grid > div'));

          // Check URL query parameters for ?q= or ?category=
          const urlParams = new URLSearchParams(window.location.search);
          const qParam = urlParams.get('q');
          if (qParam && searchInput) {
            searchInput.value = qParam;
            filterCards();
          }

          if (searchInput) {
            searchInput.addEventListener('input', filterCards);
          }

          function filterCards() {
            const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
            let visibleCount = 0;

            cards.forEach(card => {
              const text = card.textContent.toLowerCase();
              const matchesQuery = !query || text.includes(query);

              if (matchesQuery) {
                card.style.display = 'flex';
                visibleCount++;
              } else {
                card.style.display = 'none';
              }
            });
          }

          // Wire Card Buttons
          cards.forEach((card, index) => {
            const heading = card.querySelector('h3');
            const name = heading ? heading.textContent.trim() : 'Rare Cultivar';
            const priceEl = card.querySelector('.font-serif.font-bold, .font-display-lg');
            const price = priceEl ? parseFloat(priceEl.textContent.replace(/[^0-9.]/g, '')) || 94 : 94;
            const img = card.querySelector('img');
            const imgSrc = img ? img.src : '';

            // Card links to product detail
            const inspectBtn = card.querySelector('button:last-of-type');
            if (inspectBtn) {
              inspectBtn.addEventListener('click', (e) => {
                e.preventDefault();
                // If Philodendron Spiritus Sancti
                if (name.includes('Spiritus')) {
                  window.location.href = 'product.html?id=philodendron-spiritus-sancti';
                } else if (name.includes('Ficus Lyrata')) {
                  window.location.href = 'product.html?id=ficus-lyrata';
                } else if (name.includes('Calathea')) {
                  window.location.href = 'product.html?id=calathea-orbifolia';
                } else if (name.includes('Anthurium')) {
                  window.location.href = 'product.html?id=anthurium-regale';
                } else {
                  window.location.href = 'product.html?id=monstera-deliciosa';
                }
              });
            }

            // Bookmark button
            const bookmarkBtn = card.querySelector('button[aria-label="Bookmark cultivar"]');
            if (bookmarkBtn) {
              bookmarkBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const icon = bookmarkBtn.querySelector('.material-symbols-outlined');
                const isSaved = VerdantStore.toggleWishlist('catalog-item-' + index);
                if (icon) {
                  icon.textContent = isSaved ? 'bookmark' : 'bookmark_border';
                  icon.classList.toggle('text-secondary', isSaved);
                }
              });
            }
          });

          // Sort Handler
          if (sortSelect) {
            sortSelect.addEventListener('change', (e) => {
              const val = e.target.value;
              const grid = document.querySelector('.lg\\:col-span-9 .grid');
              if (!grid) return;

              const sorted = [...cards].sort((a, b) => {
                const priceA = parseFloat(a.querySelector('.font-serif.font-bold, .font-display-lg')?.textContent.replace(/[^0-9.]/g, '') || 0);
                const priceB = parseFloat(b.querySelector('.font-serif.font-bold, .font-display-lg')?.textContent.replace(/[^0-9.]/g, '') || 0);

                if (val.includes('Lowest First') || val.includes('Low to High')) {
                  return priceA - priceB;
                } else if (val.includes('High to Low') || val.includes('Rarity')) {
                  return priceB - priceA;
                }
                return 0;
              });

              sorted.forEach(card => grid.appendChild(card));
              VerdantStore.showToast('Catalog Re-indexed', `Sorted by ${val}`, 'sort', 'info');
            });
          }
        });
      </script>
    """
    html = html.replace('</body>', f'{catalog_script}</body>')

    with open('catalog.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("catalog.html created.")

def build_product():
    print("Building product.html...")
    raw = read_source('monstera_deliciosa_plant_detail_pot_customizer')
    html = inject_common(raw, active_page='product', title='Monstera Deliciosa — Plant Detail & Pot Customizer — Verdant Haven')

    # Enhanced interactive customizer hook
    customizer_hook = """
      <script>
        // Enhanced Product Store Integration
        document.addEventListener('DOMContentLoaded', () => {
          // Wire Add to Sanctuary Bag button
          const addBtn = document.querySelector('button.w-full.bg-primary, button:has-text("Add to Sanctuary Bag")');
          const allButtons = Array.from(document.querySelectorAll('button'));
          const targetAddBtn = allButtons.find(b => b.textContent.includes('Add to Sanctuary Bag') || b.textContent.includes('Sanctuary Bag'));

          if (targetAddBtn) {
            targetAddBtn.addEventListener('click', (e) => {
              e.preventDefault();
              const priceText = document.getElementById('priceDisplay')?.textContent || '$94.00';
              const price = parseFloat(priceText.replace(/[^0-9.]/g, '')) || 94.00;
              const sizeLabel = document.getElementById('selectedSizeLabel')?.textContent || 'Medium (8" Nursery Pot)';
              const vesselSummary = document.getElementById('vesselSummary')?.textContent || 'Raw Tuscan Terracotta / Terracotta Natural';
              const qty = parseInt(document.getElementById('qtyVal')?.textContent || '1');
              const saucerChecked = document.querySelector('input[type="checkbox"]:not(#marketing-consent)')?.checked !== false;

              VerdantStore.addToCart({
                id: 'monstera-deliciosa',
                name: 'Monstera Deliciosa Liebm.',
                binomial: 'Monstera Deliciosa Liebm. • "Swiss Cheese Plant"',
                size: sizeLabel,
                vessel: vesselSummary,
                drainageTray: saucerChecked,
                price: price,
                quantity: qty,
                image: document.getElementById('mainPlantImage')?.src || 'https://lh3.googleusercontent.com/aida-public/AB6AXuA0l5W9m-5LQW_lVoLP2pMUScwTriaQ1KYlQkpAY-_7hcs8FSy4c3x-q5IUHw9R3pY18wBYqbMn9xaFsQidYuNvtkINRm06Ba04J3sKmcgiGOzBhzvdw1JbgqPTl1KAFR-TaqoUmSg5WLzLkP3Dk2soWm1FiZw9_UHqKicA1fS8I9Oggf2_qH9LUFY4pQt0t-dB7U_NWFA07nfxte2EkR81ru3jp54vHOuJxsUgmhuS74dY9CoLltlVkw'
              });

              openCartDrawer();
            });
          }

          // Wire Consultation buttons
          document.querySelectorAll('a, button').forEach(el => {
            if (el.textContent.includes('Schedule Video Consultation') || el.textContent.includes('Book a Plant Doctor')) {
              el.onclick = () => { window.location.href = 'consultation.html'; };
            }
            if (el.textContent.includes('Certificate of Provenance') || el.textContent.includes('View Living Passport')) {
              el.onclick = () => { window.location.href = 'passport.html'; };
            }
          });
        });
      </script>
    """
    html = html.replace('</body>', f'{customizer_hook}</body>')

    with open('product.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("product.html created.")

build_index()
build_catalog()
build_product()
