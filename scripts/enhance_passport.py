with open('passport.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """    function switchSpecimenView(viewType, btn) {
      const display = document.getElementById('specimen-display');
      const buttons = document.querySelectorAll('.tab-btn');
      
      // Update Tab Styles
      buttons.forEach(b => {
        b.classList.remove('bg-primary', 'text-on-primary');
        b.classList.add('bg-surface-container', 'text-on-surface-variant');
      });
      btn.classList.remove('bg-surface-container', 'text-on-surface-variant');
      btn.classList.add('bg-primary', 'text-on-primary');

      // Update Imagery placeholder description and trigger visual transition
      display.style.opacity = '0.5';
      setTimeout(() => {
        if(viewType === 'canopy') {
          display.setAttribute('data-alt', 'Macro photograph of a luxuriant Monstera Deliciosa canopy with emerald split leaves showing intricate natural vascular leaf venation and glossy cuticle sheen.');
        } else if(viewType === 'fenestration') {
          display.setAttribute('data-alt', 'Close-up botanical laboratory analysis of Monstera Deliciosa leaf fenestrations, demonstrating double perforations and pristine margin cell structure under soft laboratory lighting.');
        } else if(viewType === 'rootnet') {
          display.setAttribute('data-alt', 'High definition conservatory inspection of potted root ball network showing thick healthy white primary feeder roots and rich porous terracotta mycorrhizal soil substrate.');
        } else if(viewType === 'lineage') {
          display.setAttribute('data-alt', 'Historic conservatory mother plant Monstera Deliciosa climbing a cedar conservatory pillar in a Victorian botanical glasshouse with lush green light.');
        }
        display.style.opacity = '1';
      }, 150);
    }"""

replacement = """    const PASSPORT_VIEWS = {
      canopy: {
        img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuChvYkunOOEVd-SSsdh7tWtQPCLADQecqR98ATlI2v5HybaDVCHqAEfQWL7WjPxI-I7HkDPhwincKGBjwewVjwpbVYStTDg-ezjui9B05HGUOSm48oketNy_IKtmQcFd7xA57BjsPK3dnrtpgXJ6bITqLiFfstnG0oo9U5nWieEt9zLo5DXK72qEglmC05OVzjWA_3eE85boa9YmxRL1ckKSNtiGTl8gStkI_DV35RMDdP0uC5QKSSfNQ',
        tag: 'Accession #MD-2025-V7',
        subtag: 'Sauvie Island Lot #04',
        pinpoint: '6th Primary Fenestration unfurled Jan 31. Zero foliar browning.',
        badgeTitle: 'Optical Biometric Pass',
        badgeValue: 'Grade AAA Exemplar',
        toast: 'Displaying Current Living Canopy (Day 48)'
      },
      fenestration: {
        img: 'https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=1200&q=80',
        tag: 'Fenestration Analysis #FEN-992',
        subtag: 'Double Perforated Apical Blade',
        pinpoint: 'Double perforations confirmed across 4 mature leaves. Symmetry: 98.4%.',
        badgeTitle: 'Cuticle Integrity Check',
        badgeValue: 'Tier 1 Prime Fenestration',
        toast: 'Displaying Biometric Leaf Fenestration Analysis'
      },
      rootnet: {
        img: 'https://images.unsplash.com/photo-1545241047-6083a3684587?auto=format&fit=crop&w=1200&q=80',
        tag: 'Substrate & Root Core #RC-402',
        subtag: 'Porous Terracotta / A-7 Mix',
        pinpoint: 'Mycorrhizae colonized at 87%. Non-encircling active feeder root network.',
        badgeTitle: 'Root System Audit',
        badgeValue: '99.2% Pristine Viability',
        toast: 'Displaying Root Ball & Substrate Permeability Audit'
      },
      lineage: {
        img: 'https://images.unsplash.com/photo-1512428813834-c702c7702b78?auto=format&fit=crop&w=1200&q=80',
        tag: 'Botanical Lineage (F1 Clonal)',
        subtag: 'Parent Stock #OAX-1894 • Bay A',
        pinpoint: 'Clonally propagated from 130-year-old Pacific Northwest botanical matriarch vine.',
        badgeTitle: 'Taxonomic Certificate',
        badgeValue: 'F1 True Heritage Stock',
        toast: 'Displaying Historic Glasshouse F1 Lineage Dossier'
      }
    };

    function switchSpecimenView(viewType, btn) {
      const display = document.getElementById('specimen-display');
      const buttons = document.querySelectorAll('.tab-btn');
      const view = PASSPORT_VIEWS[viewType] || PASSPORT_VIEWS.canopy;
      
      // Update Tab Styles
      buttons.forEach(b => {
        b.classList.remove('bg-primary', 'text-on-primary');
        b.classList.add('bg-surface-container', 'text-on-surface-variant');
      });
      btn.classList.remove('bg-surface-container', 'text-on-surface-variant');
      btn.classList.add('bg-primary', 'text-on-primary');

      // Animate Transition
      display.style.opacity = '0.3';
      display.style.transform = 'scale(0.99)';
      setTimeout(() => {
        display.style.backgroundImage = `url('${view.img}')`;
        
        // Update tags and pinpoints
        const tagEl = display.querySelector('.font-label-sm.text-primary.uppercase');
        const subtagEl = display.querySelector('.font-body-sm.text-on-surface-variant');
        const pinpointEl = display.querySelector('.group .opacity-0');
        const badgeTitleEl = display.querySelector('.font-label-sm.uppercase.font-semibold');
        const badgeValEl = display.querySelector('.font-title-md.font-serif');

        if (tagEl) tagEl.textContent = view.tag;
        if (subtagEl) subtagEl.textContent = view.subtag;
        if (pinpointEl) pinpointEl.textContent = view.pinpoint;
        if (badgeTitleEl) badgeTitleEl.textContent = view.badgeTitle;
        if (badgeValEl) badgeValEl.textContent = view.badgeValue;

        display.style.opacity = '1';
        display.style.transform = 'scale(1)';
        VerdantStore.showToast('Herbarium View', view.toast, 'microbiology', 'success');
      }, 150);
    }"""

if target in content:
    content = content.replace(target, replacement)
    with open('passport.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enhanced passport.html switchSpecimenView!")
else:
    print("Target string not found in passport.html")
