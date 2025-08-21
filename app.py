import streamlit as st
import os

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="Catholic Sacramentals Encyclopedia",
    layout="wide"
)

# -----------------------
# Background (stained glass)
# -----------------------
def set_background():
    stained_glass = os.path.join("assets", "background.jpg")
    if os.path.exists(stained_glass):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("file://{os.path.abspath(stained_glass)}");
                background-size: cover;
                background-attachment: fixed;
            }}
            .sacramental-card {{
                background: rgba(255, 255, 255, 0.7);
                border-radius: 20px;
                padding: 20px;
                margin: 15px;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

set_background()

# -----------------------
# Sacramentals Data
# -----------------------
sacramentals = [
    {"name": "Holy Water", "file": "holy_water.jpg", "desc": "Used for blessing, protection, and recalling baptism."},
    {"name": "Rosary", "file": "rosary.jpg", "desc": "A devotional prayer tool dedicated to the Blessed Virgin Mary."},
    {"name": "Scapular", "file": "scapular.jpg", "desc": "A sign of Marian devotion and a reminder of Christian duty."},
    {"name": "Crucifix", "file": "crucifix.jpg", "desc": "A cross with the figure of Christ, symbolizing redemption."},
    {"name": "Medal of St. Benedict", "file": "medal_st_benedict.jpg", "desc": "A sacramental invoking protection against evil."},
    {"name": "Palm Branches", "file": "palm_branches.jpg", "desc": "Blessed on Palm Sunday, symbolizing Christ’s victory."},
    {"name": "Ashes", "file": "ashes.jpg", "desc": "Placed on the forehead on Ash Wednesday as a call to repentance."},
    {"name": "Blessed Salt", "file": "blessed_salt.jpg", "desc": "Used for protection and blessing of homes and people."},
    {"name": "Holy Oil", "file": "holy_oil.jpg", "desc": "Consecrated oil used in sacraments and blessings."},
    {"name": "Incense", "file": "incense.jpg", "desc": "Represents prayers rising to God, used in liturgies."},
    {"name": "Candles", "file": "candles.jpg", "desc": "Blessed candles symbolize Christ, the Light of the world."},
    {"name": "Agua Benedita Fonts", "file": "holy_water_font.jpg", "desc": "Holy water stoups at church entrances for blessing."},
    {"name": "Rosary Beads", "file": "rosary_beads.jpg", "desc": "Used for meditative prayer of the mysteries of Christ."},
    {"name": "Chaplet", "file": "chaplet.jpg", "desc": "A smaller devotional string of beads for prayer."},
    {"name": "Relics", "file": "relics.jpg", "desc": "Physical remains or belongings of saints, venerated with honor."},
    {"name": "Medal of Our Lady of Grace", "file": "miraculous_medal.jpg", "desc": "Popular Marian medal promising graces."},
    {"name": "Brown Scapular", "file": "brown_scapular.jpg", "desc": "A Carmelite sacramental promising Marian protection."},
    {"name": "Medal of St. Michael", "file": "medal_st_michael.jpg", "desc": "Invokes the Archangel’s defense against evil."},
    {"name": "Blessed Crucifix", "file": "blessed_crucifix.jpg", "desc": "A crucifix with special blessing for spiritual protection."},
    {"name": "Water from Lourdes", "file": "lourdes_water.jpg", "desc": "Famous Marian shrine water, associated with healings."},
    {"name": "Rosary Rings", "file": "rosary_ring.jpg", "desc": "Portable rosary ring for prayer on the go."},
    {"name": "Stations of the Cross", "file": "stations_cross.jpg", "desc": "Devotion recalling Christ’s Passion."},
    {"name": "Holy Cards", "file": "holy_cards.jpg", "desc": "Cards with saint images and prayers, widely distributed."},
    {"name": "Easter Candle", "file": "easter_candle.jpg", "desc": "The Paschal candle, symbol of Christ’s resurrection."}
]

# -----------------------
# Display
# -----------------------
st.title("Catholic Sacramentals Encyclopedia")

cols = st.columns(3)

for i, item in enumerate(sacramentals):
    with cols[i % 3]:
        st.markdown("<div class='sacramental-card'>", unsafe_allow_html=True)
        img_path = os.path.join("assets", item["file"])
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.image(os.path.join("assets", "placeholder.jpg"), use_container_width=True)
        st.subheader(item["name"])
        st.write(item["desc"])
        st.markdown("</div>", unsafe_allow_html=True)
