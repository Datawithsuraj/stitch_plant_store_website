from bs4 import BeautifulSoup

def enhance_video_call():
    with open('video-call.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the right sidebar container
    sidebar = soup.find('div', class_=lambda c: c and 'lg:col-span-5' in c)
    if not sidebar:
        print("Sidebar not found in video-call.html")
        return

    # Find the inner workspace container
    card = sidebar.find('div', class_=lambda c: c and 'bg-surface-container-lowest' in c)
    if not card:
        print("Card not found in video-call.html")
        return

    # Insert Tabs under the green header
    tabs_html = '''
    <div class="flex items-center border-b border-outline-variant/30 bg-surface-container-low px-2 pt-2 gap-1" id="call-sidebar-tabs">
      <button onclick="switchCallTab('rx')" id="call-tab-rx" class="call-tab active px-3 py-2 text-xs font-bold border-b-2 border-primary text-primary flex items-center gap-1.5 transition-all">
        <span class="material-symbols-outlined text-[15px]">clinical_notes</span>
        <span>Clinical Rx</span>
      </button>
      <button onclick="switchCallTab('pedigree')" id="call-tab-pedigree" class="call-tab px-3 py-2 text-xs font-semibold text-on-surface-variant hover:text-primary flex items-center gap-1.5 transition-all">
        <span class="material-symbols-outlined text-[15px]">history_edu</span>
        <span>Pedigree</span>
      </button>
      <button onclick="switchCallTab('chat')" id="call-tab-chat" class="call-tab px-3 py-2 text-xs font-semibold text-on-surface-variant hover:text-primary flex items-center gap-1.5 transition-all">
        <span class="material-symbols-outlined text-[15px]">chat</span>
        <span>Live Chat</span>
        <span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
      </button>
    </div>
    '''

    header = card.find('div', class_=lambda c: c and 'bg-primary' in c)
    if header:
        header.insert_after(BeautifulSoup(tabs_html, 'html.parser'))

    # Wrap the existing checklist & Rx in panel-rx
    checklist = card.find('div', class_=lambda c: c and 'p-space-md flex flex-col gap-space-sm border-b' in c)
    rx_sec = card.find('div', class_=lambda c: c and 'p-space-md flex flex-col gap-space-md' in c)
    
    # Create the other two panels
    other_panels = '''
    <!-- PANEL PEDIGREE -->
    <div id="call-panel-pedigree" class="hidden p-space-md flex flex-col gap-space-sm text-xs text-on-surface-variant">
      <div class="p-3 bg-surface-container-low rounded-xl border border-primary/10">
        <span class="font-label-sm uppercase tracking-wider text-secondary font-bold block mb-1">Archival Accession Record</span>
        <h4 class="font-headline-sm text-sm text-primary font-serif italic">Monstera Deliciosa Liebm. (Batch #MD-2025-V7)</h4>
        <div class="mt-2 space-y-1 font-mono text-[11px]">
          <div>Lineage: <strong>Sauvie Island F1 Clonal Line</strong></div>
          <div>Substrate: <strong>Formula A-7 (Pine Bark, Perlite, Worm Castings)</strong></div>
          <div>Vessel: <strong>8-Inch Breathable Tuscan Terracotta</strong></div>
          <div>Hardened: <strong>28 Days in Glasshouse Bay 04</strong></div>
          <div>NFC Brass Tag: <strong>#MD-772 (Verified Active)</strong></div>
        </div>
      </div>
      <a href="passport.html" class="w-full py-2.5 bg-primary text-on-primary text-center rounded-xl font-bold hover:bg-primary-container transition-colors">Open Full Living Passport</a>
    </div>

    <!-- PANEL LIVE CHAT -->
    <div id="call-panel-chat" class="hidden flex flex-col h-[380px] p-space-md">
      <div id="chatMessages" class="flex-1 overflow-y-auto space-y-2.5 pr-1 text-xs">
        <div class="flex items-start gap-2">
          <div class="w-6 h-6 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold text-[10px] shrink-0">EA</div>
          <div class="bg-surface-container-low p-2.5 rounded-xl rounded-tl-none text-on-surface">
            <strong>Dr. Elena:</strong> Welcome Clara! I can see your Monstera's canopy clearly. Leaf 3 shows great turgor. Could you tilt the camera toward the pot rim?
          </div>
        </div>
        <div class="flex items-start gap-2 justify-end">
          <div class="bg-primary text-on-primary p-2.5 rounded-xl rounded-tr-none text-right">
            <strong>You:</strong> Just did! Is the soil moisture level looking okay?
          </div>
        </div>
        <div class="flex items-start gap-2">
          <div class="w-6 h-6 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold text-[10px] shrink-0">EA</div>
          <div class="bg-surface-container-low p-2.5 rounded-xl rounded-tl-none text-on-surface">
            <strong>Dr. Elena:</strong> Yes! Top 2 inches are perfectly drying. We will schedule your next deep soak for Saturday morning.
          </div>
        </div>
      </div>
      <div class="pt-2 border-t border-primary/10 flex items-center gap-1.5 mt-2">
        <input type="text" id="chatInput" placeholder="Message Dr. Elena..." class="flex-1 px-3 py-1.5 text-xs bg-surface-container-low border border-outline-variant rounded-lg focus:outline-none focus:ring-1 focus:ring-primary" />
        <button onclick="sendConsultChatMessage()" class="px-3 py-1.5 bg-primary text-on-primary hover:bg-primary-container rounded-lg text-xs font-bold">Send</button>
      </div>
    </div>
    '''

    card.append(BeautifulSoup(other_panels, 'html.parser'))

    # Wrap checklist and rx in panel-rx
    wrapper = soup.new_tag('div', id='call-panel-rx', class_='flex flex-col')
    if checklist:
        checklist.wrap(wrapper)
        if rx_sec:
            wrapper.append(rx_sec)

    # Add JavaScript
    script = '''
    <script>
      function switchCallTab(tabId) {
        document.querySelectorAll('.call-tab').forEach(b => {
          b.classList.remove('border-b-2', 'border-primary', 'text-primary', 'font-bold');
          b.classList.add('text-on-surface-variant', 'font-semibold');
        });

        const activeBtn = document.getElementById(`call-tab-${tabId}`);
        if (activeBtn) {
          activeBtn.classList.remove('text-on-surface-variant', 'font-semibold');
          activeBtn.classList.add('border-b-2', 'border-primary', 'text-primary', 'font-bold');
        }

        ['call-panel-rx', 'call-panel-pedigree', 'call-panel-chat'].forEach(id => {
          const el = document.getElementById(id);
          if (el) el.classList.add('hidden');
        });

        const activePanel = document.getElementById(`call-panel-${tabId}`);
        if (activePanel) activePanel.classList.remove('hidden');
      }

      function sendConsultChatMessage() {
        const input = document.getElementById('chatInput');
        const box = document.getElementById('chatMessages');
        if (!input || !box || !input.value.trim()) return;

        const userMsg = input.value.trim();
        input.value = '';

        const userDiv = document.createElement('div');
        userDiv.className = 'flex items-start gap-2 justify-end';
        userDiv.innerHTML = `<div class="bg-primary text-on-primary p-2.5 rounded-xl rounded-tr-none text-right"><strong>You:</strong> ${userMsg}</div>`;
        box.appendChild(userDiv);
        box.scrollTop = box.scrollHeight;

        setTimeout(() => {
          const botDiv = document.createElement('div');
          botDiv.className = 'flex items-start gap-2';
          botDiv.innerHTML = `<div class="w-6 h-6 rounded-full bg-primary text-on-primary flex items-center justify-center font-bold text-[10px] shrink-0">EA</div><div class="bg-surface-container-low p-2.5 rounded-xl rounded-tl-none text-on-surface"><strong>Dr. Elena:</strong> Recorded that observation into your acclimation log, Clara! Turgor index is responding favorably.</div>`;
          box.appendChild(botDiv);
          box.scrollTop = box.scrollHeight;
        }, 1200);
      }

      // Mic & Cam toggles
      document.addEventListener('DOMContentLoaded', () => {
        const micBtn = document.querySelector('button[aria-label="Toggle Microphone"]');
        let micActive = true;
        if (micBtn) {
          micBtn.onclick = () => {
            micActive = !micActive;
            const icon = micBtn.querySelector('.material-symbols-outlined');
            if (icon) icon.textContent = micActive ? 'mic' : 'mic_off';
            micBtn.classList.toggle('bg-error/20');
            micBtn.classList.toggle('text-error');
            VerdantStore.showToast('Microphone', micActive ? 'Microphone unmuted.' : 'Microphone muted.', 'mic', 'info');
          };
        }

        const camBtn = document.querySelector('button[aria-label="Toggle Video Camera"]');
        let camActive = true;
        if (camBtn) {
          camBtn.onclick = () => {
            camActive = !camActive;
            const icon = camBtn.querySelector('.material-symbols-outlined');
            if (icon) icon.textContent = camActive ? 'videocam' : 'videocam_off';
            camBtn.classList.toggle('bg-error/20');
            camBtn.classList.toggle('text-error');
            VerdantStore.showToast('Camera', camActive ? 'Video stream enabled.' : 'Video stream paused.', 'videocam', 'info');
          };
        }

        const snapBtn = document.querySelector('button span.material-symbols-outlined:contains("photo_camera")')?.parentElement || document.querySelectorAll('button')[3];
        if (snapBtn) {
          snapBtn.addEventListener('click', () => {
            document.body.classList.add('flash-effect');
            setTimeout(() => document.body.classList.remove('flash-effect'), 200);
            VerdantStore.showToast('Foliar Macro Snapshot', 'High-res image captured and pinned to Dr. Alvarez clinical dossier.', 'camera', 'success');
          });
        }
      });
    </script>
    '''

    soup.body.append(BeautifulSoup(script, 'html.parser'))

    with open('video-call.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced video-call.html tabs, chat, and camera controls!")

if __name__ == '__main__':
    enhance_video_call()
