import glob
from bs4 import BeautifulSoup

def inspect_all():
    for f in sorted(glob.glob("*.html")):
        soup = BeautifulSoup(open(f, encoding="utf-8"), "html.parser")
        print(f"=== {f} ===")
        # Look for navs
        for nav in soup.find_all("nav"):
            links = [(a.get_text(strip=True)[:20], a.get("href")) for a in nav.find_all("a")]
            if links:
                print(f"  Nav ({len(links)} links): {links}")
        
        # Look for button groups / tabs
        for div in soup.find_all(["div", "ul"]):
            classes = " ".join(div.get("class", []))
            if any(k in classes for k in ["tab", "segmented", "filter", "pills", "flex-wrap"]):
                btns = div.find_all(["button", "a"], recursive=False)
                if len(btns) >= 2:
                    names = [b.get_text(strip=True)[:25] for b in btns]
                    print(f"  Group in {classes[:35]}: {names}")

if __name__ == "__main__":
    inspect_all()
