import streamlit as st
import os
import base64

st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

ASSETS_DIR = "assets"
PLACEHOLDER = os.path.join(ASSETS_DIR, "placeholder.jpg")
BACKGROUND = os.path.join(ASSETS_DIR, "background.jpg")

def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return ""

# Load background
background_b64 = get_base64_image(BACKGROUND)

if background_b64:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{background_b64}");
                background-size: cover;
                background-attachment: fixed;
            }}
            img {{
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                border-radius: 10px;
            }}
            img:hover {{
                transform: scale(1.05);
                box-shadow: 0px 0px 20px rgba(255, 255, 200, 0.7);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def safe_image_loader(file_name):
    """Returns path to file or placeholder if missing."""
    path = os.path.join(ASSETS_DIR, file_name)
    return path if os.path.exists(path) else PLACEHOLDER

sacramentals = {
    "ashes": "Blessed ashes symbolize repentance and mortality, especially during Ash Wednesday liturgy.",
    "background": "Background image for the app, enhancing the devotional atmosphere.",
    "bible": "The Holy Scriptures, containing the Word of God and central to Christian life and liturgy.",
    "blessed_medals": "Sacred medals blessed by clergy, worn for protection and remembrance of faith.",
    "blessed_salt": "Salt blessed by a priest, used for exorcism, protection, and sacramental purposes.",
    "blessing": "Prayers of blessing invoking God's grace upon people, objects, or events.",
    "candle": "Lit candles symbolize Christ as the Light of the World, faith, and prayers ascending to heaven.",
    "chaplet": "A set of prayers often recited on beads, similar to the rosary but with varying devotions.",
    "crucifix": "A cross with the image of Christ crucified, representing His sacrifice and love.",
    "holy_bells": "Blessed bells rung to signify sacred moments, calling the faithful to prayer.",
    "holy_card": "Small cards with images of saints or sacred scenes, often with prayers printed on them.",
    "holy_doors": "Specially designated church doors that grant indulgences when passed through during pilgrimages.",
    "holy_images": "Sacred images used for devotion, veneration, and catechesis.",
    "holy_oil": "Blessed oils used in sacraments such as Baptism, Confirmation, and Anointing of the Sick.",
    "holy_water": "Water blessed by a priest, a reminder of baptism and a source of protection and blessing.",
    "incense": "Fragrant smoke symbolizing prayers rising to heaven, often used during Mass and benediction.",
    "liturgical_vestments": "Sacred garments worn by clergy during liturgy, representing different seasons and roles.",
    "medal": "Sacred medals like the Miraculous or St. Benedict Medal, worn for grace and protection.",
    "palms": "Palm branches blessed on Palm Sunday, symbolizing Christ's victory and kingship.",
    "pilgrimage_item": "Objects carried or collected during pilgrimages, reminders of sacred journeys.",
    "placeholder": "Generic placeholder image for items without a photo yet.",
    "relic": "Sacred remains or belongings of saints, venerated for their connection to holy lives.",
    "rosary": "Beads used to meditate on the life of Christ and the Blessed Virgin Mary.",
    "sacramentals_of_the_dead": "Items used for the dying or deceased, such as candles, oils, or crucifixes.",
    "sacapular": "Two small pieces of cloth joined by cords, worn over the shoulders as a sign of devotion.",
    "sign_of_the_cross": "Gesture invoking the Trinity, a prayerful action marking blessing and remembrance."
}

st.title("Catholic Sacramentals Encyclopedia")

# Display each item with image and description
for item, description in sacramentals.items():
    img_path = safe_image_loader(f"{item}.jpg")
    st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
    st.markdown(f"**{description}**")
    st.markdown("---")
