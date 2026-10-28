# Verdant Haven — Artisanal Botanical Boutique & Sanctuary Portal

A high-end, luxury botanical e-commerce atelier and living plant care sanctuary. Designed with editorial typography, earthy warmth, and clinical horticultural precision.

---

## 🌿 Quick Start

You can run the full functional website locally with either Node.js or Python:

```bash
# Using Node / npx serve (Port 3000)
npm run dev

# Or using Python's built-in server (Port 3000)
npm run serve:py
```

Then open `http://localhost:3000` in your web browser.  
You can also open `index.html` directly in any modern browser (`file:///...`).

---

## 🏛️ Website Architecture & Complete Page Directory

| Page | URL / File | Purpose & Interactive Features |
|---|---|---|
| **Storefront** | `index.html` | Editorial homepage, hero showcase, value props, habitat categories, curated bestsellers, interactive plant quiz teaser, care lab teaser, reviews preview, and newsletter. |
| **Botanical Catalog** | `catalog.html` | Living cultivar archive with live real-time search, category filtering, light tier & pet safety checkboxes, price sorting, wishlist toggling, and fast add-to-bag. |
| **Product Detail & Customizer** | `product.html` | Monstera Deliciosa interactive pot customizer: plant size selection (Small $78, Medium $94, Large $135), hand-thrown vessel material & color swatches, drainage tray toggle, live price recalculation, gallery switcher, and seasonal care calendar. |
| **Greenhouse Checkout** | `checkout.html` | Complete 4-step dispatch workflow: Step 1 (Sanctuary Shipping), Step 2 (Payment Settlement with Card Vault, Add Card Modal & Split Payment Modal), Step 3 (Order Review with live cart items & promo code), Step 4 (Processing animation & order confirmation). |
| **Dispatch Tracker** | `order-confirmation.html` | Real-time live specimen transit tracking, courier milestone progress, microclimate temperature & humidity sensor readouts. |
| **Certificate of Provenance & Invoice** | `invoice.html` | Official archival invoice with cryptographic seal, NFC accession hash, lead arborist signature attestation, and 1-click print mode. |
| **Dedicated Print Preview** | `invoice-print.html` | High-resolution, print-optimized document preview for archival physical printing. |
| **Archival Mailing Label** | `mailing-label.html` | Greenhouse botanical packaging label with customs flora declaration and courier barcodes. |
| **Care Lab & Plant Doctor** | `care-lab.html` | Foliar clinical triage tool: select leaf symptoms, input ambient humidity and lighting, trigger the AI biometric scanning radar, and receive an instant prescription. |
| **Living Plant Passport** | `passport.html` | Digital Herbarium and cryptographic plant passport lookup (e.g. `#MD-2025-V7`), canopy & root inspection tabs, and PDF dossier export. |
| **Tele-Horticulturist Scheduling** | `consultation.html` | 1-on-1 virtual consult booking with Master Botanists (Dr. Elena Alvarez / Marcus Thorne), interactive date picker and time slot selector. |
| **Live Consultation Room** | `video-call.html` | Split-screen video consultation interface: mic/camera toggles, high-definition specimen snapshot capture, live clinical notes pad, and real-time chat with Dr. Elena. |
| **30-Day Root Vitality Checkup** | `vitality-checkup.html` | Acclimation growth log submission form (new leaves, soil moisture, ambient humidity) to extend warranty from 30 to 90 days. |
| **Checkup Confirmation** | `vitality-confirmed.html` | Appointment confirmation with calendar invite generator (.ics) and preparation checklist. |
| **Specimen Reviews Hub** | `reviews.html` | Verified purchaser community reviews, filter by rating & specimen, helpful voting thumbs-up counters, and "Write a Review" interactive modal. |
| **Sanctuary Portal Login** | `login.html` | Secure member authentication with tab toggle (Sign In vs Mint Account) and a 1-Click Demo Login button for testing. |
| **Specimen Linking** | `account-link.html` | Link newly acquired specimen accession IDs and NFC medallions to your user sanctuary account. |
| **Sanctuary Dashboard** | `dashboard.html` | User sanctuary management hub: linked specimen passports, live microclimate telemetry, care reminders, past orders, and upcoming consultations. |

---

## ⚡ Global Interactive Systems

### 1. Slide-out Cart Drawer (`js/nav.js` & `js/store.js`)
- Accessible from every page via the cart icon in the header or any "Add to Bag" button.
- Live `localStorage` synchronization.
- Quantity increment / decrement and removal.
- Dynamic Greenhouse Thermal Express Shipping progress meter towards the $120 threshold.
- Winter Thermal Heat-Pack Add-on toggle (+$4.50).
- Promo code engine: enter `VERDANT10` for a 10% botanical discount!
- Direct transition to `checkout.html`.

### 2. 2-Minute Botanical Quiz Modal
- Triggered globally from header navigation, hero CTAs, or any `data-open-quiz` element.
- 3-step assessment (Light availability, Experience level, Pet safety requirement).
- Instant recommendation matching to the ideal cultivar with 1-click Add to Bag.

### 3. Currency Converter
- Live currency switcher (USD `$`, EUR `€`, GBP `£`) in the header that converts all prices dynamically.

### 4. Live Search Autocomplete
- Header search bar with real-time specimen suggestions and direct link routing.

### 5. Botanical Toast Notification System
- Non-blocking, beautiful toast popups for wishlist updates, cart additions, promo codes, and triage results.
