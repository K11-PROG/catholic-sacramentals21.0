import streamlit as st
import base64
import os
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

ASSETS_DIR = Path("assets")
# Supported image extensions to try in order
EXTS = [".jpg", ".jpeg", ".png", ".webp"]

# The 24 sacramentals (exact, lowercase, underscores)
ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "medal", "palms", "pilgrimage_item",
    "relic", "rosary", "sacramentals_of_the_dead", "sacapular",
    "sign_of_the_cross",
]

# ---------- DESCRIPTIONS (extensive but readable) ----------
DESC = {
    "ashes": "Ashes, blessed and imposed on Ash Wednesday, signify repentance and our mortality—“Remember you are dust…”. The custom echoes ancient Jewish and early Christian penitential practice and became universal in the medieval West. The cross traced on the forehead calls us to conversion and a renewed Lent.",
    "bible": "The Holy Bible, inspired Word of God, is the Church’s foundational book of faith and worship. Catholic editions include the deuterocanon. From handwritten codices and illuminated manuscripts to print, the Church has preserved and proclaimed Scripture in liturgy and life for two millennia.",
    "blessed_medals": "Blessed medals (e.g., Miraculous Medal, St. Benedict Medal) bear sacred images and prayers, asking God’s help and saints’ intercession. Their popularity surged in modern centuries, yet they reflect the Church’s ancient instinct to keep holy reminders close to daily life.",
    "blessed_salt": "Blessed salt symbolizes covenant, preservation, and protection. Used historically in scrutinies for baptism and in exorcisms, it recalls Christ’s “You are the salt of the earth.” Sprinkled with faith, it’s a reminder that all creation is ordered to God’s praise.",
    "blessing": "Blessings invoke God’s favor upon people, places, and things. Rooted in Scripture and the Church’s earliest worship, blessings set apart everyday life for divine purposes, acknowledging that every good is from the Lord and returns to Him in thanksgiving.",
    "candle": "Blessed candles recall Christ the Light. From catacombs to Candlemas processions, candlelight marks Christian prayer, sacrament, and vigil. At home, a blessed candle symbolizes watchful hope and Christ’s presence amid darkness.",
    "chaplet": "Chaplets are structured prayers on beads (e.g., Divine Mercy) that combine vocal prayer with meditation. Flourishing since the late medieval period, they help sanctify time and focus the heart on the mysteries of salvation.",
    "crucifix": "The crucifix—Christ on the Cross—keeps before our eyes the Paschal Mystery. Venerated since the early centuries, it graces altars and homes as a sign of love stronger than death, a silent homily of mercy and redemption.",
    "holy_bells": "Blessed bells summon the faithful, mark sacred moments, and—according to venerable custom—dispel fear. Medieval Christians rang church bells in storms and processions; their sound still calls hearts to prayer and praise.",
    "holy_card": "Holy cards—small sacred images with prayers—proliferated with printing. Tucked into missals and wallets, they are “pocket icons” that teach, console, and invite us to imitate Christ and the saints.",
    "holy_doors": "Holy Doors, opened during Jubilees since the 15th century, symbolize Christ the Gate of Mercy. Passing through with faith obtains special indulgences and renews the pilgrim heart for mission.",
    "holy_images": "Icons, statues, and sacred art sprang from the Incarnation: the invisible God made visible in Christ. From catacomb frescoes to Renaissance altarpieces, images are windows that lift the mind to divine realities.",
    "holy_oil": "Sacred oils—chrism, catechumens’, and the sick—are consecrated at the Chrism Mass. Since apostolic times, the Church has anointed in sacraments, invoking the Spirit’s healing, strengthening, and consecrating power.",
    "holy_water": "Holy water recalls Baptism and is used to bless, to protect, and to dedicate spaces and lives to God. Flicked from a font or carried home in bottles, it is a humble conduit of grace.",
    "incense": "Incense, a fragrant sign of prayer rising to God (cf. Ps 141:2), graces Christian liturgy from earliest times, echoing temple worship. Its smoke veils the holy with mystery and reverent joy.",
    "liturgical_vestments": "From Roman garments grew the alb, stole, chasuble and more—vesture whose colors and forms proclaim seasons and feasts. Vestments are not costumes but signs of office and service in Christ.",
    "medal": "Beyond particular devotions, medals commemorate sacraments and pilgrimages. Blessed and worn in faith, they’re daily reminders to “put on the Lord Jesus Christ” and live as His disciples.",
    "palms": "Blessed palms recall Christ’s entry into Jerusalem. Kept in homes or woven into small crosses, they connect Palm Sunday’s hosannas with the Passion and our call to follow the Lord to Easter.",
    "pilgrimage_item": "Tokens from holy places—water, stones, cloths—remember journeys of conversion. Since antiquity, Christian pilgrims have sought grace at tombs and shrines, returning as witnesses to hope.",
    "relic": "Relics (first-, second-, third-class) are tangible links to the saints, venerated since the early Church at martyrs’ tombs. They spur imitation, draw us into the communion of saints, and magnify God’s wonders in His friends.",
    "rosary": "The Rosary, perfected in the Middle Ages, weds vocal prayer with contemplation of Christ’s mysteries in Mary’s school. The gentle rhythm beads grace into daily life and anchors the soul in the Gospel.",
    "sacramentals_of_the_dead": "For the dying, sacramentals—crucifix, candle, prayers—surround the Anointing and Viaticum with faith’s tenderness. Christians have kept such watch since the beginning, entrusting loved ones to the Lord.",
    "sacapular": "The scapular (notably the Brown Scapular of Carmel) reflects a medieval monastic garment refashioned as a sign of Marian devotion and discipleship—an outward reminder to live the Gospel faithfully.",
    "sign_of_the_cross": "Tracing the Cross while invoking the Trinity is one of Christianity’s oldest prayers. It marks us as Christ’s own and sanctifies our speaking, working, and suffering with His saving sign.",
}

# ---------- UTILITIES ----------
def humanize(key: str) -> str:
    return key.replace("_", " ").title()

def first_existing(path_stem: Path) -> Path | None:
    """Return first existing file among supported EXTS for a given stem."""
    for ext in EXTS:
        p = path_stem.with_suffix(ext)
        if p.exists():
            return p
    return None

def read_bytes(path: Path) -> bytes | None:
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception:
        return None

def b64_of(path: Path) -> str | None:
    data = read_bytes(path)
    return base64.b64encode(data).decode("utf-8") if data else None

def img_data_uri(path: Path, fallback: Path) -> str:
    """Return a data: URI for path or fallback if missing/unreadable."""
    candidate = read_bytes(path)
    if candidate:
        # Try to guess mime by extension; browsers handle it fine
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(candidate).decode('utf-8')}"
    # fallback
    fb = read_bytes(fallback)
    return f"data:image/jpeg;base64,{base64.b64encode(fb).decode('utf-8')}" if fb else ""

# ---------- BACKGROUND (BASE64 CSS) ----------
bg_file = first_existing(ASSETS_DIR / "background")
ph_file = first_existing(ASSETS_DIR / "placeholder")  # global placeholder
if ph_file is None:
    # Ensure at least some placeholder exists to avoid broken UI
    st.warning("Missing assets/placeholder.(jpg|png|webp). Please add one.")
bg_uri = img_data_uri(bg_file, ph_file) if bg_file else (img_data_uri(ph_file, ph_file) if ph_file else "")

st.markdown(
    f"""
    <style>
      /* App background */
      .stApp {{
        background-image: linear-gradient(rgba(10,10,20,0.55), rgba(10,10,20,0.55)), url('{bg_uri}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
      }}
      /* Card & hover glow for images */
      .sac-card {{
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 16px;
        padding: 16px;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      }}
      .sac-img {{
        width: 100%;
        border-radius: 12px;
        display: block;
        transition: transform .25s ease, filter .25s ease, box-shadow .25s ease;
        box-shadow: 0 0 0 rgba(255,255,255,0);
      }}
      .sac-img:hover {{
        transform: translateY(-4px) scale(1.02);
        filter: brightness(1.06);
        box-shadow: 0 14px 32px rgba(255,255,220,0.25);
      }}
      .sac-title {{
        margin: 10px 0 6px 0;
        font-weight: 700;
        font-size: 1.05rem;
      }}
      .sac-desc {{
        font-size: 0.95rem;
        line-height: 1.5;
      }}
      /* Make Streamlit columns gap a bit tighter visually */
      section.main > div.block-container {{
        padding-top: 1.2rem;
        padding-bottom: 2rem;
      }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color: #fff; text-shadow: 0 2px 8px rgba(0,0,0,.4)'>Catholic Sacramentals</h1>", unsafe_allow_html=True)
st.caption("Drop your images into the **assets/** folder using the exact filenames below. Missing or invalid images fall back to **placeholder**.")

# ---------- GRID RENDER ----------
# Build three columns responsive grid
cols = st.columns(3, gap="large")

for idx, key in enumerate(ITEM_KEYS):
    col = cols[idx % 3]
    with col:
        # Find the item image (try multiple extensions), or fallback to placeholder
        img_path = first_existing(ASSETS_DIR / key)
        placeholder_path = ph_file  # already resolved above
        if placeholder_path is None:
            # If absolutely nothing exists, skip rendering the image but keep text
            img_uri = ""
        else:
            use_path = img_path if img_path else placeholder_path
            img_uri = img_data_uri(use_path, placeholder_path)

        st.markdown('<div class="sac-card">', unsafe_allow_html=True)

        if img_uri:
            st.markdown(
                f"""
                <img src="{img_uri}" alt="{humanize(key)}" class="sac-img"/>
                """,
                unsafe_allow_html=True
            )

        st.markdown(f'<div class="sac-title">{humanize(key)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sac-desc">{DESC.get(key, "Description coming soon.")}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER HINT ----------
st.markdown("---")
st.info(
    "🖼️ **Add/replace images:** put files in `assets/` named exactly like the items "
    f"({', '.join(ITEM_KEYS[:6])}, ...). Supported: {', '.join(EXTS)}. "
    "Background image should be `assets/background.(jpg|png|webp)`. A global `assets/placeholder.(jpg|png|webp)` "
    "is used when an image is missing or invalid."
)
