import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

# Background CSS
background_path = os.path.join("assets", "background.jpg")
st.markdown(
    f'''
    <style>
    .stApp {{
        background-image: url("{background_path}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .hover-effect img {{
        transition: transform 0.3s, box-shadow 0.3s;
    }}
    .hover-effect img:hover {{
        transform: scale(1.05);
        box-shadow: 0px 4px 20px rgba(255, 255, 200, 0.6);
    }}
    </style>
    ''',
    unsafe_allow_html=True
)

# Display sacramentals with hover effect
sacramentals = [
    "holy_water","rosary","crucifix","scapular","medal",
    "holy_card","blessed_salt","candle","incense","oil",
    "bible","prayer_book","chalice","paten","thurible",
    "monstrance","relic","holy_water_font","altar_cloth",
    "holy_bells","sign_of_the_cross","ash","palm","blessing"
]

st.title("Catholic Sacramentals")
cols = st.columns(3)
for idx, item in enumerate(sacramentals):
    img_path = os.path.join("assets", f"{item}.jpg")
    with cols[idx % 3]:
        st.markdown(f"<div class='hover-effect'>", unsafe_allow_html=True)
        st.image(img_path, caption=item.replace("_"," ").title(), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
