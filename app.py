import streamlit as st
import os

# App config
st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# Add custom CSS for hover glow
st.markdown(
    """
    <style>
    /* Background stained glass */
    body {
        background-image: url('assets/stained_glass.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    /* Glow effect for sacramental images */
    .sacramental-card img {
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        border-radius: 12px;
    }
    .sacramental-card img:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 20px rgba(255, 255, 200, 0.7);
    }

    /* Adjust text readability */
    .sacramental-description {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1em;
        border-radius: 12px;
        margin-top: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Catholic Sacramentals Encyclopedia")

# Path to images
assets_dir = "assets"

# Example sacramentals with descriptive text
sacramentals = [
    {
        "name": "holy_water",
        "title": "Holy Water",
        "description": "Holy Water has been used in the Catholic Church since ancient times. It is blessed by a priest and serves as a reminder of baptism, purity, and the washing away of sin. Historically, fonts of holy water were present at the entrances of churches as early as the 4th century.",
    },
    {
        "name": "rosary",
        "title": "Rosary",
        "description": "The Rosary is one of the most significant sacramentals in Catholic tradition. Originating in the Middle Ages, it involves meditative prayer on the life of Christ and the Virgin Mary using beads. The Dominican Order is credited with popularizing it in the 13th century.",
    },
    {
        "name": "scapular",
        "title": "Scapular",
        "description": "The Scapular is a devotional garment symbolizing dedication to Mary and protection. First associated with the Carmelite Order in the 13th century, it is worn as a sign of faith and commitment to a Christian life.",
    },
    # Add the rest of your 24 sacramentals here, following the same pattern...
]

# Display items
cols = st.columns(3)
for i, item in enumerate(sacramentals):
    img_path = os.path.join(assets_dir, f"{item['name']}.jpg")
    col = cols[i % 3]

    with col:
        # Image card with hover
        if os.path.exists(img_path):
            col.markdown(
                f"""
                <div class="sacramental-card">
                    <img src="{img_path}" width="100%">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            col.markdown(
                f"""
                <div class="sacramental-card">
                    <img src="assets/placeholder.jpg" width="100%">
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Description
        col.markdown(
            f"""
            <div class="sacramental-description">
                <h4>{item['title']}</h4>
                <p>{item['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
