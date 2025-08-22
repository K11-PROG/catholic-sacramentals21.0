import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

# Background style
st.markdown(
    '''
    <style>
    .stApp {{
        background-image: url('assets/stained_glass_bg.jpg');
        background-size: cover;
        background-attachment: fixed;
    }}
    .sacramental-card img:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
        transition: all 0.3s ease-in-out;
    }}
    </style>
    ''',
    unsafe_allow_html=True
)

st.title("Catholic Sacramentals Encyclopedia")

# Load sacramentals
sacramentals = [
    ("holy_water", "Holy Water", "Blessed water used in sacramental rites since early Christianity."),
    ("rosary", "Rosary", "Prayer beads developed around the 13th century for meditative prayer."),
    ("scapular", "Scapular", "Worn garment symbolizing devotion, originating in monastic traditions."),
    ("medal", "Medal", "Blessed devotional medals representing saints and Marian apparitions."),
    ("crucifix", "Crucifix", "A cross bearing the image of Christ, widely used in worship."),
    ("relic", "Relic", "Physical remains or personal effects of saints, venerated for holiness."),
    ("blessed_salt", "Blessed Salt", "Salt blessed by a priest, used for protection and blessing.")
]

# Display cards
cols = st.columns(3)
for idx, (file, name, desc) in enumerate(sacramentals):
    with cols[idx % 3]:
        img_path = os.path.join("assets", f"{file}.jpg")
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.image("assets/placeholder.jpg", use_container_width=True)
        st.subheader(name)
        st.write(desc)
