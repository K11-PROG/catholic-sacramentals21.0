import streamlit as st
import os

# Page setup
st.set_page_config(
    page_title="Catholic Sacramentals Encyclopedia",
    layout="wide"
)

# CSS for background and hover effect
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

# Updated ITEM_KEYS list
ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "medal", "palms", "thurible",
    "relic", "rosary", "cord", "sacapular",
    "monstrance", "eucharistic_host"
]

# Rich descriptions (keeping old ones, adding new)
DESC = {
    "ashes": "Ashes are traditionally blessed and placed on the faithful’s forehead during Ash Wednesday, marking the start of Lent. They symbolize mortality and penance, recalling the biblical phrase 'Remember that you are dust and to dust you shall return.'",
    "bible": "The Bible is the inspired Word of God, central to Christian life. Catholic editions include the Deuterocanonical books and are often richly illustrated or bound, serving both liturgical and devotional purposes.",
    "blessed_medals": "Blessed medals are sacramentals bearing the image of Christ, the Virgin Mary, or saints. The Miraculous Medal and St. Benedict Medal are especially well known, believed to provide spiritual protection and encouragement in faith.",
    "blessed_salt": "Blessed salt is exorcised and blessed by a priest, often used for protection, purification, and blessing of homes and places.",
    "blessing": "Blessings invoke God’s favor, sanctifying persons, places, or objects. They have ancient biblical roots and are integral to Catholic liturgy and devotion.",
    "candle": "Candles symbolize Christ as the Light of the World. Lit during Mass, sacraments, and devotions, they serve as signs of prayer, offering, and presence.",
    "chaplet": "Chaplets are forms of prayer using beads, often centered on specific devotions like the Divine Mercy Chaplet or St. Michael Chaplet.",
    "crucifix": "The crucifix, depicting Christ on the Cross, is a powerful reminder of the Passion and the redemption of humanity. It is used in homes, churches, and processions.",
    "holy_bells": "Holy bells, blessed for liturgical use, are rung to signify sacred moments such as the Consecration during Mass. They recall biblical uses of bells to summon or signify holiness.",
    "holy_card": "Holy cards depict saints, Christ, or Marian images, often with prayers printed on the reverse. They are devotional aids and keepsakes.",
    "holy_doors": "Holy Doors are ceremonial entrances opened during Jubilee years. Passing through a Holy Door signifies pilgrimage and indulgence in Catholic tradition.",
    "holy_images": "Holy images, whether icons, paintings, or statues, foster devotion and remind the faithful of the heavenly realities and communion of saints.",
    "holy_oil": "Holy oil, consecrated by the bishop, is used in sacraments like Baptism, Confirmation, and Anointing of the Sick. It represents the Holy Spirit’s healing and strengthening grace.",
    "holy_water": "Holy water is blessed and often exorcised, used for blessings, protection, and as a reminder of Baptism. It is placed in fonts in churches and homes.",
    "incense": "Incense, burned during liturgies, symbolizes prayers rising to God and sanctifies spaces. It is used during Mass, Benediction, and other solemn rites.",
    "liturgical_vestments": "Vestments are sacred garments worn by clergy during liturgy, each color signifying seasons and feasts. Their development traces back to Roman attire and centuries of tradition.",
    "medal": "General medals depict saints or events and are blessed to bring spiritual benefits. They are often worn as signs of devotion.",
    "palms": "Palms are blessed on Palm Sunday, commemorating Christ’s triumphal entry into Jerusalem. They are often shaped into crosses and kept in homes.",
    "thurible": "A thurible, also called a censer, is a metal vessel suspended by chains, used to burn incense during liturgical ceremonies. Swinging the thurible spreads fragrant smoke, symbolizing prayers ascending to heaven, and adds solemnity to the Mass and processions.",
    "relic": "Relics are physical objects connected to saints—bones, clothing, or items they used. They are venerated (not worshiped) and placed in altars or reliquaries, linking the faithful with the Communion of Saints.",
    "rosary": "The rosary is a cherished devotion, combining vocal prayers and meditations on the mysteries of Christ and Mary. Beads help track decades of prayers and foster contemplation.",
    "cord": "Cords are sacramentals worn around the waist, often dedicated to a saint (such as St. Joseph or St. Philomena). They symbolize purity, dedication, and protection, sometimes used during times of special prayer or need.",
    "sacapular": "A scapular consists of two small pieces of cloth joined by cords and worn over the shoulders. The Brown Scapular of Our Lady of Mount Carmel is the most famous, signifying Marian devotion and consecration.",
    "monstrance": "A monstrance is an ornate vessel used to display the consecrated Eucharist for adoration. Its design often radiates like the sun, symbolizing Christ as the Light of the World. The faithful pray and worship Christ visibly present in the Blessed Sacrament.",
    "eucharistic_host": "The Eucharistic Host, consecrated bread, becomes the Body of Christ during Mass according to Catholic faith. It is the source and summit of Catholic worship, received in Holy Communion and sometimes reserved for adoration in the tabernacle or displayed in a monstrance."
}

# Assets folder
ASSETS_DIR = "assets"

# Display
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
