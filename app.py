
import streamlit as st
import base64

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f'''
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{b64}") no-repeat center center fixed;
            background-size: cover;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.55); /* faded overlay */
            z-index: -1;
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

set_bg("assets/stained_glass_bg.jpg")

st.title("📖 Catholic Sacramentals Encyclopedia")
st.write("Welcome! Browse sacramentals and their explanations.")

# Example item with placeholder
st.image("assets/placeholder.jpg", caption="Holy Water", use_container_width=True)
st.markdown("""
### Holy Water
Holy Water is water that has been blessed by a priest. It is a symbol of spiritual cleansing, protection, 
and a reminder of baptism. Faithful Catholics use it upon entering churches, in homes, 
and during blessings to invite God's grace.
""")
