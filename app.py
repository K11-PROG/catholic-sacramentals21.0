import streamlit as st
import os

st.set_page_config(layout="wide")

# Background CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('assets/background.jpg') no-repeat center center fixed;
        background-size: cover;
    }}
    .sacramental-img {{
        transition: all 0.3s ease-in-out;
        border-radius: 12px;
    }}
    .sacramental-img:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255, 255, 200, 0.6);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Catholic Sacramentals Encyclopedia")

# List of sacramentals
sacramentals = [
    "holy_water", "scapular", "rosary", "medal", "crucifix",
    "blessed_oil", "palm_branch", "candle", "incense",
    "relic", "holy_card", "rosary_ring"
]

# Display images and descriptions
for item in sacramentals:
    img_path = os.path.join("assets", f"{item}.jpg")
    if not os.path.exists(img_path) or os.path.getsize(img_path) == 0:
        img_path = os.path.join("assets", "placeholder.jpg")
    st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
    st.write(f"**{item.replace('_', ' ').title()}**: Detailed and rich historical description coming soon.")
