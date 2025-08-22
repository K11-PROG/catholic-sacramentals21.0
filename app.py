import streamlit as st
from PIL import Image
import os
import base64

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_path = "assets/background.jpg"
if os.path.exists(bg_path):
    bg_base64 = get_base64_of_bin_file(bg_path)
    bg_style = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

st.title("Catholic Sacramentals Encyclopedia")

sacramentals = [
    "holy_water_bottle",
    "rosary",
    "scapular",
    "medal",
    "crucifix",
    "holy_card",
    "blessed_salt",
    "oil_of_the_sick",
    "palm_branch",
    "ash_cross",
    "holy_chalice",
    "thurible",
    "holy_water_font",
    "candle",
    "incense",
    "bible",
    "rosary_ring",
    "chaplet",
    "cord",
    "blessed_bells",
    "holy_door",
    "monstrance",
    "eucharistic_host",
    "holy_relic",
]

assets_path = "assets"

for item in sacramentals:
    img_path = os.path.join(assets_path, f"{item}.jpg")
    if os.path.exists(img_path):
        try:
            img = Image.open(img_path)
            st.image(img, caption=item.replace("_", " ").title(), use_container_width=True)
        except Exception as e:
            st.warning(f"Problem loading {item}: {e}")
    else:
        st.image(os.path.join(assets_path, "placeholder.jpg"), caption=f"{item} (placeholder)", use_container_width=True)
