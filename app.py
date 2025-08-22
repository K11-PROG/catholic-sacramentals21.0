import os
import base64
import textwrap
from PIL import Image
import streamlit as st

# ---------------------------
# Page & background
# ---------------------------
st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

def _b64(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Subtle stained-glass background (put assets/background.jpg in repo)
bg_b64 = _b64(os.path.join("assets", "background.jpg"))
if bg_b64:
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
          background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                      url("data:image/jpeg;base64,{bg_b64}") center/cover no-repeat fixed;
        }}
        /* soft card style */
        .s-card {{
          background: rgba(255,255,255,0.75);
          backdrop-filter: blur(8px);
          border-radius: 16px;
          padding: 1rem;
          border: 1px solid rgba(0,0,0,0.05);
          box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        }}
        .s-title {{ margin-bottom: .25rem; }}
        .s-muted {{ color: #444; font-size: 0.92rem; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("Catholic Sacramentals Encyclopedia")
st.caption(
    "Brief entries with historical notes and traditional usage. "
    "Replace images in the **assets/** folder using the exact filenames below."
)

# ---------------------------
# Data: titles + image filenames + rich descriptions
# (English only for now)
# ---------------------------
# NOTE: Keep keys in sync with your image names: assets/<key>.jpg
ITEMS = [
    {
        "key": "holy_water_bottle",
        "title": "Holy Water (Bottle)",
        "blurb": "Water blessed by a priest, used for blessing persons, places, and things.",
        "desc": """
**What it is.** Holy water is water blessed with a liturgical blessing. It signifies spiritual cleansing and protection.

**History.** The use of blessed water is attested in the early centuries of Christianity. The **Roman Ritual (1614)** standardized formulas for blessing water, often with exorcised salt mixed in older rites. Parish *stoups* or fonts by church doors for signing oneself with holy water are common by the medieval period.

**Use.** The faithful may keep a small bottle at home for blessing themselves, rooms, or sacramentals. It’s often used when entering a church, recalling Baptism.
""",
    },
    {
        "key": "rosary",
        "title": "Rosary",
        "blurb": "String of beads for meditative prayer on the life of Christ and Mary.",
        "desc": """
**What it is.** A devotional aid of five decades (or more) of beads, used to pray vocal prayers while meditating on the Mysteries.

**History.** Forms of *Psalter-like* bead prayer developed between the **12th–15th centuries**; the Dominican tradition spread the Rosary broadly. **Pope St. Pius V (1569)**, in *Consueverunt Romani Pontifices*, promoted and clarified the Rosary structure. **St. John Paul II (2002)** proposed the Luminous Mysteries.

**Use.** A powerful contemplative prayer, often carried or hung as a sacramental.
""",
    },
    {
        "key": "scapular",
        "title": "Brown Scapular (Carmelite)",
        "blurb": "Two small pieces of cloth connected by strings, worn as a sign of devotion.",
        "desc": """
**What it is.** The Brown Scapular of Our Lady of Mount Carmel is a miniature form of a monastic garment, worn under clothing.

**History.** Carmelite tradition associates the scapular with **St. Simon Stock (†1265)** and a Marian promise (historicity discussed by scholars). The Church approves the scapular as a sign of consecration to Mary and a reminder to live the Gospel. Enrollment is customary.

**Use.** Worn devoutly, coupled with a Christian life and Marian devotion.
""",
    },
    {
        "key": "medal",
        "title": "Devotional Medal (e.g., Miraculous Medal)",
        "blurb": "Blessed medal worn as a sign of faith and protection.",
        "desc": """
**What it is.** Blessed medals depict saints or mysteries (e.g., the Cross, Our Lady).

**History.** A well-known example is the **Miraculous Medal (1830)** revealed to **St. Catherine Labouré** in Paris. Another is the **St. Benedict Medal** (inscriptions known by the 17th c., Jubilee design **1880**). Medals became widespread in early modern Catholic devotion.

**Use.** Worn around the neck or kept on one’s person, reminding the wearer to trust in Christ.
""",
    },
    {
        "key": "crucifix",
        "title": "Crucifix",
        "blurb": "A cross bearing the corpus of Christ; a sign of our redemption.",
        "desc": """
**What it is.** A cross with the Body of Christ represented upon it.

**History.** Crucifixes appear in Christian art by late antiquity, and by the medieval period they are central in churches and homes. The **Council of Trent (16th c.)** affirmed the veneration of sacred images.

**Use.** Displayed in homes, used in prayer, and carried on processions.
""",
    },
    {
        "key": "holy_card",
        "title": "Holy Card",
        "blurb": "Small card with sacred art and a prayer or scripture.",
        "desc": """
**What it is.** A devotional card depicting Christ, Our Lady, or the saints, often with a prayer on the reverse.

**History.** Printing made holy cards widely available from the **16th–19th centuries**; they helped spread catechesis and devotion.

**Use.** Kept in wallets, books, or home altars; given on feast days or at funerals.
""",
    },
    {
        "key": "blessed_salt",
        "title": "Blessed (Exorcised) Salt",
        "blurb": "Salt blessed with special prayers, once often mixed with holy water.",
        "desc": """
**What it is.** Salt blessed with a formula that asks God’s protection; in older rites the salt was explicitly *exorcised*.

**History.** The use of blessed salt is ancient. The **Roman Ritual (1614)** contained prayers for exorcised salt; post-conciliar books retain forms of blessing.

**Use.** Sprinkled in homes or at thresholds; sometimes dissolved in water for a simple blessing.
""",
    },
    {
        "key": "oil_of_the_sick",
        "title": "Oil of the Sick (Holy Oil)",
        "blurb": "Olive oil blessed by a bishop, used primarily in the Sacrament of the Anointing.",
        "desc": """
**Note.** While sacred oils are principally **sacramental matter for sacraments** (e.g., Anointing of the Sick), blessed oils as such are treated reverently.

**History.** Blessing of oils dates to the early Church; the bishop blesses the oils at the **Chrism Mass (Holy Week)**.

**Use.** Reserved for sacramental use; stored safely in parishes.
""",
    },
    {
        "key": "palm_branch",
        "title": "Palm (Palm Sunday)",
        "blurb": "Blessed palm branches recalling Christ’s entry into Jerusalem.",
        "desc": """
**What it is.** Palms blessed on **Palm Sunday** at the start of Holy Week.

**History.** The custom is witnessed in **4th–5th century** Jerusalem (e.g., *Pilgrimage of Egeria*). The blessing and procession developed broadly in the West by the medieval period.

**Use.** Taken home and kept near a crucifix or holy image until they are reverently disposed (often burned).
""",
    },
    {
        "key": "ash_cross",
        "title": "Ashes (Ash Wednesday)",
        "blurb": "Blessed ashes placed on the forehead as a sign of penance.",
        "desc": """
**What it is.** Ashes (traditionally from burned palms) blessed and imposed on **Ash Wednesday**.

**History.** Public penitential practices with ashes are recorded by the **10th–11th centuries** in the West; universal observance followed.

**Use.** The faithful receive the sign of the cross on the forehead: “Remember that you are dust…”
""",
    },
    {
        "key": "holy_chalice",
        "title": "Chalice (Consecrated Vessel)",
        "blurb": "Sacred vessel for the Precious Blood at Mass.",
        "desc": """
**Note.** As a consecrated vessel primarily for the **Eucharist (a Sacrament)**, the chalice is treated with the highest reverence.

**History.** Eucharistic chalices are attested from the earliest liturgies; materials and rubrics developed over centuries.

**Use.** Kept in sacristies; not used as a common devotional object at home.
""",
    },
    {
        "key": "thurible",
        "title": "Thurible (Censer)",
        "blurb": "Vessel for burning incense during liturgical rites.",
        "desc": """
**What it is.** A metal censer swung on chains to cense the altar, Gospel, clergy, and faithful.

**History.** Christian incense use is ancient; thuribles with chains became common in the **medieval** West.

**Use.** Liturgical; at home, blessed incense may be used devotionally with due care.
""",
    },
    {
        "key": "holy_water_font",
        "title": "Holy Water Font (Home/Parish)",
        "blurb": "A small basin holding holy water for blessing oneself.",
        "desc": """
**What it is.** A font at church entrances or small fonts in homes to hold holy water.

**History.** Church stoups near doors appear widely by the **Middle Ages**.

**Use.** The faithful sign themselves on entering and leaving, recalling Baptism.
""",
    },
    {
        "key": "candle",
        "title": "Blessed Candle",
        "blurb": "Wax candle blessed for feast days, prayer, and processions.",
        "desc": """
**What it is.** A candle blessed for devotional or liturgical use.

**History.** **Candlemas (Feb 2)** includes the blessing of candles. Candles symbolize Christ the Light; beeswax has long been preferred in the Latin tradition.

**Use.** Lit in prayer, during storms, or at the sickbed; handled safely and reverently.
""",
    },
    {
        "key": "incense",
        "title": "Incense (Blessed)",
        "blurb": "Aromatic resin used to symbolize prayer rising to God.",
        "desc": """
**What it is.** Resin (e.g., frankincense) sometimes blended with aromatics, blessed for liturgical use.

**History.** Incense was used in the Temple; Christians employed it early, with censing rites developing especially in the **medieval** West.

**Use.** Liturgical censing; at home, small grains may be burned with care and pious intent.
""",
    },
    {
        "key": "bible",
        "title": "Holy Bible",
        "blurb": "The inspired Word of God; blessed copies are kept with reverence.",
        "desc": """
**Note.** The Bible itself is the Word of God; a *blessing* of a copy is a pious custom.

**History.** From scrolls and codices to printed editions after **15th-century** printing, Scripture has been central to Christian prayer.

**Use.** Enthroned at home, read daily; many families have a blessed family Bible.
""",
    },
    {
        "key": "rosary_ring",
        "title": "Rosary Ring",
        "blurb": "A small ring with ten bumps and a cross for discreet rosary prayer.",
        "desc": """
**What it is.** A compact form of the rosary for travel or discreet prayer.

**History.** Rosary counters and rings appear with the spread of rosary devotion from the **late medieval** period onward.

**Use.** Kept on a keychain or finger to pray a decade anywhere.
""",
    },
    {
        "key": "chaplet",
        "title": "Chaplet (Various)",
        "blurb": "Beads for particular devotions (e.g., Divine Mercy Chaplet).",
        "desc": """
**What it is.** Chaplets are rosary-like prayers with specific intentions (e.g., **Divine Mercy, revealed 1930s** to St. Faustina; chaplets of saints).

**History.** Many chaplets arose in **modern** Catholic piety, tailored to devotions and feasts.

**Use.** Prayed privately or in groups, often on dedicated bead sets.
""",
    },
    {
        "key": "cord",
        "title": "Cord (e.g., St. Joseph / St. Philomena)",
        "blurb": "Blessed cord worn as a sign of devotion and purity.",
        "desc": """
**What it is.** A blessed cord associated with a saint’s intercession (e.g., **St. Joseph’s Cord**; **St. Philomena’s Cord** popular since the 19th c.).

**History.** Cord devotions spread particularly in the **18th–19th centuries** with confraternities and indulgenced practices.

**Use.** Worn devoutly with intention to live chastely and prayerfully.
""",
    },
    {
        "key": "blessed_bells",
        "title": "Blessed Bells",
        "blurb": "Bells blessed for churches or domestic use, calling to prayer.",
        "desc": """
**What it is.** Bells blessed to call the faithful, mark the Angelus, or accompany processions.

**History.** Church bell blessing rites are medieval; the custom of naming large bells developed in Europe.

**Use.** Liturgical/processional; small domestic bells may be blessed for prayer reminders.
""",
    },
    {
        "key": "holy_door",
        "title": "Holy Door (Jubilee)",
        "blurb": "A special door opened in Jubilee Years as a sign of grace and pilgrimage.",
        "desc": """
**What it is.** Doors in certain basilicas opened during **Jubilee Years** for pilgrims, signifying Christ the Door (Jn 10:7).

**History.** Roman Holy Doors are attested from the **15th century**; **St. John Paul II (2000)** and **Pope Francis (2015–2016)** popularized wider jubilee celebrations.

**Use.** Pilgrims pass through, fulfilling conditions for special graces/indulgences.
""",
    },
    {
        "key": "monstrance",
        "title": "Monstrance",
        "blurb": "Vessel for Eucharistic exposition and adoration.",
        "desc": """
**Note.** The monstrance holds the **Blessed Sacrament** for adoration (center of Catholic worship).

**History.** Developed in the **late Middle Ages** alongside Corpus Christi processions (established **1264**, *Transiturus* of Urban IV).

**Use.** For exposition/benediction; treated with the greatest reverence.
""",
    },
    {
        "key": "eucharistic_host",
        "title": "Eucharistic Host (Consecrated Species)",
        "blurb": "The Body of Christ—center of the Church’s life (a Sacrament, not merely a sacramental).",
        "desc": """
**Note.** The consecrated Host **is** the Real Presence of Christ—**the Sacrament of the Eucharist**. Mentioned here only to distinguish from sacramentals that point to it.

**History & Use.** Central since the Last Supper; reserved in the tabernacle; adored and received at Mass.
""",
    },
    {
        "key": "holy_relic",
        "title": "Relic (Sacred Relic)",
        "blurb": "Remains or objects connected with a saint, honored as signs of God’s grace.",
        "desc": """
**What it is.** First-class (body), second-class (use), third-class (touched to). Venerated—not worshiped—as God worked in the saints.

**History.** Christian relic veneration is ancient (cf. **martyr shrines** in catacombs). The **Council of Trent** affirmed the practice.

**Use.** Kept and venerated with Church norms; relics of significant rank are ordinarily housed in churches.
""",
    },
]

# Quick lookup by key
ITEMS_BY_KEY = {i["key"]: i for i in ITEMS}

# ---------------------------
# Search / filter
# ---------------------------
query = st.text_input("Search titles & descriptions", placeholder="Try: rosary, medal, ashes…").strip().lower()

def matches(item, q: str) -> bool:
    if not q:
        return True
    hay = (item["title"] + " " + item.get("blurb","") + " " + item.get("desc","")).lower()
    return q in hay

filtered = [it for it in ITEMS if matches(it, query)]

# ---------------------------
# Image helper
# ---------------------------
def show_image_for(key: str):
    """
    Tries to load assets/<key>.jpg -> .png -> .webp
    Falls back to assets/placeholder.jpg if missing or unreadable.
    """
    base = os.path.join("assets", key)
    candidates = [base + ext for ext in (".jpg", ".png", ".webp")]
    for path in candidates:
        if os.path.exists(path):
            try:
                st.image(Image.open(path), use_container_width=True)
                return
            except Exception:
                pass
    # last resort placeholder
    ph = os.path.join("assets", "placeholder.jpg")
    if os.path.exists(ph):
        try:
            st.image(Image.open(ph), use_container_width=True)
            return
        except Exception:
            pass
    st.info("Image not available yet.")

# ---------------------------
# Grid render (3 per row on desktop, 1–2 on mobile)
# ---------------------------
cols_per_row = 3
for i in range(0, len(filtered), cols_per_row):
    row = filtered[i:i+cols_per_row]
    cols = st.columns(len(row))
    for c, item in zip(cols, row):
        with c:
            st.markdown('<div class="s-card">', unsafe_allow_html=True)
            st.markdown(f"### {item['title']}", unsafe_allow_html=True)
            st.caption(item.get("blurb", ""))
            show_image_for(item["key"])
            with st.expander("Learn more"):
                st.markdown(textwrap.dedent(item["desc"]))
            st.markdown('</div>', unsafe_allow_html=True)

# Footer hint
st.markdown("---")
st.caption(
    "Tip: add or replace images in **assets/** using these exact names: "
    + ", ".join(f"`{k['key']}.jpg`" for k in ITEMS)
)
