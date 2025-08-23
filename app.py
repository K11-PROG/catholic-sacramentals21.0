import streamlit as st
import os

# App config
st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# Custom CSS for hover glow and background
st.markdown(
    """
    <style>
    body {
        background-image: url('assets/stained_glass.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    .sacramental-card img {
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        border-radius: 12px;
    }
    .sacramental-card img:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 20px rgba(255, 255, 200, 0.7);
    }

    .sacramental-description {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1em;
        border-radius: 12px;
        margin-top: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Catholic Sacramentals Encyclopedia")

assets_dir = "assets"

sacramentals = [
    {
        "name": "holy_water",
        "title": "Holy Water",
        "description": "Holy Water has been a sacramental since the earliest centuries. Blessed by a priest, it is used for protection, purification, and as a reminder of baptism. Fonts were common in churches by the 4th century."
    },
    {
        "name": "rosary",
        "title": "Rosary",
        "description": "The Rosary, popularized by the Dominicans in the 13th century, is a meditative prayer tool reflecting on the lives of Jesus and Mary through beads and prayers."
    },
    {
        "name": "scapular",
        "title": "Scapular",
        "description": "Originating with the Carmelites in the 13th century, the scapular is a small cloth worn as a sign of devotion and protection, symbolizing Marian dedication."
    },
    {
        "name": "medal",
        "title": "Religious Medals",
        "description": "Sacramental medals, such as the Miraculous Medal (1830) and Saint Benedict Medal, carry blessings and symbols of faith and protection."
    },
    {
        "name": "crucifix",
        "title": "Crucifix",
        "description": "The crucifix, a cross bearing the image of Christ, has been venerated since early Christianity. It reminds the faithful of Christ's sacrifice and triumph over death."
    },
    {
        "name": "blessed_salt",
        "title": "Blessed Salt",
        "description": "Blessed salt, often used with holy water, has biblical roots and symbolizes preservation and purification. It is used in blessings and protection against evil."
    },
    {
        "name": "palm",
        "title": "Blessed Palms",
        "description": "Palm branches, blessed on Palm Sunday, commemorate Christ’s triumphal entry into Jerusalem. They are often kept in homes as a sign of victory and faith."
    },
    {
        "name": "ash",
        "title": "Blessed Ashes",
        "description": "Ashes blessed and imposed on Ash Wednesday remind the faithful of mortality and repentance. This practice dates to the early centuries of Christianity."
    },
    {
        "name": "oil",
        "title": "Blessed Oil",
        "description": "Blessed or holy oils are used for anointing the sick, catechumens, and during confirmations and ordinations. They signify healing, strength, and consecration."
    },
    {
        "name": "blessed_candles",
        "title": "Blessed Candles",
        "description": "Candles blessed at Candlemas and other times symbolize Christ as the Light of the World and are often lit during prayers, sacraments, and blessings."
    },
    {
        "name": "chaplet",
        "title": "Chaplets",
        "description": "Chaplets are similar to rosaries but focus on specific devotions, like the Divine Mercy Chaplet. They guide prayer and meditation on particular mysteries or saints."
    },
    {
        "name": "prayer_card",
        "title": "Prayer Cards",
        "description": "Prayer cards contain sacred images and prayers. They have been a devotional aid since the 16th century, helping the faithful remember prayers and saints."
    },
    {
        "name": "rosary_ring",
        "title": "Rosary Ring",
        "description": "A compact version of the rosary, often worn as a ring or carried discreetly, for prayer on the go."
    },
    {
        "name": "relic",
        "title": "Sacred Relics",
        "description": "Relics, categorized as first, second, or third class, are objects associated with saints and martyrs. They have been venerated since the early Church as tangible connections to holiness."
    },
    {
        "name": "holy_card",
        "title": "Holy Cards",
        "description": "Holy cards combine art and devotion, typically with a saint or prayer. They became popular in Europe during the Renaissance and remain devotional keepsakes."
    },
    {
        "name": "medallion",
        "title": "Medallions",
        "description": "Medallions often commemorate a sacrament or pilgrimage. They carry prayers or images and are worn or kept as devotional items."
    },
    {
        "name": "prayer_book",
        "title": "Prayer Books",
        "description": "Prayer books compile prayers, devotions, and instructions for worship. They have existed since the medieval period and help guide daily prayer life."
    },
    {
        "name": "holy_card_folder",
        "title": "Holy Card Folders",
        "description": "Folders or albums store multiple prayer cards and holy images, preserving devotional items and memories of faith."
    },
    {
        "name": "thurible",
        "title": "Thurible (Censer)",
        "description": "Used to burn incense during liturgy, the thurible represents prayers rising to God. Incense use dates back to Jewish Temple worship and early Christian liturgy."
    },
    {
        "name": "blessing",
        "title": "Priestly Blessings",
        "description": "Blessings impart grace and protection. They range from simple signs of the cross to solemn benedictions, continuing the apostolic practice."
    },
    {
        "name": "holy_picture",
        "title": "Sacred Images",
        "description": "Sacred pictures or icons inspire prayer and meditation. Veneration of images has been part of Catholic tradition since the early centuries, affirmed at the Second Council of Nicaea (787)."
    },
    {
        "name": "book_of_gospels",
        "title": "Book of the Gospels",
        "description": "A liturgical book containing the Gospel readings, honored during Mass and processions. Its reverence highlights the Word of God."
    },
    {
        "name": "altar_bells",
        "title": "Altar Bells",
        "description": "Bells rung during Mass alert the faithful to the consecration, emphasizing the sacred moment. Their use became common in medieval Europe."
    },
    {
        "name": "processional_cross",
        "title": "Processional Cross",
        "description": "Carried at the head of liturgical processions, it symbolizes Christ leading His Church. A tradition rooted in early Christian worship."
    }
]

cols = st.columns(3)
for i, item in enumerate(sacramentals):
    img_path = os.path.join(assets_dir, f"{item['name']}.jpg")
    col = cols[i % 3]

    with col:
        if os.path.exists(img_path):
            col.markdown(
                f'<div class="sacramental-card"><img src="{img_path}" width="100%"></div>',
                unsafe_allow_html=True
            )
        else:
            col.markdown(
                f'<div class="sacramental-card"><img src="assets/placeholder.jpg" width="100%"></div>',
                unsafe_allow_html=True
            )

        col.markdown(
            f"""
            <div class="sacramental-description">
                <h4>{item['title']}</h4>
                <p>{item['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
