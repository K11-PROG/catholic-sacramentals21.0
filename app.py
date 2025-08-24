import streamlit as st
from PIL import Image
import os

# Paths
ASSETS_DIR = "assets"
BACKGROUND = os.path.join(ASSETS_DIR, "background.jpg")
PLACEHOLDER = os.path.join(ASSETS_DIR, "placeholder.jpg")

# CSS for background and hover glow
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{BACKGROUND}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .sacramental-img {{
        transition: all 0.3s ease;
        border-radius: 12px;
    }}
    .sacramental-img:hover {{
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.5);
    }}
    </style>
""", unsafe_allow_html=True)

# Sacramentals list
sacramentals = [
    "holy_water",
    "rosary",
    "scapular",
    "medal",
    "crucifix",
    "palms",
    "blessed_salt",
    "holy_oil",
    "incense",
    "candle",
    "sign_of_the_cross",
    "blessing",
    "chaplet",
    "bible",
    "holy_card",
    "sacramentals_of_the_dead",
    "pilgrimage_item",
    "holy_bells",
    "holy_images",
    "liturgical_vestments",
    "holy_doors",
    "ashes",
    "blessed_medals",
    "relic"
]

def safe_image_load(path):
    """Return a safe image path or fallback."""
    if os.path.exists(path):
        try:
            Image.open(path)  # validate image
            return path
        except:
            return PLACEHOLDER
    else:
        return PLACEHOLDER

st.title("Catholic Sacramentals Encyclopedia")

# Loop through sacramentals
for item in sacramentals:
    img_path = os.path.join(ASSETS_DIR, f"{item}.jpg")
    safe_path = safe_image_load(img_path)
    st.markdown(
        f'<img src="{safe_path}" class="sacramental-img" width="100%">',
        unsafe_allow_html=True
    )
    st.write(f"### {item.replace('_', ' ').title()}")
    st.write("Extensive description here. Replace with real content.")
