import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Catholic Sacramentals Encyclopedia",
    layout="wide",
    page_icon="✝️"
)

# --- CUSTOM CSS (Background + Hover Effect) ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("assets/background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .sacramental-img {
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        border-radius: 12px;
    }
    .sacramental-img:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 0 20px rgba(255, 255, 200, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# --- SACRAMENTALS LIST ---
ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "medal", "palms", "rosary",
    "sacapular", "thurible", "monstrance", "cord", "eucharistic_host", "relic"
]

# --- DESCRIPTIONS (EXTENSIVE, HISTORIC, RICH) ---
DESC = {
    "ashes": """**Ashes** are blessed remains of burned palm branches from the previous year's Palm Sunday, used on Ash Wednesday to mark the faithful with the sign of the cross. This custom dates back to the early Middle Ages, symbolizing penance and mortality, reminding Christians: "Remember that you are dust, and to dust you shall return." """,
    "bible": """**Bible** is the sacred collection of writings comprising the Old and New Testaments. It has been central to Christian worship since the first centuries, translated into thousands of languages, and remains the source of Catholic doctrine, prayer, and study.""",
    "blessed_medals": """**Blessed Medals**, such as the Miraculous Medal or Saint Benedict Medal, are sacramentals that bear holy images or inscriptions. Worn for spiritual protection and devotion, medals became widespread in the early Church and gained formal blessings in the 17th–19th centuries.""",
    "blessed_salt": """**Blessed Salt** is ordinary salt exorcised and blessed by a priest, used for protection against evil and for purification. Mentioned by St. Augustine and rooted in Jewish and Christian ritual, it can be sprinkled in homes or mixed with holy water.""",
    "blessing": """**Blessings** are invocations of God's favor pronounced by clergy or laity. From the earliest centuries, blessings were extended over people, objects, and events, sanctifying daily life and inviting divine grace.""",
    "candle": """**Candles** symbolize Christ, the Light of the World. They appear in every sacramental rite—baptism, funerals, Mass. Beeswax candles were prescribed by medieval liturgical norms; their steady flame represents prayer and divine presence.""",
    "chaplet": """**Chaplets** are devotional prayers counted on beads, often shorter than the rosary. Originating in medieval Europe, chaplets encourage meditation on Christ, Mary, or the saints, adapting prayer to specific needs.""",
    "crucifix": """**Crucifix** displays the body of Christ on the cross, recalling the Passion and salvation. Crucifixes became widespread by the 6th century and are required in Catholic liturgical settings, symbolizing sacrificial love.""",
    "holy_bells": """**Holy Bells** are blessed and sometimes exorcised, used to call the faithful and ward off evil. Bell blessing rituals date to the early Middle Ages; their sound was believed to sanctify the air and announce sacred action.""",
    "holy_card": """**Holy Cards** are small devotional pictures, often with prayers. They emerged in 16th-century Europe and remain a popular way to share images of saints, scripture, or devotions.""",
    "holy_doors": """**Holy Doors** are sealed doors in major basilicas opened during Jubilee Years. Crossing them symbolizes pilgrimage and spiritual renewal, a tradition confirmed since the 15th century by papal decree.""",
    "holy_images": """**Holy Images** include icons, paintings, and statues, aiding devotion and contemplation. Defended by the Second Council of Nicaea (787), they teach and inspire, pointing to the realities they depict.""",
    "holy_oil": """**Holy Oils** (chrism, catechumens, infirm) are consecrated at the Chrism Mass and used in sacraments. The use of oil in anointing dates to the Old Testament and the early Church, signifying healing and sanctification.""",
    "holy_water": """**Holy Water** is water blessed by a priest, recalling baptism and used for blessing persons, places, and things. The practice is ancient, rooted in Jewish ritual washings and the earliest Christian baptisms.""",
    "incense": """**Incense** is fragrant resin burned in liturgy to honor God and signify prayers rising to heaven. Mentioned in scripture and used since apostolic times, its solemn use enriches Mass and Benediction.""",
    "liturgical_vestments": """**Liturgical Vestments** are garments worn by clergy during services, evolving from Roman dress. Each vestment carries symbolism, and colors follow the liturgical calendar to reflect seasons of penance, joy, or solemnity.""",
    "medal": """**Medal** is a broader category for devotional tokens bearing saints or sacred images, often carried or worn. Medals became popular devotional aids in medieval Christianity.""",
    "palms": """**Palms** are blessed branches distributed on Palm Sunday, commemorating Christ’s triumphal entry into Jerusalem. They are later burned to make ashes
