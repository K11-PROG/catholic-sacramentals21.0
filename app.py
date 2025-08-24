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

# Encode background if present
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
            .sacramental-img {{
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                border-radius: 10px;
            }}
            .sacramental-img:hover {{
                transform: scale(1.05);
                box-shadow: 0px 0px 20px rgba(255, 255, 200, 0.7);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def safe_image_loader(file_name):
    path = os.path.join(ASSETS_DIR, file_name)
    return path if os.path.exists(path) else PLACEHOLDER

sacramentals = {
    "rosary": "A string of beads used for prayer, symbolizing devotion to Mary and meditation on Christ's life.",
    "scapular": "Two small pieces of cloth worn over the shoulders, symbolizing commitment to the faith and Marian protection.",
    "holy_water": "Water blessed by a priest, used for blessings, protection, and remembrance of baptism.",
    "medal": "Sacred medals like the Miraculous Medal or St. Benedict Medal, worn for grace and protection.",
    "crucifix": "A cross with the figure of Christ crucified, reminding the faithful of His sacrifice and love.",
    "relic": "Physical remains or items associated with saints, revered for their connection to holy lives.",
    "candle": "Lit candles represent prayers rising to God, faith, and Christ as the Light of the World.",
    "incense": "Fragrant smoke symbolizing prayers ascending to heaven and purification during worship."
}

st.title("Catholic Sacramentals Encyclopedia")

for item, description in sacramentals.items():
    img_path = safe_image_loader(f"{item}.jpg")
    st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
    st.markdown(f"**{description}**")
    st.markdown("---")
