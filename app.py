import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# --- STYLES ---
st.markdown(
    """
    <style>
    body {
        background-image: url('assets/stained_glass_bg.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .sacramental-image {
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .sacramental-image:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(255, 255, 255, 0.6);
    }
    .sacramental-card {
        background-color: rgba(255,255,255,0.85);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- DATA ---
sacramentals = [
    {
        "name": "holy_water",
        "description": """Holy water is water blessed by a priest used for blessings, protection, and purification.
        Its earliest recorded use dates to the early Christian centuries, modeled after Jewish purification rituals.""",
        "img": "assets/holy_water.jpg"
    },
    {
        "name": "rosary",
        "description": """The rosary is a set of prayer beads used for meditative prayer focusing on Christ’s life.
        Popularized in the Middle Ages, it remains a core Marian devotion.""",
        "img": "assets/rosary.jpg"
    },
    {
        "name": "scapular",
        "description": """The brown scapular of Our Lady of Mount Carmel emerged in the 13th century as a sign of devotion and protection.
        Other scapulars developed over time as sacramentals of commitment.""",
        "img": "assets/scapular.jpg"
    },
    {
        "name": "crucifix",
        "description": """The crucifix displays the image of Christ on the cross, used in homes, churches, and personal devotion.
        It recalls the Passion and is an outward sign of Christian faith.""",
        "img": "assets/crucifix.jpg"
    },
    {
        "name": "medal",
        "description": """Medals, such as the Miraculous Medal or St. Benedict Medal, often bear sacred images and inscriptions for protection and remembrance.
        Their roots go back to the early Christian symbols worn discreetly.""",
        "img": "assets/medal.jpg"
    },
    {
        "name": "palms",
        "description": """Blessed palms from Palm Sunday commemorate Christ’s triumphal entry into Jerusalem.
        Traditionally kept in homes as a sign of blessing and protection.""",
        "img": "assets/palms.jpg"
    },
    {
        "name": "ash",
        "description": """Ashes used on Ash Wednesday mark repentance and mortality.
        The custom dates back to ancient penance practices.""",
        "img": "assets/ash.jpg"
    },
    {
        "name": "incense",
        "description": """Incense symbolizes prayers rising to God.
        Used since ancient Jewish worship and in Christian liturgy since the earliest centuries.""",
        "img": "assets/incense.jpg"
    },
    {
        "name": "blessed_salt",
        "description": """Blessed salt is used in exorcisms, blessings, and protection.
        Its symbolism of purification and preservation dates to biblical times.""",
        "img": "assets/blessed_salt.jpg"
    },
    {
        "name": "holy_oil",
        "description": """Holy oils (chrism, oil of catechumens, oil of the sick) are blessed annually and used in sacraments and blessings.
        Anointed use traces to Old Testament and apostolic practice.""",
        "img": "assets/holy_oil.jpg"
    },
    {
        "name": "candle",
        "description": """Blessed candles symbolize Christ as Light of the World.
        Candles are blessed on Candlemas and used for prayer, processions, and protection.""",
        "img": "assets/candle.jpg"
    },
    {
        "name": "chaplet",
        "description": """Chaplets are prayer beads distinct from the rosary, often dedicated to particular devotions like Divine Mercy.
        They developed in various forms across Christian spirituality.""",
        "img": "assets/chaplet.jpg"
    },
    {
        "name": "prayer_card",
        "description": """Prayer cards depict saints or prayers, encouraging devotion and remembrance.
        They became popular in the 19th century with advances in printing.""",
        "img": "assets/prayer_card.jpg"
    },
    {
        "name": "holy_card",
        "description": """Similar to prayer cards, these small images often bear relics or devotional texts.""",
        "img": "assets/holy_card.jpg"
    },
    {
        "name": "book_of_blessings",
        "description": """Books containing prayers and blessings for various occasions.
        Essential in parish and household devotion.""",
        "img": "assets/book_of_blessings.jpg"
    },
    {
        "name": "religious_statue",
        "description": """Statues of Christ, Mary, and saints inspire prayer and contemplation.
        Used since early Christianity to honor sacred figures.""",
        "img": "assets/religious_statue.jpg"
    },
    {
        "name": "holy_relic",
        "description": """Relics are physical remains or items associated with saints.
        Veneration dates to the earliest martyrs and reflects the communion of saints.""",
        "img": "assets/holy_relic.jpg"
    },
    {
        "name": "altar_bread",
        "description": """Unconsecrated hosts used at Mass.
        Though not the Eucharist until consecration, their preparation is reverent.""",
        "img": "assets/altar_bread.jpg"
    },
    {
        "name": "vestment",
        "description": """Liturgical vestments symbolize the dignity of sacred ministry.
        Their colors and forms reflect the Church calendar.""",
        "img": "assets/vestment.jpg"
    },
    {
        "name": "thurible",
        "description": """A censer used for burning incense during worship.
        Its use is ancient and highly symbolic.""",
        "img": "assets/thurible.jpg"
    },
    {
        "name": "aspergillum",
        "description": """Instrument used to sprinkle holy water.
        It reminds of baptism and cleansing.""",
        "img": "assets/aspergillum.jpg"
    },
    {
        "name": "pyx",
        "description": """A small container used to carry the Eucharist to the sick or absent.
        Revered as a sacred vessel.""",
        "img": "assets/pyx.jpg"
    },
    {
        "name": "monstrance",
        "description": """A vessel used to display the consecrated host for adoration.
        Developed in medieval Europe for Eucharistic devotion.""",
        "img": "assets/monstrance.jpg"
    },
    {
        "name": "blessed_crucifix",
        "description": """A crucifix blessed for protection and devotion in the home.
        Represents Christ’s sacrifice and victory over sin.""",
        "img": "assets/blessed_crucifix.jpg"
    }
]

# --- CONTENT ---
st.title("Catholic Sacramentals Encyclopedia")

for item in sacramentals:
    img_path = item["img"]
    st.markdown(f"### {item['name'].replace('_', ' ').title()}")
    st.markdown(f"<div class='sacramental-card'><p>{item['description']}</p></div>", unsafe_allow_html=True)
    if os.path.exists(img_path):
        st.markdown(
            f"<img src='{img_path}' class='sacramental-image' width='300'>",
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Image for {item['name']} not found in assets folder.")
