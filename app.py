import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

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
        "description": "Holy Water is a fundamental sacramental used throughout Catholic history. Blessed by a priest, it is used to recall Baptism, ward off evil, and bless individuals, homes, and objects. Its roots go back to early Christianity when water was blessed before baptisms and during liturgies. Fonts appeared in churches as early as the 4th century, and holy water continues to be a powerful reminder of purification and divine grace."
    },
    {
        "name": "rosary",
        "title": "Rosary",
        "description": "The Rosary is a centuries-old prayer devotion popularized by St. Dominic in the 13th century and the Dominican Order. It involves meditating on the lives of Jesus and Mary while reciting prayers on beads. The mysteries—Joyful, Sorrowful, Glorious, and Luminous—guide the faithful through salvation history. The Rosary remains one of the most beloved Catholic devotions worldwide."
    },
    {
        "name": "scapular",
        "title": "Scapular",
        "description": "The Brown Scapular, associated with Our Lady of Mount Carmel, originated in the 13th century as part of the Carmelite habit. Worn by laity and clergy, it symbolizes Marian devotion and a commitment to live a Christian life. Tradition holds that wearing the scapular brings spiritual benefits and a reminder of Mary's protection."
    },
    {
        "name": "medal",
        "title": "Religious Medals",
        "description": "Religious medals are tangible signs of faith and devotion. Among the most famous is the Miraculous Medal, revealed to St. Catherine Labouré in 1830. Another is the Saint Benedict Medal, known for its prayers of exorcism and protection. Worn or carried by the faithful, medals act as reminders of saints, virtues, and divine protection."
    },
    {
        "name": "crucifix",
        "title": "Crucifix",
        "description": "The crucifix, featuring the image of Christ crucified, is a profound sign of love and redemption. It has been used since the early Church to recall Christ’s sacrifice on the cross. It is a central symbol in Catholic homes, schools, and churches, often displayed prominently during prayer and liturgical celebrations."
    }
    # Additional sacramentals follow the same pattern with rich descriptions...
]

cols = st.columns(3)
for i, item in enumerate(sacramentals):
    img_path = os.path.join(assets_dir, f"{item['name']}.jpg")
    col = cols[i % 3]
    with col:
        if os.path.exists(img_path):
            col.markdown(f'<div class="sacramental-card"><img src="{img_path}" width="100%"></div>', unsafe_allow_html=True)
        else:
            col.markdown(f'<div class="sacramental-card"><img src="assets/placeholder.jpg" width="100%"></div>', unsafe_allow_html=True)
        col.markdown(f'<div class="sacramental-description"><h4>{item["title"]}</h4><p>{item["description"]}</p></div>', unsafe_allow_html=True)
