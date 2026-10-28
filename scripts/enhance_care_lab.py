import re
from bs4 import BeautifulSoup

def update_care_lab():
    with open('care-lab.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the category tabs div
    tab_container = None
    for div in soup.find_all('div'):
        if 'flex flex-wrap gap-1.5' in ' '.join(div.get('class', [])) and 'Foliar' in div.get_text():
            tab_container = div
            break

    if tab_container:
        tab_container.clear()
        tab_container['id'] = 'care-zone-tabs'
        tab_container.append(BeautifulSoup('''
          <button data-zone="foliar" class="zone-tab active px-space-sm py-1.5 bg-primary text-on-primary rounded font-label-sm text-label-sm font-semibold shadow-sm transition-all" type="button">
            Foliar &amp; Blade
          </button>
          <button data-zone="petiole" class="zone-tab px-space-sm py-1.5 bg-surface-container text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high rounded font-label-sm text-label-sm transition-all" type="button">
            Petiole &amp; Stem
          </button>
          <button data-zone="root" class="zone-tab px-space-sm py-1.5 bg-surface-container text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high rounded font-label-sm text-label-sm transition-all" type="button">
            Root &amp; Substrate
          </button>
          <button data-zone="pest" class="zone-tab px-space-sm py-1.5 bg-surface-container text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high rounded font-label-sm text-label-sm transition-all" type="button">
            Pest Vector
          </button>
        ''', 'html.parser'))

    # Ensure symptom container has an ID
    symptom_container = soup.find('div', class_=re.compile(r'space-y-space-xs'))
    if symptom_container:
        symptom_container['id'] = 'symptom-matrix-container'

    # Add interactive JavaScript at end of body
    script = BeautifulSoup('''
    <script>
      const SYMPTOM_DATA = {
        foliar: [
          { id: 'f1', name: 'Marginal Leaf Crisping & Tip Necrosis', desc: 'Brittle brown leaf borders radiating inward from lateral veins', match: '94% Match', checked: true, badgeClass: 'bg-secondary-container text-on-secondary-fixed' },
          { id: 'f2', name: 'Interveinal Chlorosis', desc: 'Paling tissue between primary structural veins; deep green veins preserved', match: 'Detected', checked: true, badgeClass: 'bg-surface-container-high text-primary' },
          { id: 'f3', name: 'Loss of Petiole Turgor / Drooping', desc: 'Cellular hydrostatic slackness across lowest two petioles', match: 'Subtle (12%)', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'f4', name: 'Guttation & Edema Blistering', desc: 'Overpressure blisters on abaxial (underside) cuticle layer', match: 'None', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' }
        ],
        petiole: [
          { id: 'p1', name: 'Loss of Petiole Turgor / Hydrostatic Drooping', desc: 'Petiole angle dropped below 45 degrees relative to vertical stem axis', match: '82% Match', checked: true, badgeClass: 'bg-secondary-container text-on-secondary-fixed' },
          { id: 'p2', name: 'Aerial Root Tip Desiccation', desc: 'Brown calloused tips on emergent adventitious nodes', match: '65% Match', checked: false, badgeClass: 'bg-surface-container-high text-primary' },
          { id: 'p3', name: 'Basal Collar Mechanical Constriction', desc: 'Tight substrate binding at the soil line restricting sap flow', match: 'Low (15%)', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'p4', name: 'Vascular Darkening at Petiole Node', desc: 'Internal discoloration indicating potential fungal vascular wilt', match: 'None', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' }
        ],
        root: [
          { id: 'r1', name: 'Perched Water Table Saturation', desc: 'Persistent bottom saturation from heavy non-porous peat layering', match: '91% Match', checked: true, badgeClass: 'bg-secondary-container text-on-secondary-fixed' },
          { id: 'r2', name: 'Anaerobic Substrate Odor / Pythium Risk', desc: 'Lack of aeration in root core giving damp sour substrate aroma', match: '85% Match', checked: true, badgeClass: 'bg-secondary-container text-on-secondary-fixed' },
          { id: 'r3', name: 'Hydrophobic Channeling in Peat Core', desc: 'Water drains rapidly through fissures without wetting root ball', match: '25% Match', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'r4', name: 'Terracotta Salt Efflorescence Crust', desc: 'White mineral residue accumulating on porous pot exterior', match: 'Present (45%)', checked: false, badgeClass: 'bg-surface-container-high text-primary' }
        ],
        pest: [
          { id: 'x1', name: 'Tetranychidae Spider Mite Webbing', desc: 'Microscopic silk filaments in leaf axils with yellow stippling', match: 'Undetected', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'x2', name: 'Thrips Silvery Scarring & Fecal Specks', desc: 'Silvery sheen on upper blade surface with tiny black frass spots', match: 'Undetected', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'x3', name: 'Pseudococcidae Cottony Wax Cushions', desc: 'White mealybug clusters hidden in petiole sheaths and leaf joints', match: 'Undetected', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' },
          { id: 'x4', name: 'Diaspididae Armor Scale Clusters', desc: 'Hard brown waxy bumps adhering tightly to petioles and main veins', match: 'Undetected', checked: false, badgeClass: 'bg-surface-container text-on-surface-variant' }
        ]
      };

      let currentZone = 'foliar';

      function renderSymptoms(zone) {
        currentZone = zone;
        const list = SYMPTOM_DATA[zone] || [];
        const container = document.getElementById('symptom-matrix-container');
        if (!container) return;

        const checkedCount = list.filter(item => item.checked).length;

        container.innerHTML = `
          <div class="flex items-center justify-between pb-1">
            <span class="font-label-sm text-label-sm uppercase tracking-wide text-on-surface-variant font-semibold">Active ${zone.toUpperCase()} Symptoms</span>
            <span id="cv-count-badge" class="font-label-sm text-label-sm text-secondary font-medium">${checkedCount} Detected by CV</span>
          </div>
          ${list.map((item, idx) => `
            <label class="flex items-start gap-space-sm p-space-sm rounded-lg ${item.checked ? 'bg-secondary/10 border border-secondary/20' : 'hover:bg-surface-container-low'} cursor-pointer transition-all">
              <input type="checkbox" ${item.checked ? 'checked' : ''} onchange="toggleSymptom('${zone}', ${idx}, this.checked)" class="mt-1 w-4 h-4 accent-primary rounded cursor-pointer" />
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between gap-2">
                  <span class="font-title-md text-title-md text-on-surface text-sm sm:text-base ${item.checked ? 'font-semibold text-primary' : ''}">${item.name}</span>
                  <span class="px-2 py-0.5 rounded-full ${item.badgeClass} text-label-sm font-semibold shrink-0">${item.match}</span>
                </div>
                <p class="font-body-sm text-body-sm text-on-surface-variant mt-0.5">${item.desc}</p>
              </div>
            </label>
          `).join('')}
        `;
      }

      function toggleSymptom(zone, index, isChecked) {
        if (SYMPTOM_DATA[zone] && SYMPTOM_DATA[zone][index]) {
          SYMPTOM_DATA[zone][index].checked = isChecked;
          renderSymptoms(zone);
          
          const totalChecked = Object.values(SYMPTOM_DATA).flat().filter(s => s.checked).length;
          VerdantStore.showToast('Diagnostic Recalibrated', `${totalChecked} symptom vectors active. Prescription adjusted.`, 'biotech', 'success');
        }
      }

      document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.zone-tab').forEach(btn => {
          btn.addEventListener('click', () => {
            document.querySelectorAll('.zone-tab').forEach(b => {
              b.classList.remove('bg-primary', 'text-on-primary');
              b.classList.add('bg-surface-container', 'text-on-surface-variant');
            });
            btn.classList.remove('bg-surface-container', 'text-on-surface-variant');
            btn.classList.add('bg-primary', 'text-on-primary');
            renderSymptoms(btn.getAttribute('data-zone'));
          });
        });
        renderSymptoms('foliar');
      });
    </script>
    ''', 'html.parser')

    soup.body.append(script)

    with open('care-lab.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced care-lab.html tabs!")

if __name__ == '__main__':
    update_care_lab()
