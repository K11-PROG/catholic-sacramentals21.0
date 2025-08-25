import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Catholic Sacramentals Encyclopedia",
    layout="wide"
)

# --- STYLES ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');

    body {
        background-image: url('assets/background.jpg');
        background-size: cover;
        background-attachment: fixed;
    }
    h1 {
        font-family: 'UnifrakturCook', cursive;
        font-size: 60px;
        color: #fdfdfd;
        text-align: center;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.8);
        margin-bottom: 40px;
    }
    .sacramental-img {
        transition: all 0.3s ease;
        border-radius: 10px;
        box-shadow: 0 0 0 rgba(0,0,0,0);
    }
    .sacramental-img:hover {
        transform: translateY(-6px);
        box-shadow: 0 8px 20px rgba(255, 255, 200, 0.7);
    }
    .sacramental-desc {
        color: #fff;
        background: rgba(0,0,0,0.4);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 30px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ITEMS ---
ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water",
    "incense", "liturgical_vestments", "medal", "palms",
    "thurible", "relic", "rosary", "cord", "sacapular",
    "monstrance", "eucharistic_host"
]

# --- DESCRIPTIONS (historical and detailed) ---
DESC = {
    "ashes": """Ashes, used on Ash Wednesday, mark the start of Lent. They date back to the earliest Christian centuries and reflect older Jewish penitential rites. Burned from the previous year’s palms, they remind the faithful of mortality and repentance: "Remember that you are dust and to dust you shall return." """,
    "bible": """The Bible, meaning 'books,' is the inspired Word of God. Catholic editions include the Deuterocanonical books. From hand-copied manuscripts of monks to the printing revolution, the Bible has been preserved, illuminated, and venerated as the foundation of Christian belief and liturgy.""",
    "blessed_medals": """Blessed medals are sacred tokens depicting Christ, Mary, or saints. The Miraculous Medal (1830, Rue du Bac, Paris) and St. Benedict Medal (11th century) are prominent examples, worn as reminders of faith and shields of spiritual protection.""",
    "blessed_salt": """Blessed salt, noted in the Roman Ritual, has been used since at least the 3rd century. It recalls biblical events like Elisha purifying water and serves as a sign of preservation and protection, sprinkled in homes, fields, or during exorcisms.""",
    "blessing": """Blessings sanctify people, places, and objects. Rooted in Jewish prayers (berakhot), Christian blessings date to apostolic times and were codified in texts like the Roman Pontifical, calling down God’s grace in daily life and worship.""",
    "candle": """Candles, symbolizing Christ as Light, were used by early Christians in catacombs. By the 4th century they became essential in liturgy. The Paschal candle, lit at Easter Vigil, represents the risen Christ. Candles accompany sacraments, processions, and private devotion.""",
    "chaplet": """Chaplets are prayer beads beyond the rosary, often focused on specific devotions. Medieval confraternities popularized them, and the Divine Mercy Chaplet (20th century) revealed to St. Faustina continues this tradition of meditative, repetitive prayer.""",
    "crucifix": """The crucifix, depicting Christ crucified, emerged by the 6th century. It confronts the believer with the Passion and redemption. Crucifixes are blessed for homes, altars, and personal devotion, embodying the core mystery of salvation.""",
    "holy_bells": """Bells were first blessed in the 8th century. Known as 'sacred trumpets,' they marked sacred time and were believed to drive away storms and evil. Church bells, tower bells, and sanctuary bells announce prayer and liturgy.""",
    "holy_card": """Holy cards, devotional prints often with saintly images and prayers, appeared as woodcuts in the 15th century and flourished in the 17th-19th centuries. They teach, inspire, and serve as portable reminders of faith.""",
    "holy_doors": """Holy Doors, ceremonial entrances in basilicas, were instituted in the 15th century. Opened only during Jubilee years, they symbolize grace and new beginnings; crossing them grants indulgences and renewal.""",
    "holy_images": """Holy images, icons, and statues trace to early Christian catacombs. The Second Council of Nicaea (787) defended their veneration as aids to devotion, not worship. They make visible the invisible realities of faith.""",
    "holy_oil": """Holy oils are consecrated annually by bishops. Chrism, Oil of Catechumens, and Oil of the Sick are mentioned by early Fathers. They anoint in sacraments, signify the Spirit, heal the sick, and strengthen the baptized and ordained.""",
    "holy_water": """Holy water, blessed and exorcised, reminds Christians of Baptism and cleanses spiritually. Mentioned in the 4th century, it is used to bless persons, homes, and wards off evil.""",
    "incense": """Incense, a mixture of resins, has been part of worship since the Temple of Jerusalem. By the 4th century, it adorned Christian liturgy. Its rising smoke symbolizes prayer and reverence, sanctifying sacred spaces.""",
    "liturgical_vestments": """Liturgical vestments developed from Roman civil dress. By the 5th century they were distinct to worship. The chasuble, alb, and stole bear ancient symbolism, and colors mark liturgical seasons and feasts.""",
    "medal": """Medals commemorate saints, events, or Marian devotions. Rooted in pilgrim tokens of the Middle Ages, they are blessed for spiritual benefit and carried or worn as expressions of faith.""",
    "palms": """Palms, blessed on Palm Sunday, recall Christ’s triumphal entry. From the 4th century, Christians carried branches in Jerusalem. Palms are later burned to ashes, connecting Holy Week to Lent.""",
    "thurible": """The thurible, or censer, burns incense on charcoal. Swinging it spreads fragrant smoke, signifying prayers rising. Used since the 6th century, it solemnizes Mass, Benediction, and processions.""",
    "relic": """Relics—remains or belongings of saints—have been honored since the 2nd century. Martyrs’ tombs were early altars. The Council of Trent reaffirmed relic veneration, linking the faithful with the communion of saints.""",
    "rosary": """The rosary, beads to meditate on Christ and Mary, took shape in the Middle Ages, promoted by St. Dominic. The mysteries guide prayer through the life of Christ, embraced by millions worldwide.""",
    "cord": """Cords, blessed ropes worn at the waist, are associated with saints like Joseph and Philomena. Dating to the 17th century, they symbolize purity, consecration, and are used for petitions and healing.""",
    "sacapular": """The scapular, from monastic habits, became a small devotional garment. The Brown Scapular, tied to the Carmelites in the 13th century, expresses Marian protection and dedication.""",
    "monstrance": """Monstrances, from the 13th century, display the consecrated Host. Gilded and radiant, they emphasize Christ’s Real Presence and are used in adoration and processions, especially after Corpus Christi’s institution.""",
    "eucharistic_host": """The Eucharistic Host, unleavened bread consecrated in the Mass, becomes the Body of Christ. From the Last Supper to medieval elevation rites, it is the summit of worship, adored and received as Christ Himself."""
}

ASSETS_DIR = "assets"

# --- DISPLAY ---
st.markdown("<h1>Catholic Sacramentals Encyclopedia</h1>", unsafe_allow_html=True)

cols = st.columns(3)

for idx, item in enumerate(ITEM_KEYS):
    img_path = os.path.join(ASSETS_DIR, f"{item}.jpg")
    with cols[idx % 3]:
        if os.path.exists(img_path):
            st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True, output_format="auto")
        else:
            st.image(os.path.join(ASSETS_DIR, "placeholder.jpg"), caption=item.replace("_", " ").title(), use_container_width=True)
        st.markdown(f"<div class='sacramental-desc'>{DESC.get(item, '')}</div>", unsafe_allow_html=True)
