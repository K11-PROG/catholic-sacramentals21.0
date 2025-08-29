import streamlit as st
import base64
import json
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
    "ashes": """Ashes, used on Ash Wednesday...""",
    "bible": """The Bible, meaning 'books,' is a library...""",
    "blessed_medals": """Blessed medals gained popularity...""",
    "blessed_salt": """Blessed salt, known in the Roman Ritual...""",
    "blessing": """Blessings are among the oldest sacramentals...""",
    "candle": """Candles symbolize Christ as the Light...""",
    "chaplet": """Chaplets are prayer beads beyond the rosary...""",
    "crucifix": """The crucifix, with the figure of Christ...""",
    "holy_bells": """Bells were blessed as early as the 8th century...""",
    "holy_card": """Holy cards began as woodcuts...""",
    "holy_doors": """Holy Doors, opened during Jubilee years...""",
    "holy_images": """Holy images trace to the earliest Christian catacombs...""",
    "holy_oil": """Holy oil has Old Testament roots...""",
    "holy_water": """Holy water has its roots in early Christian practices...""",
    "incense": """Incense was offered in the Temple...""",
    "liturgical_vestments": """Vestments evolved from Roman attire...""",
    "palms": """Palms, blessed on Palm Sunday...""",
    "thurible": """The thurible or censer holds burning charcoal...""",
    "relic": """Relics have been venerated since the 2nd century...""",
    "rosary": """The rosary’s origins lie in the 12th-13th century...""",
    "cord": """Cords, like the Cord of St. Joseph or St. Philomena...""",
    "scapular": """The scapular developed from monastic habits...""",
    "monstrance": """Monstrances developed in the 13th century...""",
    "eucharistic_host": """The Eucharistic Host, unleavened bread..."""
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

def to_data_uri(p: Path, data: bytes) -> str:
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"

def img_data_uri(path: Path | None, fallback: Path | None) -> str:
    if path:
        data = read_bytes(path)
        if data:
            return to_data_uri(path, data)
    if fallback:
        fb = read_bytes(fallback)
        if fb:
            return f"data:image/jpeg;base64,{base64.b64encode(fb).decode('utf-8')}"
    return ""

def hires_for(original_path: Path | None) -> Path | None:
    if not original_path:
        return None
    stem = original_path.with_suffix("")
    suffix_candidates = [f"{stem}", f"{stem}_hires", f"{stem}_full", f"{stem}@2x", f"{stem}_large"]
    for base in suffix_candidates:
        for ext in EXTS:
            p = Path(str(base)).with_suffix(ext)
            if p.exists():
                return p
    return original_path

# ---------- BACKGROUND ----------
bg_file = first_existing(ASSETS_DIR / "background")
ph_file = first_existing(ASSETS_DIR / "placeholder")
bg_uri = img_data_uri(bg_file, ph_file)

# ---------- STYLES ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&display=swap');

.stApp {{
  background-image: linear-gradient(rgba(10,10,20,0.55), rgba(10,10,20,0.55)), url('{bg_uri}');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  min-height: 200vh;
}}

h1.app-title {{
  font-family: 'IM Fell English SC', serif;
  text-align: center;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0,0,0,0.6);
  font-size: 2.4rem;
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
  transition: transform .3s ease, filter .3s ease, box-shadow .3s ease;
  cursor: zoom-in;
}}
.sac-img:hover {{
  transform: scale(1.08);
  filter: brightness(1.06);
  box-shadow: 0 14px 34px rgba(255,255,220,0.3);
}}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='app-title'>Catholic Sacramentals</h1>", unsafe_allow_html=True)

# ---------- Collect all image URIs per item ----------
def uris_for_item(item_key: str):
    paths = multiple_existing(ASSETS_DIR / item_key, max_images=3)
    out = []
    for p in paths:
        hi = hires_for(p)
        out.append(img_data_uri(hi, ph_file))
    if not out and ph_file:
        out = [img_data_uri(ph_file, ph_file)]
    return out

all_item_uris = {k: uris_for_item(k) for k in ITEM_KEYS}

# ---------- GRID ----------
cols = st.columns(3, gap="large")

for idx, key in enumerate(ITEM_KEYS):
    col = cols[idx % 3]
    with col:
        images = multiple_existing(ASSETS_DIR / key, max_images=3)
        st.markdown('<div class="sac-card">', unsafe_allow_html=True)
        if images:
            show_path = images[0]
            hires_path = hires_for(show_path)
            img_uri = img_data_uri(hires_path, ph_file)
            st.markdown(
                f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img" '
                f'data-group="{key}" data-index="0"/>',
                unsafe_allow_html=True
            )
            st.session_state["lightbox_img"] = img_uri
        st.expander(humanize(key)).write(DESC.get(key, "Description coming soon."))
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
import streamlit.components.v1 as components

st.markdown("""
<style>
.sidebar-lightbox-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 6px;
    font-size: 22px;
    color: #ddd;
    transition: color .2s ease;
}
.sidebar-lightbox-btn:hover {
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    if "lightbox_img" in st.session_state and st.session_state["lightbox_img"]:
        img_uri = st.session_state["lightbox_img"]
        if st.button("👁️", key="view_btn", help="View full size"):
            components.html(f"""
            <div style="position:fixed;top:0;left:0;width:100%;height:100%;
                        background:rgba(0,0,0,0.85);z-index:9999;
                        display:flex;align-items:center;justify-content:center;">
                <img src="{img_uri}" style="max-width:90%;max-height:90%;border-radius:8px;"/>
            </div>
            """, height=600)
