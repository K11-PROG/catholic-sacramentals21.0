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

# ---------- DESCRIPTIONS (paragraph-form) ----------
DESC = {
    "ashes": """Ashes, used on Ash Wednesday, date back to the early Church and Jewish penitential practices. The imposition of ashes recalls mortality and repentance, connecting Christians to ancient Israelite traditions and reminding them of Genesis 3:19.

In our present liturgy for Ash Wednesday, we use ashes made from the burned palm branches distributed on the Palm Sunday of the previous year. The priest blesses the ashes and imposes them on the foreheads of the faithful, making the sign of the cross and saying, “Remember, man you are dust and to dust you shall return,” or “Turn away from sin and be faithful to the Gospel.”

When we begin the holy season of Lent in preparation for Easter, we mourn and do penance for our sins, convert our hearts to the Lord, renew baptismal promises, and look forward to the kingdom of God.""",
    "bible": """The Bible, meaning 'books,' is a library of sacred writings. It consists of the Old Testament and the New Testament.

The Old Testament is the Hebrew Bible as interpreted among the various branches of Christianity. The New Testament contains the four Gospels (Matthew, Mark, Luke, and John), Acts, 21 letters, and Revelation.

The Gospels narrate the life, death, and teachings of Jesus Christ. The Bible is viewed as the inspired word of God and a guide for Christian living. Catholic editions include the Deuterocanonical books, preserved by the Septuagint. Since the earliest centuries, illuminated manuscripts and later printed Bibles were treasured, forming the foundation of Christian teaching.""",
    "blessed_medals": """Blessed medals gained popularity in the early Middle Ages as tokens of faith and protection.

They commemorate saints, events, or Marian devotions and often bear protective inscriptions. The Miraculous Medal originated from St. Catherine Labouré’s visions in 1830, while the St. Benedict Medal dates back at least to the 11th century, inscribed with prayers of exorcism.""",
    "blessed_salt": """Blessed salt, known in the Roman Ritual, was used as early as the 3rd century.

It recalls Elisha’s purification of water (2 Kings 2:19-22) and symbolizes preservation from corruption and spiritual protection.""",
    "blessing": """Blessings are among the oldest sacramentals, rooted in the Jewish practice of berakhot.

Early Christian communities blessed homes, fields, and travelers. The Roman Pontifical preserved many such prayers, sanctifying daily life.""",
    "candle": """Candles symbolize Christ as the Light of the World. Early Christians used candles in catacombs; by the 4th century, they became standard in liturgy.

Their origins can be traced back to Jewish practices, where a perpetual light was kept in the Temple to signify God's presence, which Christians adapted for their own rituals over time.

There are several types of candles used in the Catholic tradition: the Paschal candle, used during Easter Vigil, represents the Resurrection and light of Christ. Votive candles are lit for specific prayer intentions, often placed before statues or images. Altar candles are present during Mass to signify the presence of Christ in the Eucharist.""",
    "chaplet": """Chaplets are prayer beads beyond the rosary, dating to medieval confraternities.

The Divine Mercy Chaplet, revealed to St. Faustina in the 20th century, shows how these devotions evolve to meet spiritual needs.""",
    "crucifix": """The crucifix, with the figure of Christ, emerged in the 6th century and spread widely by the Middle Ages.

It confronts the believer with the Passion and remains central to Catholic identity, often blessed for protection.""",
    "holy_bells": """Bells were blessed as early as the 8th century, called 'campanae' or 'sacred trumpets.'

Their ringing at Mass or in towers was believed to ward off storms and evil, summoning the faithful to prayer.""",
    "holy_card": """Holy cards began as woodcuts in the late Middle Ages and became popular devotional items by the 17th century.

They often depict saints or events and were used as catechetical tools.""",
    "holy_doors": """Holy Doors, opened during Jubilee years, originated in the 15th century at St. Peter’s Basilica.

Passing through them symbolizes spiritual renewal and the reception of special indulgences.""",
    "holy_images": """Holy images trace to the earliest Christian catacombs. Icons flourished in the East; statues in the West.

The Second Council of Nicaea (787) affirmed their veneration, not worship, as windows to the divine.""",
    "holy_oil": """Holy oil has Old Testament roots (Exodus 30). Chrism was mentioned by Church Fathers like Tertullian and Hippolytus.

Consecrated oils are still used in Baptism, Confirmation, Holy Orders, and the Anointing of the Sick.""",
    "holy_water": """Holy water reflects ancient Jewish purification rites and was noted by the 4th century.

It is exorcised and blessed, reminding the faithful of Baptism and serving as protection against evil.""",
    "incense": """Incense was offered in the Temple of Jerusalem and adopted by Christians by the 4th century.

Its smoke symbolizes prayers rising to heaven (Psalm 141:2) and sanctifies the liturgy.""",
    "liturgical_vestments": """Vestments evolved from Roman attire. By the 5th century, they became distinct for worship.

Colors signify liturgical seasons, and garments like the chasuble and stole symbolize Christ’s yoke and charity.""",
    "palms": """Palms, blessed on Palm Sunday, recall Christ’s entry into Jerusalem.

The custom dates back to the 4th century in Jerusalem and spread throughout Christendom as a sign of victory and hope.""",
    "thurible": """The thurible or censer holds burning charcoal and incense. Its use mirrors Jewish Temple worship and became a fixed part of Christian liturgy by the 6th century.

Its fragrant smoke signifies reverence and prayer.""",
    "relic": """Relics have been venerated since the 2nd century, with martyrs’ graves becoming pilgrimage sites.

The Council of Trent affirmed their use, and they remain integral to altars and devotions.""",
    "rosary": """The rosary’s origins lie in the 12th-13th century, with Dominican promotion by St. Dominic.

It unites vocal prayer and meditation on Christ’s life and Mary’s role, a devotion embraced worldwide.""",
    "cord": """Cords, like the Cord of St. Joseph or St. Philomena, appeared in the 17th century.

Worn around the waist, they symbolize purity, fidelity, and special petitions for protection and grace.""",
    "scapular": """The scapular developed from monastic habits. The Brown Scapular, linked to Our Lady of Mount Carmel in the 13th century, became a sign of Marian devotion and consecration.""",
    "monstrance": """Monstrances developed in the 13th century to display the consecrated Host during adoration and processions.

Often gilded and radiant, they emphasize Christ’s Real Presence and became common after Corpus Christi was established in 1264.""",
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
  min-height: 200vh;
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
  padding-bottom: 4.0rem;
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
  box-shadow: 0 0 0 rgba(255,255,255,0);
}}
.sac-img:hover {{
  transform: scale(1.08);
  filter: brightness(1.06);
  box-shadow: 0 14px 34px rgba(255,255,220,0.3);
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
                selected = st.radio("", list(range(len(images))),
                                    horizontal=True, label_visibility="collapsed", key=f"radio_{key}")
                img_uri = img_data_uri(images[selected], ph_file)
            else:
                img_uri = img_data_uri(images[0], ph_file)
            st.markdown(f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img"/>', unsafe_allow_html=True)

        with st.expander(humanize(key), expanded=False):
            text = DESC.get(key, "Description coming soon.")
            for para in text.split("\n"):
                if para.strip():
                    st.write(para.strip())

        st.markdown('</div>', unsafe_allow_html=True)
