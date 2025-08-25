import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide", page_icon="✝️")

# CSS for background, hover effects, and ornamental heading
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

.stApp {
    background-image: url("assets/background.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #fff;
}

.sacramental-img {
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    border-radius: 12px;
}
.sacramental-img:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 0 20px rgba(255, 255, 200, 0.6);
}

h1.cursive-title {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    font-size: 4em;
    margin-top: 10px;
    margin-bottom: 30px;
    color: #fff;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='cursive-title'>Catholic Sacramentals</h1>", unsafe_allow_html=True)

ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "medal", "palms", "rosary",
    "sacapular", "thurible", "monstrance", "cord", "eucharistic_host", "relic"
]

DESC = {
    "ashes": """**Ashes**: Blessed ashes, usually from burnt palms, symbolize repentance and mortality. They are used on Ash Wednesday, reminding the faithful of life’s fragility and the call to conversion, a tradition dating back to the 10th century.""",
    "bible": """**Bible**: The Holy Scriptures are central to Christian life. As a sacramental, a blessed Bible encourages reverence for God’s Word, tracing its written forms back to the early Church and monastic scriptoria.""",
    "blessed_medals": """**Blessed Medals**: Sacred medals bearing images of Christ, Mary, or saints. Common examples include the Miraculous Medal (1830) and St. Benedict Medal. They serve as reminders of faith and intercession.""",
    "blessed_salt": """**Blessed Salt**: Used in blessings and exorcisms, this ancient sacramental recalls salt’s biblical symbolism of purity and preservation. It has roots in Old Testament ritual and early Christian practice.""",
    "blessing": """**Blessings**: Spoken or written invocations asking God’s favor. Priests bless objects, people, and events, extending the Church’s prayerful protection. Blessings are among the oldest sacramentals, recorded in Scripture.""",
    "candle": """**Candle**: Blessed candles represent Christ the Light. Key moments include Candlemas (Feast of the Presentation, 4th century). They accompany prayers, processions, and sacraments.""",
    "chaplet": """**Chaplet**: A smaller string of beads or prayers. Variants include the Divine Mercy Chaplet (20th century). Chaplets echo the rosary’s meditative rhythm, focusing on particular devotions.""",
    "crucifix": """**Crucifix**: A cross bearing the image of Christ crucified. Essential in Catholic homes and churches since the early centuries, reminding of Christ’s sacrifice and love.""",
    "holy_bells": """**Holy Bells**: Blessed bells call the faithful to worship and sanctify spaces. Historically, bells were blessed to ward off storms and evil, with documented rites from the 8th century.""",
    "holy_card": """**Holy Card**: Small devotional cards depicting sacred images or prayers. These originated in 16th-century Europe as popular aids for prayer and remembrance.""",
    "holy_doors": """**Holy Doors**: Specially designated doors opened during Jubilees (since 1300), symbolizing pilgrimage and the grace of entering God’s mercy.""",
    "holy_images": """**Holy Images**: Sacred art, icons, and statues encourage prayer and teaching. Veneration of images was defended at the Second Council of Nicaea (787).""",
    "holy_oil": """**Holy Oil**: Oils blessed for sacraments and blessings, including Chrism, Catechumen, and Oil of the Sick. Used since apostolic times to anoint and strengthen the faithful.""",
    "holy_water": """**Holy Water**: Blessed water for blessing people and places. Early Christians adopted the Jewish use of ritual water, now found in fonts at every church entrance.""",
    "incense": """**Incense**: Aromatic resin burned in worship, symbolizing prayers rising to God. Its use dates back to the Temple in Jerusalem and is prominent in Christian liturgies.""",
    "liturgical_vestments": """**Liturgical Vestments**: Special garments worn in worship, evolving from ancient Roman dress. They symbolize service and reverence in liturgy.""",
    "medal": """**Medal**: Blessed tokens of faith, commemorating saints or events. Their widespread use began in the Middle Ages, deepening personal devotion.""",
    "palms": """**Palms**: Blessed branches from Palm Sunday, recalling Christ’s entry into Jerusalem. Kept in homes and later burned for ashes used on Ash Wednesday.""",
    "rosary": """**Rosary**: A string of beads for meditative prayer. Tradition credits St. Dominic (13th century), though prayer beads existed earlier. A central Marian devotion.""",
    "sacapular": """**Scapular**: A devotional garment or smaller badge, signifying dedication to Mary or a saint. The Carmelite scapular (13th century) is especially well-known.""",
    "thurible": """**Thurible**: A metal censer swung during liturgy to burn incense. Used since the early Church, derived from temple worship.""",
    "monstrance": """**Monstrance**: A vessel to display the Eucharist for adoration. Evolved in the Middle Ages to encourage devotion to the Blessed Sacrament.""",
    "cord": """**Cord**: A blessed rope or band, often linked to a confraternity or saint. Used as a sign of devotion or protection.""",
    "eucharistic_host": """**Eucharistic Host**: The consecrated bread, truly the Body of Christ. Revered at Mass and in adoration, the summit of Catholic worship.""",
    "relic": """**Relic**: Physical remains or items linked to saints or holy events. Veneration dates to the early Church, affirming the holiness of God’s friends."""
}

for key in ITEM_KEYS:
    img_path = os.path.join("assets", f"{key}.jpg")
    caption = key.replace("_", " ").title()
    desc = DESC.get(key, "")
    try:
        if os.path.exists(img_path):
            st.image(img_path, caption=caption, use_container_width=True, output_format="auto")
        else:
            st.image(os.path.join("assets", "placeholder.jpg"), caption=caption, use_container_width=True)
        st.markdown(desc)
    except:
        st.image(os.path.join("assets", "placeholder.jpg"), caption=caption, use_container_width=True)
        st.markdown(desc)
