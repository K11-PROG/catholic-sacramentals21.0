import streamlit as st
import os

st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# Custom CSS for hover effect
st.markdown(
    """
    <style>
    body {
        background-image: url('assets/background.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .sacramental-card img {
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        border-radius: 12px;
    }
    .sacramental-card img:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(255, 255, 180, 0.7);
    }
    .sacramental-card {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Catholic Sacramentals Encyclopedia")

sacramentals = [
    {
        "name": "holy_water",
        "title": "Holy Water",
        "description": "Holy water is water blessed by a priest and used for blessings, protection, and as a reminder of baptism."
    },
    {
        "name": "rosary",
        "title": "Rosary",
        "description": "A string of beads used for prayer and meditation, recalling the mysteries of Christ and the Virgin Mary."
    },
    {
        "name": "scapular",
        "title": "Scapular",
        "description": "A devotional garment worn as a sign of faith and consecration to Mary or a religious order."
    },
    {
        "name": "relic",
        "title": "Relic",
        "description": "Sacred remains or objects associated with a saint, venerated for their closeness to holiness."
    },
    # Add the rest of your sacramentals here...
]

# Display sacramentals
cols = st.columns(3)
for i, item in enumerate(sacramentals):
    with cols[i % 3]:
        st.markdown(f"### {item['title']}")
        img_path = os.path.join("assets", f"{item['name']}.jpg")
        if os.path.exists(img_path):
            st.markdown(
                f"""
                <div class="sacramental-card">
                    <img src="{img_path}" width="100%">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.write("Image missing.")
        st.write(item["description"])
