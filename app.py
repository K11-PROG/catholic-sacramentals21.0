import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# Background
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('assets/stained_glass.jpg');
        background-size: cover;
        background-attachment: fixed;
    }}
    .sacramental-card {{
        background: rgba(255, 255, 255, 0.7);
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✝️ Catholic Sacramentals Encyclopedia")

sacramentals = [
    "holy_water", "rosary", "scapular", "medal", "crucifix", "blessed_salt",
    "palm_branch", "ash", "candle", "incense", "holy_oil", "prayer_card",
    "statue", "icon", "chaplet", "holy_card", "religious_book", "veil",
    "rosary_ring", "medallion", "devotional_image", "st_benedict_medal",
    "agnus_dei", "blessed_bells"
]

descriptions = {name: f"Description for {name.replace('_',' ').title()}." for name in sacramentals}

for name in sacramentals:
    img_path = os.path.join("assets", f"{name}.jpg")
    if not os.path.exists(img_path):
        img_path = os.path.join("assets", "placeholder.jpg")
    with st.container():
        st.markdown(f"<div class='sacramental-card'><h3>{name.replace('_',' ').title()}</h3></div>", unsafe_allow_html=True)
        st.image(img_path, use_container_width=True)
        st.write(descriptions[name])
