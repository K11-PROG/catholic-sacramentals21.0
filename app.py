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

    A crucifix (from the Latin cruci fixus meaning '(one) fixed to a cross') is a cross with an image of Jesus on it, as distinct from a bare cross. The representation of Jesus himself on the cross is referred to in English as the corpus (Latin for 'body'). The crucifix emphasizes Jesus' sacrifice, including his death by crucifixion, which Christians believe brought about the redemption of mankind. Most crucifixes portray Jesus on a Latin cross, rather than a Tau cross or a Coptic cross.

    Western crucifixes usually have a three-dimensional corpus, but in Eastern Orthodoxy Jesus' body is normally painted on the cross, or in low relief. Strictly speaking, to be a crucifix, the cross must be three-dimensional, but this distinction is not always observed. An entire painting of the crucifixion of Jesus including a landscape background and other figures is not a crucifix either.

On some crucifixes a skull and crossbones are shown below the corpus, referring to Golgotha (Calvary), the site at which Jesus was crucified, which the Gospels say means in Hebrew "the place of the skull. Medieval tradition held that it was the burial-place of Adam and Eve, and that the cross of Christ was raised directly over Adam's skull, so many crucifixes manufactured in Catholic countries still show the skull and crossbones below the corpus. There may also be a short projecting nameplate, showing the letters INRI (Greek: INBI).

Western crucifixes may show Christ dead or alive, the presence of the spear wound in his ribs traditionally indicating that he is dead. In either case his face very often shows his suffering. Eastern crucifixes have Jesus' two feet nailed side by side, rather than crossed one above the other, as Western crucifixes have shown them since around the 13th century. The crown of thorns is also generally absent in Eastern crucifixes, since the emphasis is not on Christ's suffering, but on his triumph over sin and death. It was in Italy that the emphasis was put on Jesus' suffering and realistic details, during a process of general humanization of Christ favored by the Franciscan order.

In the early Church, many Christians hung a cross on the eastern wall of their house in order to indicate the eastward direction of prayer.[13][14] Prayer in front of a crucifix, which is seen as a sacramental, is often part of devotion for Christians, especially those worshipping in a church, also privately. The person may sit, stand, or kneel in front of the crucifix, sometimes looking at it in contemplation, or merely in front of it with head bowed or eyes closed. During the Middle Ages small crucifixes, generally hung on a wall, became normal in the personal cells or living quarters first of monks, then all clergy, followed by the homes of the laity, spreading down from the top of society as these became cheap enough for the average person to afford. Most towns had a large crucifix erected as a monument, or some other shrine at the crossroads of the town.

The crucifix confronts the believer with the Passion and remains central to Catholic identity, often blessed for protection.""",
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
    """
    Try to locate a higher-resolution alternative near the original:
    name_hires, name_full, name@2x, name_large (same extension priority order).
    Falls back to original if none found.
    """
    if not original_path:
        return None
    stem = original_path.with_suffix("")  # drop ext
    # Candidates without ext; we add EXTS below
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
  cursor: zoom-in;
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

/* ---- Modal Lightbox ---- */
#lightbox-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.85);
  backdrop-filter: blur(2px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}}
#lightbox-overlay.show {{ display: flex; }}

#lightbox-content {{
  position: relative;
  max-width: 96vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}}
#lightbox-img {{
  max-width: 96vw;
  max-height: 90vh;
  border-radius: 10px;
  box-shadow: 0 10px 40px rgba(0,0,0,.6);
}}

.lb-btn {{
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 28px;
  line-height: 1;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.35);
  color: #fff;
  padding: 10px 14px;
  border-radius: 12px;
  cursor: pointer;
  user-select: none;
}}
#lb-prev {{ left: -56px; }}
#lb-next {{ right: -56px; }}

#lb-close {{
  position: absolute;
  top: -48px;
  right: 0;
  font-size: 26px;
  background: rgba(255,255,255,0.22);
  border: 1px solid rgba(255,255,255,0.35);
  color: #fff;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
}}

@media (max-width: 768px) {{
  #lb-prev {{ left: -36px; }}
  #lb-next {{ right: -36px; }}
  #lb-close {{ top: -44px; }}
}}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='app-title'>Catholic Sacramentals</h1>", unsafe_allow_html=True)

# ---------- Collect all image URIs per item (for the lightbox) ----------
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
            if len(images) > 1:
                selected = st.radio(
                    "", list(range(len(images))),
                    horizontal=True, label_visibility="collapsed", key=f"radio_{key}"
                )
                show_path = images[selected]
            else:
                show_path = images[0]
            # Use hires if available for display (browser scales it down)
            hires_path = hires_for(show_path)
            img_uri = img_data_uri(hires_path, ph_file)
            # Add data attributes so JS knows which group and index
            st.markdown(
                f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img" '
                f'data-group="{key}" data-index="0"/>',
                unsafe_allow_html=True
            )
        else:
            # fallback placeholder if no item image found
            if ph_file:
                ph_uri = img_data_uri(ph_file, ph_file)
                st.markdown(
                    f'<img src="{ph_uri}" alt="{humanize(key)}" class="sac-img" '
                    f'data-group="{key}" data-index="0"/>',
                    unsafe_allow_html=True
                )

        with st.expander(humanize(key), expanded=False):
            text = DESC.get(key, "Description coming soon.")
            for para in text.split("\n"):
                if para.strip():
                    st.write(para.strip())

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- LIGHTBOX HTML + JS ----------
# Embed the overlay once and provide the images map to JS:
images_json = json.dumps(all_item_uris)

st.components.v1.html(f"""
<div id="lightbox-overlay">
  <div id="lightbox-content">
    <button id="lb-prev" class="lb-btn" aria-label="Previous">‹</button>
    <img id="lightbox-img" src="" alt=""/>
    <button id="lb-next" class="lb-btn" aria-label="Next">›</button>
    <button id="lb-close" aria-label="Close">✕</button>
  </div>
</div>

<script>
(function() {{
  const IMAGES = {images_json};
  const overlay = document.getElementById('lightbox-overlay');
  const imgEl = document.getElementById('lightbox-img');
  const btnPrev = document.getElementById('lb-prev');
  const btnNext = document.getElementById('lb-next');
  const btnClose = document.getElementById('lb-close');

  let currentGroup = null;
  let currentIndex = 0;

  function show(group, index) {{
    const list = IMAGES[group] || [];
    if (!list.length) return;
    currentGroup = group;
    currentIndex = Math.max(0, Math.min(index, list.length - 1));
    imgEl.src = list[currentIndex];
    overlay.classList.add('show');
  }}

  function hide() {{
    overlay.classList.remove('show');
    setTimeout(() => {{ imgEl.src = ''; }}, 200);
  }}

  function next() {{
    if (!currentGroup) return;
    const list = IMAGES[currentGroup] || [];
    currentIndex = (currentIndex + 1) % list.length;
    imgEl.src = list[currentIndex];
  }}

  function prev() {{
    if (!currentGroup) return;
    const list = IMAGES[currentGroup] || [];
    currentIndex = (currentIndex - 1 + list.length) % list.length;
    imgEl.src = list[currentIndex];
  }}

  // Click bindings on images
  function bindImages() {{
    const imgs = document.querySelectorAll('img.sac-img');
    imgs.forEach((el) => {{
      el.addEventListener('click', (e) => {{
        const group = el.getAttribute('data-group');
        // Use 0 as index because we render only the selected image per group in the grid;
        // the full set is available in IMAGES[group] for navigation.
        show(group, 0);
      }});
      // Title tooltip (quick fact): show first 80 chars of the item's name
      const group = el.getAttribute('data-group');
      if (group) {{
        el.title = group.replaceAll('_',' ').replace(/\\b\\w/g, c => c.toUpperCase());
      }}
    }});
  }}

  // Controls
  btnPrev.addEventListener('click', prev);
  btnNext.addEventListener('click', next);
  btnClose.addEventListener('click', hide);
  overlay.addEventListener('click', (e) => {{
    if (e.target === overlay) hide();
  }});

  // Keyboard
  document.addEventListener('keydown', (e) => {{
    if (!overlay.classList.contains('show')) return;
    if (e.key === 'Escape') hide();
    else if (e.key === 'ArrowRight') next();
    else if (e.key === 'ArrowLeft') prev();
  }});

  // Touch swipe
  let touchStartX = 0;
  imgEl.addEventListener('touchstart', (e) => {{
    touchStartX = e.changedTouches[0].screenX;
  }});
  imgEl.addEventListener('touchend', (e) => {{
    const dx = e.changedTouches[0].screenX - touchStartX;
    if (Math.abs(dx) > 40) {{
      if (dx < 0) next(); else prev();
    }}
  }});

  // Initial bind + slight delay for Streamlit rerenders
  bindImages();
  // Rebind after Streamlit updates the DOM
  const mo = new MutationObserver(() => bindImages());
  mo.observe(document.body, {{ childList: true, subtree: true }});
}})();
</script>
""", height=0)
