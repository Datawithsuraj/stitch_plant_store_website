from bs4 import BeautifulSoup

def enhance_reviews():
    with open('reviews.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 1. Update filter pills
    filters_container = soup.find('div', class_=lambda c: c and 'overflow-x-auto' in c and 'scrollbar-none' in c)
    if filters_container:
        btns = filters_container.find_all('button')
        filter_keys = ['all', 'monstera', 'aroids', 'ficus', 'rare', 'photos']
        for btn, k in zip(btns, filter_keys):
            btn['data-review-filter'] = k
            btn['class'] = ['review-filter-btn', 'px-space-sm', 'py-1.5', 'rounded-lg', 'whitespace-nowrap', 'cursor-pointer', 'text-label-sm', 'font-label-sm', 'transition-all']
            if k == 'all':
                btn['class'].extend(['bg-primary', 'text-on-primary', 'shadow-sm'])
            else:
                btn['class'].extend(['bg-surface-container', 'hover:bg-surface-container-high', 'text-on-surface'])

    # 2. Tag review articles
    articles = soup.find_all('article')
    categories = [
        'monstera aroids photos',
        'ficus photos',
        'aroids photos',
        'rare aroids photos'
    ]
    for art, cat in zip(articles, categories):
        art['data-category'] = cat
        art['class'] = art.get('class', []) + ['review-item', 'transition-all', 'duration-300']

    # 3. Add search input ID
    search_input = soup.find('input', placeholder=lambda p: p and 'Search chronicles' in p)
    if search_input:
        search_input['id'] = 'reviewSearchInput'

    # 4. Append script
    script = BeautifulSoup('''
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const filterBtns = document.querySelectorAll('.review-filter-btn');
        const articles = document.querySelectorAll('.review-item');
        const searchInput = document.getElementById('reviewSearchInput');
        let currentFilter = 'all';

        function applyReviewFilter() {
          const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
          let visibleCount = 0;

          articles.forEach(art => {
            const cat = art.getAttribute('data-category') || '';
            const text = art.textContent.toLowerCase();
            const matchesFilter = currentFilter === 'all' || cat.includes(currentFilter);
            const matchesQuery = !query || text.includes(query);

            if (matchesFilter && matchesQuery) {
              art.style.display = 'block';
              art.style.opacity = '1';
              visibleCount++;
            } else {
              art.style.display = 'none';
              art.style.opacity = '0';
            }
          });
        }

        filterBtns.forEach(btn => {
          btn.addEventListener('click', () => {
            filterBtns.forEach(b => {
              b.classList.remove('bg-primary', 'text-on-primary', 'shadow-sm');
              b.classList.add('bg-surface-container', 'text-on-surface');
            });
            btn.classList.remove('bg-surface-container', 'text-on-surface');
            btn.classList.add('bg-primary', 'text-on-primary', 'shadow-sm');
            currentFilter = btn.getAttribute('data-review-filter');
            applyReviewFilter();
            VerdantStore.showToast('Reviews Filtered', `Displaying reviews matching: ${btn.textContent.trim().split('(')[0]}`, 'filter_list', 'success');
          });
        });

        if (searchInput) {
          searchInput.addEventListener('input', applyReviewFilter);
        }

        // Star rating in review drawer
        const stars = document.querySelectorAll('#review-form-panel button span.material-symbols-outlined');
        stars.forEach((star, idx) => {
          star.parentElement.addEventListener('click', () => {
            stars.forEach((s, sIdx) => {
              if (sIdx <= idx) {
                s.style.fontVariationSettings = "'FILL' 1";
                s.parentElement.classList.remove('text-outline');
                s.parentElement.classList.add('text-tertiary-container');
              } else {
                s.style.fontVariationSettings = "'FILL' 0";
                s.parentElement.classList.remove('text-tertiary-container');
                s.parentElement.classList.add('text-outline');
              }
            });
            const ratingText = star.parentElement.parentElement.querySelector('span:last-child');
            if (ratingText) {
              const ratingVal = (idx + 1).toFixed(1);
              const labels = ['Needs Attention', 'Fair Acclimation', 'Healthy Specimen', 'Vibrant Specimen', 'Flawless Foliage & Hydrated Roots'];
              ratingText.textContent = `${ratingVal} • ${labels[idx]}`;
            }
          });
        });
      });
    </script>
    ''', 'html.parser')

    soup.body.append(script)

    with open('reviews.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Enhanced reviews.html filters, search, and stars!")

if __name__ == '__main__':
    enhance_reviews()
