import streamlit as st
import os

# Page config
st.set_page_config(
    page_title="Catholic Sacramentals",
    page_icon="✝",
    layout="wide"
)

# Custom CSS for background, header font, hover & glow effects
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');

        body {
            background-image: url("assets/background.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        h1 {
            font-family: 'UnifrakturCook', cursive;
            font-size: 60px;
            text-align: center;
            color: #fdfdfd;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
            margin-bottom: 40px;
        }
        .sacramental-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .sacramental-card:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(255, 255, 200, 0.6);
        }
        .sacramental-caption {
            font-size: 18px;
            color: #f8f8f8;
            text-align: center;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Catholic Sacramentals</h1>", unsafe_allow_html=True)

ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water",
    "incense", "liturgical_vestments", "medal", "palms",
    "relic", "rosary", "scapular", "thurible", "monstrance",
    "cord", "eucharistic_host"
]

DESCRIPTIONS = {
    "ashes": """**Ashes** – Distributed on Ash Wednesday, these are the burned palms from the previous year’s Palm Sunday. They symbolize mortality and penance, tracing back to Old Testament practices and early Christian rituals of repentance.""",
    "bible": """**Bible** – The inspired Word of God, comprising the Old and New Testaments. From handwritten manuscripts to Gutenberg’s press in the 15th century, its reverence as a blessed book makes it central to Christian worship and study.""",
    "blessed_medals": """**Blessed Medals** – Sacramentals like the Miraculous Medal (1830, Rue du Bac, Paris) and St. Benedict Medal (11th century Monte Cassino) are worn for spiritual protection and reminders of faith.""",
    "blessed_salt": """**Blessed Salt** – Mentioned by Church Fathers, blessed salt is used for exorcism, purification, and blessing homes, recalling Elisha purifying water (2 Kings 2:19-22).""",
    "blessing": """**Blessing** – A priestly or episcopal invocation calling on God’s grace. Since apostolic times, blessings consecrate objects, protect people, and sanctify daily life.""",
    "candle": """**Candle** – Candles symbolize Christ, the Light of the World. Their use traces back to the early Church in catacombs and culminates in the Paschal candle lit at Easter Vigil.""",
    "chaplet": """**Chaplet** – Prayer beads distinct from the rosary, such as the Chaplet of Divine Mercy (1930s), used to meditate on Christ’s mercy and intercede for souls.""",
    "crucifix": """**Crucifix** – The cross with the figure of Christ, prominent since the 6th century. It recalls the Passion and remains a central symbol in Catholic devotion and protection.""",
    "holy_bells": """**Holy Bells** – Blessed bells have marked sacred time since the Middle Ages, rung during the Eucharist or to ward off storms and evil.""",
    "holy_card": """**Holy Card** – Small devotional images with prayers, popularized in the 16th century. They honor saints, events, or teachings and serve as portable reminders of faith.""",
    "holy_doors": """**Holy Doors** – Special doors in major basilicas, opened during Jubilee years. Pilgrims passing through receive indulgences, symbolizing grace and renewal.""",
    "holy_images": """**Holy Images** – Icons and statues, blessed and venerated since the early Church, remind the faithful of the communion of saints and inspire prayer.""",
    "holy_oil": """**Holy Oil** – Sacred Chrism, Oil of Catechumens, and Oil of the Sick are consecrated at the Chrism Mass. Used in sacraments like Baptism, Confirmation, Holy Orders, and Anointing of the Sick.""",
    "holy_water": """**Holy Water** – Blessed water, often with salt, used since the early centuries for purification and protection, marking entry into the Church through Baptism.""",
    "incense": """**Incense** – Aromatic resins burned since the Old Testament, symbolizing prayers rising to God (Psalm 141). In the Mass, incense honors the altar, Gospel, people, and Eucharist.""",
    "liturgical_vestments": """**Liturgical Vestments** – Priests and deacons wear blessed garments whose origins lie in Roman attire. Colors follow the liturgical calendar to signify seasons and feasts.""",
    "medal": """**Medal** – Sacred tokens often depicting saints, blessed for protection and remembrance, dating back to early Christian pilgrimages.""",
    "palms": """**Palms** – Blessed branches distributed on Palm Sunday, recalling Christ’s triumphal entry into Jerusalem. Burned later to make ashes, their use dates back to the 4th century.""",
    "relic": """**Relic** – First-class (body), second-class (items), and third-class (touched) relics of saints, venerated since early Christianity, especially after Constantine legalized the faith.""",
    "rosary": """**Rosary** – Prayer beads to meditate on Christ’s life and Mary’s intercession. Developed in the Middle Ages, popularized by St. Dominic and the Dominicans in the 13th century.""",
    "scapular": """**Scapular** – Originating from monastic habits, smaller versions like the Brown Scapular (13th century Carmelite tradition) are worn for Marian devotion and protection.""",
    "thurible": """**Thurible** – A censer suspended by chains to burn incense, widely used since the 4th century. Its use symbolizes sanctification and prayers ascending to heaven.""",
    "monstrance": """**Monstrance** – A radiant vessel displaying the consecrated Eucharist for adoration and benediction. Originated in the medieval period to deepen Eucharistic devotion.""",
    "cord": """**Cord** – Blessed cords or cinctures, often associated with saints like St. Joseph or St. Philomena, worn as a sign of devotion and purity since early Christianity.""",
    "eucharistic_host": """**Eucharistic Host** – The consecrated bread, truly the Body of Christ. Since the Last Supper, the host has been at the heart of Catholic worship and reverence."""
}

cols = st.columns(4)
for idx, item in enumerate(ITEM_KEYS):
    with cols[idx % 4]:
        img_path = os.path.join("assets", f"{item}.jpg")
        try:
            st.markdown("<div class='sacramental-card'>", unsafe_allow_html=True)
            st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
            st.markdown(f"<div class='sacramental-caption'>{DESCRIPTIONS.get(item, '')}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception:
            st.write(f"Image for {item} not found.")
