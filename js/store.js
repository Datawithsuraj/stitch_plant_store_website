// ==========================================================================
// Verdant Haven — Botanical Store & State Engine
// ==========================================================================

const VerdantStore = (function() {
  const STORAGE_KEYS = {
    CART: 'verdant_haven_cart',
    WISHLIST: 'verdant_haven_wishlist',
    CURRENCY: 'verdant_haven_currency',
    USER: 'verdant_haven_user',
    CURRENT_ORDER: 'verdant_haven_current_order',
    ORDERS: 'verdant_haven_orders_history',
    CHECKUP_APPT: 'verdant_haven_checkup_appt',
    CONSULT_APPT: 'verdant_haven_consult_appt',
    REVIEWS: 'verdant_haven_reviews'
  };

  const CURRENCY_RATES = {
    USD: { symbol: '$', rate: 1.0, name: 'USD ($)' },
    EUR: { symbol: '€', rate: 0.92, name: 'EUR (€)' },
    GBP: { symbol: '£', rate: 0.79, name: 'GBP (£)' }
  };

  const PRODUCTS = [
    {
      id: 'monstera-deliciosa',
      name: 'Monstera Deliciosa',
      binomial: 'Monstera Deliciosa Liebm.',
      family: 'Araceae',
      tag: 'Greenhouse Bestseller',
      price: 94,
      originalPrice: 108,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAwIjeUJVEsZ9wCzkg6Dh_ysWnm2T03QiN9OEQUKVHTFyj-O6UcK9_mwGNnWoVGqtd9r3JBTO4qq5V5zJCHJRQ2shG9Plkij4HnVQgnsS0shGg_k7KSOTf2S2-X6t18laPA0qX569usK2xT5z7eInE_m51YNwHGEwiUKnfMSdNuXy7lda6mqlA0kVCOtyLIY9v6TTcYQZFvO73fZc4proksxPV1VEFWrqCuZ8oCKNX6mupWS1NEsaW3Jg',
      category: 'aroids',
      light: 'Bright Ind.',
      humidity: '65% RH',
      water: 'Bi-Weekly',
      petSafe: false,
      careLevel: 'Easy',
      accessionId: 'MD-2025-V7',
      stock: 12,
      description: 'Epiphytic architectural aroid with dramatic fenestrated foliage, potted in hand-thrown breathable Tuscan terracotta with living bio-substrate Formula A-7.'
    },
    {
      id: 'philodendron-spiritus-sancti',
      name: 'Philodendron Spiritus Sancti',
      binomial: 'Philodendron spiritus-sancti Bunting',
      family: 'Araceae',
      tag: 'CITES Registered DNA Verified',
      price: 1450,
      originalPrice: 1600,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuB6jhhxYrVHekghiGZbGAAFLkMQIh7QXMS7oitulwIzwr_gPDKj0J1l1RU9WTSr0WiIhxflmjhJiXX5aVjhMaNHruNFOJII-qCkM9UYZQ27jFo1jf_uutv7_-u2Wj9PN8XSVgaW9HZEoOSs-6Y0On1dIq32K8JY7vItc66O-NNJezNYFVPLhuQq14U7Ui3OSIdhdGL6y1lDJDGaEEH-pkA0AgSKsLLCvNgUz53dfHgTurRF3pINdhtjNg',
      category: 'rare',
      light: 'Dappled',
      humidity: '75% RH',
      water: 'Formula B-2',
      petSafe: false,
      careLevel: 'Advanced',
      accessionId: 'PSS-8812',
      stock: 1,
      description: 'Ultra-rare endangered Brazilian archival specimen with pendant sword-like leaves accessioned from lineage clone. Delivered by private botanical courier.'
    },
    {
      id: 'ficus-lyrata',
      name: 'Ficus Lyrata Standard',
      binomial: 'Ficus lyrata Warb.',
      family: 'Moraceae',
      tag: 'Aged 4-Year Canopy Standard',
      price: 240,
      originalPrice: 280,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuA1MQ_z8wkSvP0WH2cc1Nei7kl2atQnJkiseFBfYCaJFbvxbj4WYIxB5pnacCVzMjkVz_ubsd_9cw3prUSH4LHl0WwVLFkyRfw6IhCOTkbXoiIXKGPlvCrPhnMxbdYIdXN7iNVqYk2sRyek3mHlM0zd-w-6EoH7lWh1XVe-lZzYWVet0mT55eg-Sa12Prt8XwxdWpW3k50ctK78Axqr5TjsapvsZ7iC-adH1BIht6R8b-j-8O8QN30wrw',
      category: 'trees',
      light: 'Direct AM',
      humidity: '55% RH',
      water: 'Weekly Soak',
      petSafe: false,
      careLevel: 'Moderate',
      accessionId: 'FL-4091',
      stock: 5,
      description: 'Single-stem standard fiddle leaf fig tree trained over 4 years. Shipped in thermal wooden suspension crating to eliminate branch transit shock.'
    },
    {
      id: 'calathea-orbifolia',
      name: 'Calathea Orbifolia',
      binomial: 'Goeppertia orbifolia Borchs.',
      family: 'Marantaceae',
      tag: 'Non-Toxic / Pet Friendly',
      price: 95,
      originalPrice: 110,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBaF2PJj_c8KSFOYmYABE_tHv6X1eLd8x-htfZGyR1VqI_LgfciFKa2HFrep2HsjZzVhk2IZ-msXdne-1jyd1kpuE0ymBlLl9c6h--8j4S2EsHgqkR9Vf3a1HMaa9r8WID5fz7zoQaZ40fvFPhgerXkDYceWxrqlKvx_5o-NMBg7d3KyQ-Y-WGBWHlLkIVuqAl78797glg9kvEmPL0e_2lD33at9QDANjUXZFe1uV4YKJTMZJ87YCcz1A',
      category: 'low-light',
      light: 'Med Dapple',
      humidity: '70% RH',
      water: 'Rainwater',
      petSafe: true,
      careLevel: 'Moderate',
      accessionId: 'CO-1934',
      stock: 14,
      description: 'Prayer plant specialist with broad circular leaves and metallic silver stripes. Conditioned on pure reverse osmosis water, completely pet-safe.'
    },
    {
      id: 'anthurium-regale',
      name: 'Anthurium Regale',
      binomial: 'Anthurium regale Linden',
      family: 'Araceae',
      tag: 'Velvety Silver Veination',
      price: 320,
      originalPrice: 360,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuD6riIcYkWTKW_EKlbt24opM6n70AuyM5ny5WBJl0QNqjXcPDu7lin9Va400PoNp-FuT6BiRnqS9eG43z0qs1Odc2OuuFjyUHyZYW3Xw7y2ER6dpP4m8m2vucEKGeErvFmgWJP0oQsvM2fVvnrEo8DyBI7pOWm2iAGvzscpgexJ8iTUQuaNnfLq2wnVP1ZTVVJ0SenDNjKunWkSgE1LzjxS-Kz4DOU2eTo855e1owQ4TaoqO3JFgJ8nnA',
      category: 'rare',
      light: 'Bright Ind.',
      humidity: '75% RH',
      water: 'Sphag/Pumice',
      petSafe: false,
      careLevel: 'Advanced',
      accessionId: 'AR-6102',
      stock: 2,
      description: 'Neotropical cardiocaule with massive emerald cordate leaves and crystalline white veins. Linked to telemetry disc #AR-90 with micro-climate alerts.'
    },
    {
      id: 'ficus-audrey',
      name: 'Ficus Audrey Standard',
      binomial: 'Ficus benghalensis L.',
      family: 'Moraceae',
      tag: 'Hardy Architectural Tree',
      price: 145,
      originalPrice: 165,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC7IwjBLtEKTwK1daQaFAegyAifbiZ5rbz5y1YkZDyztDfuZPEo1KHMOVw11smpeDdoNjJbHR4eP5j9jNawcCs6CLxTcrOKquHopDsbhdQJ7Zc7jQNrPpMNwEQC9rJ5dqJ__ngDwEvjdG-E3cQ2ae8SjEKKbQE8ZXYEk4lBD_sVIo2E0UomhRqkhS70hau0r_suSiXlddXMGjQrz2oH0RL5xu_EwW518pT1vScAgn76sQvwDecZ0N9kig',
      category: 'trees',
      light: 'Bright Ind.',
      humidity: '50% RH',
      water: 'Weekly',
      petSafe: false,
      careLevel: 'Easy',
      accessionId: 'FA-2025-V2',
      stock: 8,
      description: 'Stately specimen tree with velvety emerald foliage and chalk-white bark. Significantly more forgiving and draft-tolerant than traditional fiddle leaves.'
    },
    {
      id: 'philodendron-gloriosum',
      name: 'Philodendron Gloriosum',
      binomial: 'Philodendron gloriosum André',
      family: 'Araceae',
      tag: 'Crawling Heart Leaf',
      price: 110,
      originalPrice: 130,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCi3XpeJn5uuwmfNFgHpVl4eLsDKg5IcpPbDOq7BUGLj13vzZlFRo2Hsa_7Jm1-X_IV57SKwIJ4zsU4op0CCgMZYQfkGG5NK0x0cJAjncqyfNBXDle0X5XdlnqGreWDf7abQYz6-qM-7ZcpiSJgVajJ9QCkUW5zj0BKTMpkkZW4Df9kUEuChhPHkCUnprG9c6NOROB72-SwoPNgf_8wAojcN_cCNeio0vHNGoIbGV7MAp5y0x9YVOkhww',
      category: 'aroids',
      light: 'Med Dapple',
      humidity: '65% RH',
      water: 'Bi-Weekly',
      petSafe: false,
      careLevel: 'Easy',
      accessionId: 'PG-2025-V4',
      stock: 7,
      description: 'Terrestrial crawler featuring oversized velvety foliage with striking pink margins and bright white leaf ribs. Specimen includes custom rectangular planter.'
    },
    {
      id: 'tuscan-terracotta-vessel',
      name: 'Tuscan Terracotta Artisanal Vessel',
      binomial: 'Hand-thrown Italian Earthenware',
      family: 'Vessels & Pottery',
      tag: 'Kiln Fired Handcrafted',
      price: 42,
      originalPrice: 50,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCoCV7FC2dKZXWyJ3VvZU3ETl1iZy_odzhLxyVxRUC05GoBhaggxbKvlQR3p2UXVSI0fbgH6N5wjhq6yMXLxs6iuzW70CSWdnFIb1kUx9Nas5pUoOlWsiQYyJ9_bIne-EAP656_04bHQDpN5ymelguT5StPb1dLroU-kuwkw8oYy-HzCv2XEdqa5g8_607-uGYOvxdHtQf-gYKWqMQG5n6Ybh7Rr3mQw56uc4q4eiV6koqk8H-8IUhKLQ',
      category: 'vessels',
      light: 'All',
      humidity: 'Breathable',
      water: 'Drainage Built-In',
      petSafe: true,
      careLevel: 'Easy',
      accessionId: 'VES-802',
      stock: 24,
      description: 'Raw oxide porous Tuscan clay promoting natural root evaporation and aeration. Includes matching unglazed terracotta drainage saucer plate.'
    }
  ];

  // Default initial cart if empty
  const DEFAULT_CART = [
    {
      id: 'monstera-deliciosa',
      name: 'Monstera Deliciosa',
      binomial: 'Monstera Deliciosa Liebm.',
      size: 'Medium (8" Nursery Pot)',
      vessel: 'Terracotta Natural',
      material: 'Raw Tuscan Terracotta',
      drainageTray: true,
      price: 94.00,
      unitPrice: 94.00,
      quantity: 1,
      image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDiBSlfn0RAGyyFyIn05mmaHXEou3PFowbDnXfTQScgaOrkKnQJvmzpKm_WH4Xy_jeMGFziV34Jk8jWKPKgugxx--X43c0vMDEuZhbE2vn8OY4DVAPWoFRYxhlhh3jSoGHnrz6j7HR2QRAjP5JbM2WFziEd1nhU-ZaH7T0l0Rw1sS9vvgInSAz2z4xejiKo2_GdFkU-5Kr2W2afKH6XScihL8g1fpbmzAt7E2v2jJ5qSgut1gux1QG_SA',
      accessionId: 'MD-2025-V7'
    }
  ];

  // User default
  const DEFAULT_USER = {
    name: 'Clara Vance',
    email: 'clara.vance@conservatory.org',
    role: 'Tier I Specimen Guardian',
    avatar: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBFozqNo4T_xhfNVgAnqgnpcHzTwow7HxLwxOe0iJPti0ROf9HCuKvGGsqRJlwN-ki8FKaLYJYG5MoKfL0HEyLjRR8oaKcBHOH_ZwPZdR1CaIah049rfbj_g_Ov4cNqC34FkC8b1pNbj_ceYWG45QRsoMV3JJlmgu3bmQ2EPVj2P2W6jeU0Q3PTRxQ-iOuADPuoAcsQ1HBSjLMuEYB97ztA4xCZGTfFW6A0aC3eBv0sfwWFpDxojIHTCw',
    address: '4820 NW Skyline Blvd, Portland, OR 97229',
    linkedPassports: ['MD-2025-V7', 'FA-2025-V2'],
    isLoggedIn: true
  };

  // State initialization
  function getCart() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.CART);
      if (!data) {
        localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify(DEFAULT_CART));
        return DEFAULT_CART;
      }
      return JSON.parse(data);
    } catch (e) {
      return DEFAULT_CART;
    }
  }

  function saveCart(cart) {
    localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify(cart));
    window.dispatchEvent(new CustomEvent('verdant:cart-updated', { detail: { cart } }));
  }

  function addToCart(item) {
    const cart = getCart();
    // Check if same item with same options exists
    const existingIndex = cart.findIndex(c => 
      c.id === item.id && 
      c.size === item.size && 
      c.vessel === item.vessel && 
      c.drainageTray === item.drainageTray
    );

    if (existingIndex > -1) {
      cart[existingIndex].quantity += (item.quantity || 1);
    } else {
      cart.push({
        id: item.id || 'custom-specimen',
        name: item.name || 'Botanical Specimen',
        binomial: item.binomial || '',
        size: item.size || 'Medium (8" Pot)',
        vessel: item.vessel || 'Terracotta Natural',
        material: item.material || 'Raw Tuscan Terracotta',
        drainageTray: item.drainageTray !== false,
        price: Number(item.price) || 94.00,
        unitPrice: Number(item.price) || 94.00,
        quantity: Number(item.quantity) || 1,
        image: item.image || PRODUCTS[0].image,
        accessionId: item.accessionId || 'MD-2025-V7'
      });
    }

    saveCart(cart);
    showToast('Added to Botanical Bag', `${item.name} (${item.size}) has been reserved.`, 'check_circle', 'success');
    return cart;
  }

  function removeFromCart(index) {
    const cart = getCart();
    if (index >= 0 && index < cart.length) {
      const removed = cart.splice(index, 1)[0];
      saveCart(cart);
      showToast('Specimen Removed', `${removed.name} was removed from your bag.`, 'delete', 'info');
    }
    return cart;
  }

  function updateQuantity(index, delta) {
    const cart = getCart();
    if (index >= 0 && index < cart.length) {
      cart[index].quantity = Math.max(1, cart[index].quantity + delta);
      saveCart(cart);
    }
    return cart;
  }

  function clearCart() {
    saveCart([]);
  }

  function getCartSubtotal() {
    const cart = getCart();
    return cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  }

  function getCartCount() {
    const cart = getCart();
    return cart.reduce((count, item) => count + item.quantity, 0);
  }

  // Wishlist
  function getWishlist() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.WISHLIST);
      return data ? JSON.parse(data) : ['monstera-deliciosa', 'calathea-orbifolia', 'anthurium-regale'];
    } catch (e) {
      return ['monstera-deliciosa'];
    }
  }

  function toggleWishlist(productId) {
    const list = getWishlist();
    const index = list.indexOf(productId);
    let added = false;
    if (index > -1) {
      list.splice(index, 1);
      showToast('Removed from Wishlist', 'Specimen removed from your conservatory wishlist.', 'favorite_border', 'info');
    } else {
      list.push(productId);
      added = true;
      showToast('Added to Wishlist', 'Specimen saved to your botanical wishlist.', 'favorite', 'success');
    }
    localStorage.setItem(STORAGE_KEYS.WISHLIST, JSON.stringify(list));
    window.dispatchEvent(new CustomEvent('verdant:wishlist-updated', { detail: { wishlist: list, productId, added } }));
    return added;
  }

  function isWishlisted(productId) {
    return getWishlist().includes(productId);
  }

  // Currency
  function getCurrency() {
    return localStorage.getItem(STORAGE_KEYS.CURRENCY) || 'USD';
  }

  function setCurrency(curr) {
    if (CURRENCY_RATES[curr]) {
      localStorage.setItem(STORAGE_KEYS.CURRENCY, curr);
      window.dispatchEvent(new CustomEvent('verdant:currency-updated', { detail: { currency: curr } }));
      document.querySelectorAll('.currency-value').forEach(el => {
        const usdVal = parseFloat(el.getAttribute('data-usd') || el.textContent.replace(/[^0-9.]/g, ''));
        if (!isNaN(usdVal)) {
          el.textContent = formatPrice(usdVal);
        }
      });
    }
  }

  function formatPrice(amountInUSD) {
    const curr = getCurrency();
    const info = CURRENCY_RATES[curr] || CURRENCY_RATES.USD;
    const converted = amountInUSD * info.rate;
    return `${info.symbol}${converted.toFixed(2)}`;
  }

  // User
  function getUser() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.USER);
      return data ? JSON.parse(data) : DEFAULT_USER;
    } catch (e) {
      return DEFAULT_USER;
    }
  }

  function saveUser(user) {
    localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(user));
    window.dispatchEvent(new CustomEvent('verdant:user-updated', { detail: { user } }));
  }

  // Toast System
  function showToast(title, message, icon = 'local_florist', type = 'info') {
    let container = document.getElementById('verdant-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'verdant-toast-container';
      container.className = 'fixed bottom-6 right-6 z-[9999] flex flex-col gap-3 pointer-events-none';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'pointer-events-auto flex items-start gap-3 p-4 min-w-[320px] max-w-[420px] bg-surface-container-lowest/95 backdrop-blur-md rounded-xl shadow-2xl border border-primary/10 transform translate-y-8 opacity-0 transition-all duration-300 ease-out';
    
    const iconColor = type === 'success' ? 'text-secondary' : type === 'error' ? 'text-error' : 'text-primary';
    
    toast.innerHTML = `
      <div class="w-10 h-10 rounded-full bg-surface-container flex items-center justify-center shrink-0 ${iconColor}">
        <span class="material-symbols-outlined text-[20px]">${icon}</span>
      </div>
      <div class="flex-1 min-w-0">
        <h4 class="font-title-md text-[15px] font-bold text-primary leading-tight">${title}</h4>
        <p class="font-body-sm text-[13px] text-on-surface-variant mt-0.5 leading-snug">${message}</p>
      </div>
      <button class="text-outline hover:text-primary transition-colors p-1" onclick="this.parentElement.remove()">
        <span class="material-symbols-outlined text-[16px]">close</span>
      </button>
    `;

    container.appendChild(toast);

    // Animate in
    requestAnimationFrame(() => {
      toast.classList.remove('translate-y-8', 'opacity-0');
    });

    // Auto remove after 4.5 seconds
    setTimeout(() => {
      toast.classList.add('translate-y-4', 'opacity-0');
      setTimeout(() => toast.remove(), 350);
    }, 4500);
  }

  return {
    PRODUCTS,
    CURRENCY_RATES,
    getCart,
    saveCart,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    getCartSubtotal,
    getCartCount,
    getWishlist,
    toggleWishlist,
    isWishlisted,
    getCurrency,
    setCurrency,
    formatPrice,
    getUser,
    saveUser,
    showToast
  };
})();

window.VerdantStore = VerdantStore;
