import streamlit as st
import os

# Path to assets
ASSETS_DIR = "assets"

# Full, extensive sacramentals dictionary
sacramentals = {
    "ashes": (
        "Blessed ashes, primarily used on Ash Wednesday, signify penance and mortality. This ancient practice, rooted in the Old Testament "
        "(e.g., Job 42:6, Daniel 9:3), symbolized repentance and humility before God. In the early Church, public penitents wore ashes "
        "to signify their sorrow for sin and their return to God’s mercy. Today, the faithful receive ashes on their foreheads, recalling "
        "their need for conversion: 'Remember you are dust, and to dust you shall return.'"
    ),
    "background": (
        "Background image placeholder representing the visual atmosphere of the Catholic Sacramentals Encyclopedia. "
        "This serves as a spiritual and artistic canvas for showcasing the sacramentals in a reverent and engaging manner."
    ),
    "bible": (
        "The Bible, the inspired Word of God, contains the Old and New Testaments and is central to Catholic teaching and worship. "
        "Catholics revere the Bible as the living Word, to be proclaimed, studied, and prayed with. Its canon was gradually affirmed "
        "by the Church Fathers in the 4th century. The Book of the Gospels is kissed and incensed at Mass, emphasizing its sacredness."
    ),
    "blessed_medals": (
        "Blessed medals, such as the Miraculous Medal and the St. Benedict Medal, are sacramentals worn or carried as reminders of faith "
        "and channels of grace. The Miraculous Medal stems from apparitions of the Blessed Virgin to St. Catherine Labouré in Paris in 1830, "
        "while the St. Benedict Medal, rich in prayers of protection and exorcism, has roots in early Benedictine monasticism."
    ),
    "blessed_salt": (
        "Blessed salt is an ancient sacramental used for purification and protection. In the Old Testament, salt symbolized covenant and "
        "incorruptibility (Leviticus 2:13). Early Christians used blessed salt during baptisms and exorcisms, and it remains a sign of "
        "spiritual defense when sprinkled in homes or consumed reverently."
    ),
    "blessing": (
        "Blessings are prayers by which the Church invokes God's favor upon people, objects, or places. They recall the priestly blessings "
        "of the Old Testament and Christ’s own actions. From the blessing of a meal to the dedication of a church, blessings sanctify the "
        "ordinary and direct it toward God’s glory."
    ),
    "candle": (
        "Candles symbolize Christ, the Light of the World. Their use dates to the earliest Christian worship and Jewish Temple practice. "
        "The Paschal Candle at Easter represents the risen Christ, while votive candles signify ongoing prayer. Candles remind the faithful "
        "of the divine presence and call to live as children of light."
    ),
    "chaplet": (
        "Chaplets are devotional prayers recited on beads, often focused on a particular mystery or saint. The Divine Mercy Chaplet, given "
        "to St. Faustina in the 1930s, is among the most beloved. Chaplets guide the faithful in meditation and intercession, deepening "
        "their prayer life through repetition and rhythm."
    ),
    "crucifix": (
        "The crucifix—showing Christ on the cross—is the supreme symbol of love and sacrifice. The Church venerates the crucifix because "
        "it represents Christ’s passion and victory over sin. Present in homes, churches, and worn by the faithful, it is a constant call "
        "to take up one’s cross and follow Him."
    ),
    "holy_bells": (
        "Holy bells, often found in churches, are blessed instruments that call the faithful to worship, mark sacred moments, and drive away evil. "
        "The ringing of bells during the Mass, especially at the consecration, recalls the heavenly liturgy and awakens reverence in those present."
    ),
    "holy_card": (
        "Holy cards are devotional images, often with prayers on the back, depicting Christ, Mary, saints, or scenes from salvation history. "
        "These small tokens of faith became popular in the 16th century and remain treasured reminders of prayer and intercession."
    ),
    "holy_doors": (
        "Holy Doors are specially designated doors in certain churches that symbolize a passage to grace and renewal. During Jubilee years, "
        "pilgrims passing through them receive special indulgences, recalling Christ’s words: 'I am the door; whoever enters through me will be saved.'"
    ),
    "holy_images": (
        "Holy images—icons, statues, and paintings—lift the mind to God and the saints. The Seventh Ecumenical Council (Nicaea II, 787) affirmed "
        "their veneration as a means of honoring the prototype, not the material object. Sacred art has inspired devotion throughout Church history."
    ),
    "holy_oil": (
        "Holy oils, including the Oil of the Sick, Oil of Catechumens, and Sacred Chrism, are essential sacramentals used in sacraments and blessings. "
        "Anointing with oil signifies healing, strengthening, and consecration, recalling biblical kings, prophets, and Christ the Anointed One."
    ),
    "holy_water": (
        "Holy water is water blessed by a priest and used to recall baptism, cleanse venial sin, and ward off evil. Sprinkling holy water on oneself "
        "or objects invokes God's blessing and protection, continuing a tradition seen in Jewish purification rites and fulfilled in Christian baptism."
    ),
    "incense": (
        "Incense, made of aromatic resins, symbolizes prayer rising to God. Its biblical use in the Temple (Psalm 141:2) carries into Christian worship. "
        "At Mass, incense honors the altar, Gospel, Eucharist, and the faithful, reminding them of the sanctity of worship and the sweet fragrance of Christ."
    ),
    "liturgical_vestments": (
        "Liturgical vestments, from albs to chasubles, set apart the sacred actions of the liturgy. Their colors and styles reflect seasons, feasts, "
        "and ranks of clergy. Originating in Roman civic dress, vestments evolved to symbolize purity, service, and dignity in divine worship."
    ),
    "medal": (
        "Generic blessed medals often depict Christ, Mary, or saints and serve as reminders of prayer and faith. They are worn or carried as tokens "
        "of devotion, asking for the intercession of holy men and women and recalling their examples."
    ),
    "palms": (
        "Blessed palms commemorate Christ’s triumphal entry into Jerusalem. On Palm Sunday, the faithful carry and keep these palms as signs of victory, "
        "faith, and hope. Many later burn them to provide the ashes for Ash Wednesday, linking the liturgical year in a cycle of grace."
    ),
    "pilgrimage_item": (
        "Items from pilgrimages—such as badges, scallop shells, or small relics—are tangible signs of spiritual journeys. Pilgrimage has been central "
        "to Catholic life since the early centuries, recalling the Christian's earthly journey toward the heavenly homeland."
    ),
    "placeholder": (
        "This placeholder image represents sacramentals not yet photographed or uploaded. It serves as a visual marker while the collection grows."
    ),
    "relic": (
        "Relics are physical remains or belongings of saints, venerated as holy because of their connection to the person. From the earliest centuries, "
        "Christians honored the bodies of martyrs, celebrating Mass over their tombs. Relics remind the faithful of the communion of saints and the "
        "promise of resurrection."
    ),
    "rosary": (
        "The rosary is a prayer and meditation on the life of Christ and Mary. Popularized by St. Dominic in the 13th century, it combines vocal prayers "
        "and mental reflection. Each bead leads the faithful through mysteries of joy, sorrow, and glory, anchoring daily life in salvation history."
    ),
    "sacramentals_of_the_dead": (
        "Sacramentals for the dead, such as prayers, holy water, and blessed candles, accompany the faithful departed. They express hope in the resurrection "
        "and communion with those who have gone before us, recalling the Church’s care for souls and the dignity of the body even after death."
    ),
    "sacapular": (
        "The scapular, especially the Brown Scapular of Our Lady of Mount Carmel, is a small garment worn as a sign of devotion and consecration. "
        "Its origins date to the Carmelite Order in the 13th century. The scapular signifies trust in Mary’s protection and a call to live the Gospel."
    ),
    "sign_of_the_cross": (
        "The Sign of the Cross is the simplest and most profound Catholic gesture, tracing the Trinity over oneself. It is both prayer and profession of faith, "
        "dating to the early Church. Christians begin and end prayers with it, sanctifying actions and seeking God’s blessing."
    )
}

# Streamlit layout
st.set_page_config(page_title="Catholic Sacramentals Encyclopedia", layout="wide")

# Background image
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
        </style>
        """,
        unsafe_allow_html=True
    )

# Display sacramentals
for item, description in sacramentals.items():
    img_path = os.path.join(ASSETS_DIR, f"{item}.jpg")
    if not os.path.exists(img_path):
        img_path = os.path.join(ASSETS_DIR, "placeholder.jpg")
    st.image(img_path, caption=item.replace("_", " ").title(), use_container_width=True)
    st.write(description)
    st.markdown("---")
