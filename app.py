import streamlit as st
import os

# Set up assets directory
ASSETS_DIR = "assets"

# Background image CSS (handled separately, not included as a displayed item)
background_path = os.path.join(ASSETS_DIR, "background.jpg")
if os.path.exists(background_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('{background_path}');
            background-size: cover;
            background-position: center;
        }}
        img:hover {{
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
            transition: all 0.3s ease-in-out;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Extensive, descriptive content for each sacramental
sacramentals = {
    "ashes": "Ashes, traditionally blessed on Ash Wednesday, symbolize penitence and mortality. Christians receive a cross of ashes on their forehead as a call to conversion. Historically, this practice dates back to the early centuries of the Church, when public penitents wore sackcloth and ashes as a sign of repentance.",
    "bible": "The Holy Bible is the inspired Word of God and the foundational text of the Christian faith. Catholic editions include the deuterocanonical books. The Bible has been venerated, read aloud in liturgies, and preserved with care since the first centuries. Illuminated manuscripts and printed editions testify to its enduring reverence.",
    "blessed_medals": "Blessed medals, such as the Miraculous Medal or St. Benedict Medal, are sacramentals invoking God's protection and the intercession of saints. These medals carry prayers and symbols often tied to apparitions or monastic traditions. They became particularly popular from the 19th century onward, emphasizing devotion and faith.",
    "blessed_salt": "Blessed salt is sacramentally blessed to repel evil and remind the faithful of Christ’s words: 'You are the salt of the earth.' Historically used in baptisms and exorcisms, its roots go back to the early Church and the Old Testament, where salt was a symbol of covenant and purification.",
    "blessing": "Blessings, given by clergy, sanctify people, objects, or places, invoking God’s favor. This practice stems from Jewish traditions and early Christianity, when bishops and priests blessed homes, fields, and individuals. Blessings remind the faithful that all creation is meant for God’s glory.",
    "candle": "Blessed candles are a sign of Christ as the light of the world. Used during liturgies, processions, and at home, they have been a staple of Christian worship since the earliest centuries. Candlemas (Feast of the Presentation) especially highlights their importance. They remind us of vigilance and prayer.",
    "chaplet": "Chaplets are structured prayers, often using beads, such as the Divine Mercy Chaplet. Inspired by the Rosary, these devotions grew during the Middle Ages, providing the faithful with ways to meditate on Christ’s mysteries and the lives of the saints. They encourage rhythmic and contemplative prayer.",
    "crucifix": "A crucifix depicts Christ on the Cross, emphasizing His sacrifice. Crucifixes have been central to Catholic worship since the early Church, adorning altars and homes. They serve as a visual reminder of redemption and God's boundless love, often blessed to bring spiritual protection.",
    "holy_bells": "Holy bells, often blessed, call the faithful to prayer, mark sacred moments, and sometimes are rung during exorcisms. In medieval Europe, bells were believed to drive away storms and evil. Their ringing still resonates in churches worldwide, linking heaven and earth.",
    "holy_card": "Holy cards are small devotional images, often with prayers. They became popular in the 16th century as printing spread. Cards depict saints, biblical scenes, or prayers and are treasured for personal devotion, reminders of faith, and gifts of encouragement.",
    "holy_doors": "Holy Doors, opened during Jubilee Years, symbolize extraordinary grace and entry into God’s mercy. Pilgrims crossing these doors receive indulgences. The tradition dates back to the 15th century at St. Peter’s Basilica, spreading to cathedrals worldwide.",
    "holy_images": "Sacred images, icons, and statues aid devotion and recall the Incarnation—God made visible. From catacomb frescoes to Renaissance art, holy images have always been central in Catholic life, teaching and inspiring the faithful while lifting hearts to heaven.",
    "holy_oil": "Sacred oils (chrism, oil of catechumens, oil of the sick) are consecrated annually at the Chrism Mass. They are used in sacraments like Baptism, Confirmation, Holy Orders, and Anointing of the Sick. Their use dates back to apostolic times and signifies the Holy Spirit’s action.",
    "holy_water": "Holy water recalls Baptism and is used for blessing, protection, and exorcism. The practice of blessing water dates to the early Church and is rooted in Jewish purification rites. Fonts at church entrances invite the faithful to renew their baptismal promises.",
    "incense": "Incense, used in liturgies, symbolizes prayer rising to God. Mentioned in the Old and New Testaments, incense adds solemnity and sanctity to worship. The sweet-smelling smoke honors sacred spaces and objects, echoing ancient temple worship.",
    "liturgical_vestments": "Liturgical vestments, worn by clergy, signify roles and reverence. Their styles evolved from Roman garments, with colors and forms expressing the seasons and feasts. Each piece, from alb to chasuble, carries symbolic meaning and recalls centuries of tradition.",
    "medal": "Medals, whether depicting saints or sacred mysteries, are tangible signs of devotion. Beyond blessed medals like St. Benedict’s, they often commemorate pilgrimages or sacraments. They serve as reminders of faith and channels of grace.",
    "palms": "Blessed palms, distributed on Palm Sunday, recall Christ’s triumphal entry into Jerusalem. They are kept in homes as sacramentals, often woven into crosses. Their use is ancient, linking liturgy to biblical events and popular piety.",
    "pilgrimage_item": "Objects brought from pilgrimage sites, such as water, stones, or cloths, remind the faithful of their spiritual journeys. Pilgrimages have been integral to Catholic life since the earliest centuries, fostering conversion and renewal.",
    "placeholder": "This placeholder represents where images and details will be added. It ensures the structure of the app remains intact while awaiting full content.",
    "relic": "Relics are physical remains or belongings of saints, venerated as points of contact with the holy. Their veneration is rooted in the early Church, when Christians gathered at martyrs' tombs. Classified as first-, second-, or third-class, relics inspire faith and remind us of the communion of saints.",
    "rosary": "The Rosary is a meditative prayer centered on the life of Christ and Mary. Originating in the Middle Ages, it combines vocal prayer and contemplation. Each bead represents prayerful rhythm, leading believers through the mysteries of faith.",
    "sacramentals_of_the_dead": "Sacramentals for the dying include blessed candles, crucifixes, and prayers like the Litany of the Saints. They prepare the soul for its final journey, providing comfort and grace. These practices have roots in early Christian care for the dying.",
    "sacapular": "The scapular, especially the Brown Scapular of Our Lady of Mount Carmel, is a sign of Marian devotion. Worn as a garment of grace, its origins trace back to the Carmelite Order in the 13th century. It symbolizes commitment to prayer and Christian living.",
    "sign_of_the_cross": "The Sign of the Cross, traced on oneself, recalls the Trinity and redemption through Christ’s Cross. This ancient gesture dates back to the early Church and is used at the start and end of prayers, blessing daily life and actions."
}

st.title("Catholic Sacramentals Encyclopedia")

# Display sacramentals with hover effect
for item, desc in sacramentals.items():
    img_path = os.path.join(ASSETS_DIR, f"{item}.jpg")
    if os.path.exists(img_path):
        st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
    else:
        st.write(f"**{item.replace('_', ' ').title()}** - *Image placeholder*")
    st.write(desc)
    st.markdown("---")
