import streamlit as st
import base64
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

ASSETS_DIR = Path("assets")
EXTS = [".jpg", ".jpeg", ".png", ".webp"]

ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "palms", "thurible",
    "relic", "rosary", "cord", "scapular",
    "monstrance", "eucharistic_host"
]

# ---------- DESCRIPTIONS ----------
DESC = {
    "ashes": """Ashes, used on Ash Wednesday, date back to the early Church and Jewish penitential practices. The imposition of ashes recalls mortality and repentance, connecting Christians to ancient Israelite traditions and reminding them of Genesis 3:19. 

In our present liturgy for Ash Wednesday, we use ashes made from the burned palm branches distributed on the Palm Sunday of the previous year. The priest blesses the ashes and imposes them on the foreheads of the faithful, making the sign of the cross and saying, “Remember, man you are dust and to dust you shall return,” or “Turn away from sin and be faithful to the Gospel.”

When we begin the holy season of Lent in preparation for Easter, we mourn and do penance for our sins, convert our hearts to the Lord, renew baptismal promises, and look forward to the kingdom of God.""",
    # ... keep other descriptions unchanged, break into short paragraphs similarly
    "eucharistic_host": """The Eucharistic Host, unleavened bread, becomes the Body of Christ at the consecration. 

Reserved for adoration and Communion, the Host has been central since the Last Supper and was solemnly elevated in the Mass by the 12th century."""
}

# ---------- UTILITIES ----------
def humanize(key: str) -> str:
    return key.replace("_", " ").title()

def first_existing(stem: Path) -> Path | None:
    for ext in EXTS:
        p = stem.with_suffix(ext)
        if p.exists():
            return p
    return None

def multiple_existing(stem: Path, max_images=3):
    """Return up to max_images existing files: item, item_1, item_2..."""
    results = []
    candidates = [stem] + [stem.parent / f"{stem.name}_{i}" for i in range(1, max_images)]
    for candidate in candidates:
        p = first_existing(candidate)
        if p:
            results.append(p)
    return results

def read_bytes(path: Path) -> bytes | None:
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception:
        return None

def img_data_uri(path: Path | None, fallback: Path | None) -> str:
    def to_uri(p: Path, data: bytes) -> str:
        mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"
    if path:
        data = read_bytes(path)
        if data:
            return to_uri(path, data)
    if fallback:
        fb = read_bytes(fallback)
        if fb:
            return f"data:image/jpeg;base64,{base64.b64encode(fb).decode('utf-8')}"
    return ""

# ---------- BACKGROUND ----------
bg_file = first_existing(ASSETS_DIR / "background")
ph_file = first_existing(ASSETS_DIR / "placeholder")
bg_uri = img_data_uri(bg_file, ph_file)

# ---------- STYLES ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Cinzel+Decorative:wght@700&display=swap');

.stApp {{
  background-image: linear-gradient(rgba(10,10,20,0.55), rgba(10,10,20,0.55)), url('{bg_uri}');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  min-height: 200vh; /* increase page height for full background */
}}

h1.app-title {{
  font-family: 'IM Fell English SC', 'Cinzel Decorative', serif;
  text-align: center;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0,0,0,0.6);
  letter-spacing: 0.5px;
  margin: 10px 0 24px 0;
  font-size: 2.4rem;
}}

section.main > div.block-container {{
  padding-top: 1.0rem;
  padding-bottom: 4.0rem; /* more bottom space */
}}

.sac-card {{
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 22px;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}}

.sac-img {{
  width: 100%;
  display: block;
  border-radius: 12px;
  transition: transform .25s ease, filter .25s ease, box-shadow .25s ease;
  box-shadow: 0 0 0 rgba(255,255,255,0);
}}
.sac-img:hover {{
  transform: translateY(-4px) scale(1.05);
  filter: brightness(1.06);
  box-shadow: 0 14px 34px rgba(255,255,220,0.28);
}}
.expanded-img {{
  transform: scale(1.15);
}}

div[data-testid="stExpander"] > details {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}}
div[data-testid="stExpander"] summary {{
  color: #fff;
  font-weight: 700;
}}
div[data-testid="stExpander"] p, div[data-testid="stExpander"] div p {{
  color: #f2f2f2;
  line-height: 1.5;
  margin-bottom: 0.8rem;
}}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='app-title'>Catholic Sacramentals</h1>", unsafe_allow_html=True)

# ---------- GRID ----------
cols = st.columns(3, gap="large")

for idx, key in enumerate(ITEM_KEYS):
    col = cols[idx % 3]
    with col:
        images = multiple_existing(ASSETS_DIR / key, max_images=3)
        st.markdown('<div class="sac-card">', unsafe_allow_html=True)
        if images:
            if len(images) > 1:
                # Carousel: simple swipe using horizontal radio buttons
                options = list(range(len(images)))
                selected = st.radio("", options, horizontal=True, label_visibility="collapsed", key=f"radio_{key}")
                img_uri = img_data_uri(images[selected], ph_file)
                st.markdown(f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img"/>', unsafe_allow_html=True)
            else:
                img_uri = img_data_uri(images[0], ph_file)
                st.markdown(f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img"/>', unsafe_allow_html=True)

        with st.expander(humanize(key), expanded=False):
            # enlarge image when expanded
            if images:
                img_uri = img_data_uri(images[0], ph_file)
                st.markdown(f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img expanded-img"/>', unsafe_allow_html=True)
            text = DESC.get(key, "Description coming soon.")
            # Break into paragraphs
            for para in text.split("\n"):
                if para.strip():
                    st.write(para.strip())

        st.markdown('</div>', unsafe_allow_html=True)
