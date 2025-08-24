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
    body {
        background-image: url('assets/background.jpg');
        background-size: cover;
        background-attachment: fixed;
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
    </style>
    """,
    unsafe_allow_html=True
)

# --- ITEMS ---
ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "medal", "palms", "thurible",
    "relic", "rosary", "cord", "sacapular",
    "monstrance", "eucharistic_host"
]

# --- DESCRIPTIONS WITH HISTORICAL CONTEXT ---
DESC = {
    "ashes": "Ashes, used on Ash Wednesday, date back to the early Church and Jewish penitential practices. The imposition of ashes recalls mortality and repentance, connecting Christians to ancient Israelite traditions and reminding them of Genesis 3:19.",
    "bible": "The Bible, meaning 'books,' is a library of sacred writings. Catholic editions include the Deuterocanonical books, preserved by the Septuagint. Since the earliest centuries, illuminated manuscripts and later printed Bibles were treasured, forming the foundation of Christian teaching.",
    "blessed_medals": "Blessed medals gained popularity in the early Middle Ages as tokens of faith and protection. The Miraculous Medal originated from St. Catherine Labouré’s visions in 1830, while the St. Benedict Medal dates back at least to the 11th century, inscribed with prayers of exorcism.",
    "blessed_salt": "Blessed salt, known in the Roman Ritual, was used as early as the 3rd century. It recalls Elisha’s purification of water (2 Kings 2:19-22) and symbolizes preservation from corruption and spiritual protection.",
    "blessing": "Blessings are among the oldest sacramentals, rooted in the Jewish practice of berakhot. Early Christian communities blessed homes, fields, and travelers. The Roman Pontifical preserved many such prayers, sanctifying daily life.",
    "candle": "Candles symbolize Christ as the Light of the World. Early Christians used candles in catacombs; by the 4th century, they became standard in liturgy. The Paschal candle, first mentioned in the 5th century, represents the Resurrection.",
    "chaplet": "Chaplets are prayer beads beyond the rosary, dating to medieval confraternities. The Divine Mercy Chaplet, revealed to St. Faustina in the 20th century, shows how these devotions evolve to meet spiritual needs.",
    "crucifix": "The crucifix, with the figure of Christ, emerged in the 6th century and spread widely by the Middle Ages. It confronts the believer with the Passion and remains central to Catholic identity, often blessed for protection.",
    "holy_bells": "Bells were blessed as early as the 8th century, called 'campanae' or 'sacred trumpets.' Their ringing at Mass or in towers was believed to ward off storms and evil, summoning the faithful to prayer.",
    "holy_card": "Holy cards began as woodcuts in the late Middle Ages and became popular devotional items by the 17th century. They often depict saints or events and were used as catechetical tools.",
    "holy_doors": "Holy Doors, opened during Jubilee years, originated in the 15th century at St. Peter’s Basilica. Passing through them symbolizes spiritual renewal and the reception of special indulgences.",
    "holy_images": "Holy images trace to the earliest Christian catacombs. Icons flourished in the East; statues in the West. The Second Council of Nicaea (787) affirmed their veneration, not worship, as windows to the divine.",
    "holy_oil": "Holy oil has Old Testament roots (Exodus 30). Chrism was mentioned by Church Fathers like Tertullian and Hippolytus. Consecrated oils are still used in Baptism, Confirmation, Holy Orders, and the Anointing of the Sick.",
    "holy_water": "Holy water reflects ancient Jewish purification rites and was noted by the 4th century. It is exorcised and blessed, reminding the faithful of Baptism and serving as protection against evil.",
    "incense": "Incense was offered in the Temple of Jerusalem and adopted by Christians by the 4th century. Its smoke symbolizes prayers rising to heaven (Psalm 141:2) and sanctifies the liturgy.",
    "liturgical_vestments": "Vestments evolved from Roman attire. By the 5th century, they became distinct for worship. Colors signify liturgical seasons, and garments like the chasuble and stole symbolize Christ’s yoke and charity.",
    "medal": "Medals as tokens of faith emerged from pilgrim badges and relic medals in the early Middle Ages. They commemorate saints, events, or Marian devotions and often bear protective inscriptions.",
    "palms": "Palms, blessed on Palm Sunday, recall Christ’s entry into Jerusalem. The custom dates back to the 4th century in Jerusalem and spread throughout Christendom as a sign of victory and hope.",
    "thurible": "The thurible or censer holds burning charcoal and incense. Its use mirrors Jewish Temple worship and became a fixed part of Christian liturgy by the 6th century. Its fragrant smoke signifies reverence and prayer.",
    "relic": "Relics have been venerated since the 2nd century, with martyrs’ graves becoming pilgrimage sites. The Council of Trent affirmed their use, and they remain integral to altars and devotions.",
    "rosary": "The rosary’s origins lie in the 12th-13th century, with Dominican promotion by St. Dominic. It unites vocal prayer and meditation on Christ’s life and Mary’s role, a devotion embraced worldwide.",
    "cord": "Cords, like the Cord of St. Joseph or St. Philomena, appeared in the 17th century. Worn around the waist, they symbolize purity, fidelity, and special petitions for protection and grace.",
    "sacapular": "The scapular developed from monastic habits. The Brown Scapular, linked to Our Lady of Mount Carmel in the 13th century, became a sign of Marian devotion and consecration.",
    "monstrance": "Monstrances developed in the 13th century to display the consecrated Host during adoration and processions. Often gilded and radiant, they emphasize Christ’s Real Presence and became common after Corpus Christi was established in 1264.",
    "eucharistic_host": "The Eucharistic Host, unleavened bread, becomes the Body of Christ at the consecration. Reserved for adoration and Communion, the Host has been central since the Last Supper and was solemnly elevated in the Mass by the 12th century."
}

ASSETS_DIR = "assets"

# --- DISPLAY ---
st.title("Catholic Sacramentals Encyclopedia")

cols = st.columns(3)

for idx, item in enumerate(ITEM_KEYS):
    img_path = os.path.join(ASSETS_DIR, f"{item}.jpg")
    with cols[idx % 3]:
        if os.path.exists(img_path):
            st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True, output_format="auto")
        else:
            st.image(os.path.join(ASSETS_DIR, "placeholder.jpg"), caption=item.replace("_", " ").title(), use_container_width=True)
        st.markdown(f"**{DESC.get(item, '')}**")
