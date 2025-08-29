import streamlit as st
import base64
import json
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(page_title="Catholic Sacramentals", layout="wide")

ASSETS_DIR = Path("assets")
EXTS = [".jpg", ".jpeg", ".png", ".webp"]

ITEM_KEYS = [
    "ashes", "bible", "blessed_medals", "blessed_salt", "blessing",
    "candle", "chaplet", "crucifix", "holy_bells", "holy_card",
    "holy_doors", "holy_images", "holy_oil", "holy_water", "incense",
    "liturgical_vestments", "palms", "thurible",
    "relic", "rosary", "cord", "scapular",
    "monstrance", "eucharistic_host"
]

# ---------- DESCRIPTIONS (paragraph-form) ----------
DESC = {
    "ashes": """Ashes, used on Ash Wednesday, date back to the early Church and Jewish penitential practices. The imposition of ashes recalls mortality and repentance, connecting Christians to ancient Israelite traditions and reminding them of Genesis 3:19.

In our present liturgy for Ash Wednesday, we use ashes made from the burned palm branches distributed on the Palm Sunday of the previous year. The priest blesses the ashes and imposes them on the foreheads of the faithful, making the sign of the cross and saying, “Remember, man you are dust and to dust you shall return,” or “Turn away from sin and be faithful to the Gospel.”

When we begin the holy season of Lent in preparation for Easter, we mourn and do penance for our sins, convert our hearts to the Lord, renew baptismal promises, and look forward to the kingdom of God.""",
    "bible": """The Bible, meaning 'books,' is a library of sacred writings. It consists of the Old Testament and the New Testament. The Bible originated as a collection of religious texts written over many centuries, primarily in Hebrew, Aramaic, and Greek.

The Old Testament is the Hebrew Bible as interpreted among the various branches of Christianity. The New Testament contains the four Gospels (Matthew, Mark, Luke, and John), Acts, 21 letters, and Revelation.

The Gospels narrate the life, death, and teachings of Jesus Christ. The Bible is viewed as the inspired word of God and a guide for Christian living. Catholic editions include the Deuterocanonical books, preserved by the Septuagint, a Greek translation of the Hebrew Bible that was significant for the early Christians. Since the earliest centuries, illuminated manuscripts and later printed Bibles were treasured, forming the foundation of Christian teaching.

The Bible has been translated into over 2,500 languages, making it the most widely distributed book in history. The Bible has profoundly influenced Western culture, literature, and moral thought. Its themes of creation, redemption, and divine justice resonate across various societies and religions.""",
    "blessed_medals": """Blessed medals gained popularity in the early Middle Ages as tokens of faith and protection.

There are many medals in use among the catholics. They commemorate saints, events, or Marian devotions and often bear protective inscriptions. 

The Miraculous Medal, also known as the Medal of the Immaculate Conception, was designed following the visions of St. Catherine Labouré in 1830. The front of the medal depicts the Blessed Virgin Mary standing on a globe, crushing a serpent under her feet, with rays of light emanating from her hands.

This depiction of the Blessed Virgin illustrates her sinlessness and her victory over the devil, represented by the serpent. The rays of light emanating from her hands signify the graces she bestows upon those who seek her intercession. The words “O Mary, conceived without sin, pray for us who have recourse to thee” encircle the image.

On the reverse side, there is a cross and an M intertwined, with two hearts—the Sacred Heart of Jesus and the Immaculate Heart of Mary—and twelve stars representing the Apostles. The Miraculous Medal is often worn to seek Mary’s intercession and as a testament to faith in her protection and grace. 

The Saint Benedict medal is rich in symbolism and is known as a powerful weapon in spiritual warfare. It has its own special blessing in the Roman Ritual that includes powerful prayers of exorcism. One side of the medal displays Saint Benedict holding a cross and the Rule of Saint Benedict. These words encircle the saint: “Eius in obitu nostro praesentia muniamur!” (“May we be strengthened by his presence in the hour of our death!”)

Saint Michael the Archangel is known as the leader of the heavenly armies and our protector against evil. His medal usually features him wielding a sword or spear, standing triumphantly over Satan, represented as a dragon or serpent. This powerful imagery symbolizes Saint Michael’s victory over evil and his role as a defender of the faithful.

Wearing a Saint Michael medal is a call for his protection against the snares of the devil and a reminder of the spiritual battle between good and evil. It is especially popular among police officers, soldiers, and those in dangerous professions who seek courage and protection in their line of duty.""",
    "blessed_salt": """Blessed salt is a sacramental in the Catholic tradition, used historically in various rites, including baptism, to symbolize purification and protection. Its origins trace back to early Christianity, where it was associated with blessings and exorcisms, as noted in biblical accounts like the healing of the waters of Jericho by the prophet Elisha.

Salt was considered a valuable commodity, symbolizing purity and preservation, and was used in sacrifices by the Israelites. By the fourth century, Augustine of Hippo described the use of blessed salt as "visible forms of invisible grace." The Third Council of Carthage in the third century mandated the use of salt for catechumens before baptism. The earliest prayers for blessing salt and water are from Merovingian France, around 600-751 AD.

The Roman Rite of the Catholic Church includes specific prayers for blessing salt, emphasizing its protective and purifying qualities. Blessed salt serves as a sacramental, believed to provide spiritual protection and sanctification. It can be sprinkled in homes or carried for personal protection against evil influences. The practice encourages a deeper connection to faith and the presence of God in daily life.""",
    "blessing": """Blessings are among the oldest sacramentals, rooted in the Jewish practice of berakhot.

Early Christian communities blessed homes, fields, and travelers. The Roman Pontifical preserved many such prayers, sanctifying daily life.""",
    "candle": """Candles symbolize Christ as the Light of the World. Early Christians used candles in catacombs; by the 4th century, they became standard in liturgy.

Their origins can be traced back to Jewish practices, where a perpetual light was kept in the Temple to signify God's presence, which Christians adapted for their own rituals over time.

There are several types of candles used in the Catholic tradition. The Paschal candle, used during Easter Vigil, represents the Resurrection and light of Christ. Votive candles are lit for specific prayer intentions, often placed before statues or images. Altar candles are present during Mass to signify the presence of Christ in the Eucharist.""",
    "chaplet": """A chaplet is a form of Christian prayer which uses prayer beads, and which is similar to but distinct from the Rosary. Some chaplets have a strong Marian element, others focus more directly on Jesus Christ and his Divine Attributes (the Divine Mercy Chaplet), or one of the many saints, such as the Chaplet of St Michael. Chaplets are "personal devotionals" and depending on the origins, each one of the chaplets may vary considerably. In the Roman Catholic Church, while the usual five-decade Dominican rosary is also considered to be a chaplet, the other chaplets often have fewer beads and decades than a traditional rosary and may use a different set of prayers.
    
    The origins of chaplets can be traced back to various revelations and traditions within the Catholic Church. The Divine Mercy Chaplet, for instance, was revealed to St. Faustina Kowalska in the 1930s, emphasizing the importance of mercy in Christian life. Other chaplets, like the Chaplet of St. Michael, have roots in medieval devotion practices.""",
    "crucifix": """The crucifix, with the figure of Christ, emerged in the 6th century and spread widely by the Middle Ages.

    A crucifix (from the Latin cruci fixus meaning '(one) fixed to a cross') is a cross with an image of Jesus on it, as distinct from a bare cross. The representation of Jesus himself on the cross is referred to in English as the corpus (Latin for 'body'). The crucifix emphasizes Jesus' sacrifice, including his death by crucifixion, which Christians believe brought about the redemption of mankind. Most crucifixes portray Jesus on a Latin cross, rather than a Tau cross or a Coptic cross.

    Western crucifixes usually have a three-dimensional corpus, but in Eastern Orthodoxy Jesus' body is normally painted on the cross, or in low relief. Strictly speaking, to be a crucifix, the cross must be three-dimensional, but this distinction is not always observed. An entire painting of the crucifixion of Jesus including a landscape background and other figures is not a crucifix either.

On some crucifixes a skull and crossbones are shown below the corpus, referring to Golgotha (Calvary), the site at which Jesus was crucified, which the Gospels say means in Hebrew "the place of the skull. Medieval tradition held that it was the burial-place of Adam and Eve, and that the cross of Christ was raised directly over Adam's skull, so many crucifixes manufactured in Catholic countries still show the skull and crossbones below the corpus. There may also be a short projecting nameplate, showing the letters INRI (Greek: INBI). INRI is an acronym of the Latin phrase IESVS·NAZARENVS·REX·IVDÆORVM (Jesus Nazarenus, rex Judæorum), which translates into English as "Jesus Nazarene, King of the Jews."

Western crucifixes may show Christ dead or alive, the presence of the spear wound in his ribs traditionally indicating that he is dead. In either case his face very often shows his suffering. Eastern crucifixes have Jesus' two feet nailed side by side, rather than crossed one above the other, as Western crucifixes have shown them since around the 13th century. The crown of thorns is also generally absent in Eastern crucifixes, since the emphasis is not on Christ's suffering, but on his triumph over sin and death. It was in Italy that the emphasis was put on Jesus' suffering and realistic details, during a process of general humanization of Christ favored by the Franciscan order.

In the early Church, many Christians hung a cross on the eastern wall of their house in order to indicate the eastward direction of prayer. Prayer in front of a crucifix, which is seen as a sacramental, is often part of devotion for Christians, especially those worshipping in a church, also privately. The person may sit, stand, or kneel in front of the crucifix, sometimes looking at it in contemplation, or merely in front of it with head bowed or eyes closed. During the Middle Ages small crucifixes, generally hung on a wall, became normal in the personal cells or living quarters first of monks, then all clergy, followed by the homes of the laity, spreading down from the top of society as these became cheap enough for the average person to afford. Most towns had a large crucifix erected as a monument, or some other shrine at the crossroads of the town.

The crucifix confronts the believer with the Passion and remains central to Catholic identity, often blessed for protection.""",
    "holy_bells": """Bells were blessed as early as the 8th century, called 'campanae' or 'sacred trumpets.'

Their ringing at Mass or in towers was believed to ward off storms and evil, summoning the faithful to prayer.

The origins of the ringing of the bells during the consecration date back to the time when the Mass was said in Latin, and many of the words said by the celebrant were spoken in a low voice. Rood screens also became popular in the Middle Ages, and many of the laity attending Mass had an obstructed view. The use of the bells was practical: it called people’s attention to the fact that the consecration was taking place.

Although many of the practical reasons for the ringing of the bells no longer exist, they are still a part of our liturgical tradition and still call wandering minds back to the altar and the importance of what is happening.

The Bible neither requires nor forbids the ringing of church bells, but does encourage the faithful to “make a joyful noise” (Psalm 100). Since the fifth century, some Christian churches have been ringing bells for spiritual and practical purposes such as to call the faithful to worship, to highlight a particular stage during a church service, to remind the faithful of God’s presence in their daily lives, and to announce important occurrences to the local community.""",
    "holy_card": """Holy cards began as woodcuts in the late Middle Ages and became popular devotional items by the 17th century.

They often depict saints or events and were used as catechetical tools.""",
    "holy_doors": """Holy Doors, opened during Jubilee years, originated in the 15th century at St. Peter’s Basilica.

Passing through them symbolizes spiritual renewal and the reception of special indulgences.""",
    "holy_images": """Holy images trace to the earliest Christian catacombs. Icons flourished in the East; statues in the West.
    
Veneration in the Catholic faith refers to showing respect or honor to someone or something holy. It is distinct from worship, which is reserved for God alone. When Catholics venerate icons or statues, they are not treating the objects as divine. Instead, they use these images as reminders of God, the Virgin Mary, or the saints. This practice stems from the belief that physical representations can aid spiritual focus.

The use of sacred images in Christianity has roots in the early Church. In the first few centuries, Christians painted images of Christ and the saints in places like the catacombs. These images served as teaching tools for a largely illiterate population. Over time, the practice grew as a way to inspire devotion. By the 4th century, churches began incorporating more artwork to reflect biblical stories. The tradition faced challenges, particularly during the Iconoclastic Controversy in the 8th century. Some argued that images violated the commandment against graven images (Exodus 20:4-5). However, Church leaders defended the practice, emphasizing its spiritual value. This debate led to a formal clarification of the tradition. The early Church saw icons as windows to the divine, not as objects of worship.

The Second Council of Nicaea, held in 787, was a pivotal moment for this tradition. It addressed the Iconoclastic Controversy, where some Byzantine emperors sought to ban religious images. The council affirmed that veneration of icons was legitimate and theologically sound. It clarified that honor given to an image passes to the person it represents. For example, venerating an icon of Christ directs honor to Christ Himself. The council condemned the destruction of icons and upheld their use in worship spaces. This decision relied on both scripture and tradition. The fathers of the council cited John 1:14, which speaks of the Incarnation, as a basis for sacred images. Their ruling shaped Catholic practice for centuries. It remains a cornerstone of the Church’s teaching on this subject.""",
    "holy_oil": """Holy oil has Old Testament roots (Exodus 30). Chrism was mentioned by Church Fathers like Tertullian and Hippolytus.

Consecrated oils are still used in Baptism, Confirmation, Holy Orders, and the Anointing of the Sick.""",
    "holy_water": """Holy water has its roots in early Christian practices and is believed to date back to the time of the Apostles. The earliest written references to holy water appear in the Apostolic Constitutions, a Christian document from around the 4th century AD. This text suggests that the practice of blessing water for spiritual purposes was established by the Apostle Matthias, who was chosen to replace Judas Iscariot.

The use of water for purification is also found in the Old Testament, where ritual ablutions were performed by the Jewish priests. These practices laid the groundwork for the Christian use of holy water, which symbolizes spiritual cleansing and renewal. Key biblical references include the creation narrative in Genesis, where the Spirit of God moves over the waters, and various purification rituals described in the Law of Moses.

In the Catholic tradition, holy water is typically blessed by a priest, often using a mixture of water and blessed salt. This process is rooted in the belief that water, as a sacred element, can convey God's grace and protection. The blessing of holy water is accompanied by prayers that invoke divine assistance and protection against evil.""",
    "incense": """Incense was offered in the Temple of Jerusalem and adopted by Christians by the 4th century.

Its smoke symbolizes prayers rising to heaven (Psalm 141:2) and sanctifies the liturgy.""",
    "liturgical_vestments": """Vestments evolved from Roman attire. By the 5th century, they became distinct for worship.

Colors signify liturgical seasons, and garments like the chasuble and stole symbolize Christ’s yoke and charity.""",
    "palms": """Palms in the Catholic tradition originate from the biblical account of Jesus' triumphal entry into Jerusalem, where crowds greeted him by laying down palm branches. This practice has evolved into the celebration of Palm Sunday, marking the beginning of Holy Week, where blessed palms are distributed to the faithful during Mass.

The event is mentioned in all four canonical Gospels, highlighting its importance in Christian tradition.
Jesus rode into Jerusalem on a donkey, symbolizing peace, as opposed to a horse, which would signify war.

The palms symbolize victory, peace, and eternal life. They are often woven into crosses and displayed in homes as reminders of faith.
After Palm Sunday, the palms should not be discarded. Instead, they are treated with reverence and can be burned or buried when no longer needed.

This rich tradition emphasizes the significance of palms in the context of faith and community, serving as a reminder of Jesus' message of peace and salvation.""",
    "thurible": """The thurible or censer holds burning charcoal and incense. Its use mirrors Jewish Temple worship and became a fixed part of Christian liturgy by the 6th century.

Its fragrant smoke signifies reverence and prayer.

A thurible (via Old French from Medieval Latin turibulum) is a metal incense burner suspended from chains, in which incense is burned during worship services. It is used in Christian churches, including those of the Roman Catholic, Eastern Orthodox, Assyrian Church of the East, Oriental Orthodox, Lutheran and Old Catholic denominations, as well as in some Continental Reformed, Presbyterian, Methodist and Anglican churches (with its use almost universal amongst Anglican churches of Anglo Catholic churchmanship). The acolyte or altar server who carries the thurible is called the thurifer. The practice is rooted in the earlier traditions of Judaism dating from the time of the Second Jewish Temple, and is still ceremoniously utilized in some Renewal communities.""",
    "relic": """Relics have been venerated since the 2nd century, with martyrs’ graves becoming pilgrimage sites.

The earliest Christian references to relics can be found in the New Testament. For example, in the Acts of the Apostles, it is noted that handkerchiefs that touched St. Paul were able to heal the sick. This scriptural basis established the belief that physical objects associated with saints could carry divine grace.

Catholic relics are categorized into three classes. 
First Class Relics, actual physical remains of a saint (e.g., bones).
Second Class Relics, items that belonged to or were used by a saint (e.g., clothing).
Third Class Relics, objects that have touched a first or second class relic (e.g., small pieces of cloth).

The practice of relic veneration was formally recognized and regulated by the Church over time. The Second Council of Nicaea in 787 decreed that relics should be used to consecrate churches, further embedding their significance in Catholic worship. The Council of Trent (1545 and 1563) affirmed their use, and they remain integral to altars and devotions.""",
    "rosary": """The rosary’s origins lie in the 12th-13th century, with Dominican promotion by St. Dominic.

It unites vocal prayer and meditation on Christ’s life and Mary’s role, a devotion embraced worldwide.

The Rosary includes six of Catholicism’s most familiar prayers: the Apostles’ Creed, the Our Father, the Hail Mary, the Glory Be, the Fátima Prayer (“O My Jesus”) and the Hail Holy Queen. The inclusion of these prayers in the Rosary did not happen overnight but was a lengthy evolution down through the centuries. Originally, the Our Father was said 150 times as a replacement for the psalms, saying the prayer on each bead of the Rosary string. A Glory Be was normally part of the prayer. During the 11th century, St. Peter Damian (d. 1072) suggested praying 150 Angelic Salutations, the Hail Mary, as an alternative prayer to the Our Father. The Hail Mary at that time consisted of Gabriel’s angelic salutation to Mary, “Hail Mary full of Grace the Lord is with you” (see Lk 1:28-31), and the exchange between Mary and Elizabeth during the visitation, “Blessed art thou among women and blessed is the fruit of thy womb” (Lk 1:39-45). The name of Jesus (“blessed is the fruit of thy womb, Jesus”) was included sometime later. In 1365, a Carthusian monk named Henry of Kalkar (1328-1408) divided the 150 Hail Marys into 15 groups of 10 beads each. He placed an Our Father between each group or decade (10 beads); the prayer was thus made up of 10 Hail Marys, repeated 15 times with an Our Father in between each set.

By the first part of the 15th century the Hail Mary consisted of: “Hail Mary, full of Grace, the Lord is with thee. Blessed art thou among women and blessed is the fruit of thy womb, Jesus.” The third part, known as the petition (“Pray for us Holy Mother of God…”) is traced back to the Council of Ephesus in 431. At that council, Church leaders officially defined Mary as not only the Mother of Jesus but as Theotokos (God-bearer, the Mother of God).

On the night this proclamation was made, the citizens of Ephesus marched through the town joyfully chanting, “Holy Mary Mother of God, pray for us sinners.” This petition, including the words “now and at the hour of our death” would become part of the prayer by the time Pope St. Pius V (r. 1566-72) issued the papal bull Consueverunt Romani Pontifices in 1569 encouraging the universal use of the Rosary.

Since Pope Pius V issued that document, only the Fátima Prayer has been added to the Rosary. The Fátima prayer, given to the Portuguese children during the Fátima apparition in 1917, is widely used, but it is not universal. The Rosary made up of 150 beads, promoted by Pope Pius V, is still subscribed to by the Church but is, of course, different than the popular Rosary with 50 beads that many of us carry in our pockets.

From the 16th century until the 21st century there were three sets of mysteries: the Joyful, the Glorious and the Sorrowful. But in 2002 Pope St. John Paul II added the Mysteries of Light. The intent was to include meditations on the time in Jesus’ life between His incarnation (a Joyful Mystery) and His passion (a Sorrowful Mystery).

How many soldiers have repeated the Hail Mary over and over on the battlefield? In our darkest hour, even the hour of our death, we plead for the intercession, the blessing and comfort of the Blessed Mother using this 700-year-old devotion which ends, in part, “Turn then most gracious advocate thine eyes of mercy toward us …”""",
    "cord": """Cords, like the Cord of St. Joseph or St. Philomena, appeared in the 17th century.

Worn around the waist, they symbolize purity, fidelity, and special petitions for protection and grace.""",
    "scapular": """The scapular developed from monastic habits. The Brown Scapular, linked to Our Lady of Mount Carmel in the 13th century, became a sign of Marian devotion and consecration.""",
    "monstrance": """Monstrances developed in the 13th century to display the consecrated Host during adoration and processions.

    The Monstrance also was known as the Ostensorium in accordance with its etymology. It is the vessel used in the Roman Catholic Church for the more convenient exhibition of some object of piety.  Such as the consecrated Eucharistic host during Eucharistic adoration or Benediction of the Blessed Sacrament. This word monstrance comes from the Latin word “monstrare” while the word ostensorium came from the Latin word “ostendere”.

    Both terms, mean “to show”, are used for vessels intended for the exposition of the Blessed Sacrament, but ostensorium has only this meaning.[In the Catholic tradition, at the moment of consecration the elements (called “gifts” for liturgical purposes) are transformed (literally transubstantiated) into the body and blood of Christ. Both the name ostensorium and the kindred word monstrance were originally referred to all kinds of vessels of goldsmith’s or silversmith’s work in which glass, crystal, and so on were so used to distinguish contents from another – Whether the object thus honoured were the Sacred Host itself or only the relic of some saint. Modern times has limited both terms to vessels intended for the exposition of the Blessed Sacrament, and it is in this sense only that we use ostensorium/Monstrance.

    Monstrances are usually different in design. Most of them are carried by the priest. Others may be fixed at a place, typically for displaying the host in a special side or a chapel, often called the “Chapel of the Blessed Sacrament”. For portable designs, the preferred form is a sunburst on a stand, usually topped by a cross.

During Medieval times, monstrances were more varied in form than contemporary ones. Those used for relics, and occasionally for the host, typically had a crystal cylinder in a golden stand, while those usually used for hosts had a crystal window in a flat-faced golden construction, which could stand on its base.

In the centre of the sunburst, the monstrance normally has a small round glass the size of a Host, through which the Blessed Sacrament can be seen. Behind this glass is a round container made of glass and gilded metal, called a lunette. This holds the Host securely in place. When not in the monstrance, the Host in its luna is placed in a special standing container, called a standing pyx, in the Tabernacle.

Often gilded and radiant, they emphasize Christ’s Real Presence and became common after Corpus Christi was established in 1264.""",
    "eucharistic_host": """The Eucharistic Host, unleavened bread, becomes the Body of Christ at the consecration.

Reserved for adoration and Communion, the Host has been central since the Last Supper and was solemnly elevated in the Mass by the 12th century."""
}

# ---------- QUICK FACTS (for tooltips) ----------
FACTS = {
    "ashes": "Ash Wednesday ashes: 6th–7th c. penitential roots.",
    "bible": "Canon received in early councils; basis of Christian teaching.",
    "blessed_medals": "Miraculous (1830) & Benedict medals widely used.",
    "blessed_salt": "Used since 3rd c.; recalls Elisha’s purification.",
    "blessing": "Jewish berakhot roots; sanctifies daily life.",
    "candle": "Paschal, votive, altar candles symbolize Christ’s light.",
    "chaplet": "Devotional beads beyond the rosary; Divine Mercy (20th c.).",
    "crucifix": "Corpus on the cross popularized from 6th c.",
    "holy_bells": "Consecration bells refocus attention during Mass.",
    "holy_card": "Woodcuts evolved into popular catechetical images.",
    "holy_doors": "Jubilee doors: indulgences & renewal (since 15th c.).",
    "holy_images": "Icons/statues venerated; affirmed at Nicaea II (787).",
    "holy_oil": "Chrism & oils in sacraments since early Church.",
    "holy_water": "Blessed water recalls Baptism; protection & blessing.",
    "incense": "Temple tradition; prayers ‘rise’ to God (Ps 141:2).",
    "liturgical_vestments": "Roman garments adapted for worship by 5th c.",
    "palms": "Palm Sunday recalls triumphal entry (4th c. Jerusalem).",
    "thurible": "Censer symbolizes reverence; fixed by 6th c.",
    "relic": "Veneration since 2nd c.; affirmed by councils.",
    "rosary": "Dominican promotion; meditative prayer on Christ’s life.",
    "cord": "Worn for purity & petitions (since 17th c.).",
    "scapular": "Monastic origin; Marian consecration sign.",
    "monstrance": "Displays the Host for adoration (since 13th c.).",
    "eucharistic_host": "Elevated at Mass from 12th c.; Real Presence."
}

# ---------- TIMELINE ORDER (approximate historical emergence) ----------
TIMELINE = [
    "bible", "holy_images", "holy_oil", "incense", "ashes",
    "candle", "crucifix", "relic", "holy_water", "liturgical_vestments",
    "blessing", "blessed_salt", "palms", "holy_bells", "holy_card",
    "rosary", "scapular", "cord", "blessed_medals", "holy_doors",
    "chaplet", "thurible", "monstrance", "eucharistic_host"
]

# ---------- CATEGORIES ----------
ITEM_CATEGORIES = {
    "ashes": ["Lent", "Penitential", "Sacramentals"],
    "bible": ["Scripture", "Biblical"],
    "blessed_medals": ["Devotional", "Marian", "Protection", "Sacramentals"],
    "blessed_salt": ["Blessings", "Sacramentals", "Protection"],
    "blessing": ["Blessings", "Sacramentals"],
    "candle": ["Liturgical", "Devotional"],
    "chaplet": ["Prayer Beads", "Devotional", "Marian"],
    "crucifix": ["Holy Objects", "Devotional", "Protection"],
    "holy_bells": ["Liturgical", "Devotional"],
    "holy_card": ["Devotional", "Catechesis"],
    "holy_doors": ["Jubilee", "Indulgences", "Pilgrimage"],
    "holy_images": ["Holy Objects", "Icons", "Catechesis"],
    "holy_oil": ["Sacraments", "Liturgical"],
    "holy_water": ["Blessings", "Protection", "Sacramentals"],
    "incense": ["Liturgical", "Fragrance"],
    "liturgical_vestments": ["Liturgical"],
    "palms": ["Holy Week", "Lent"],
    "thurible": ["Liturgical", "Fragrance"],
    "relic": ["Relics", "Pilgrimage", "Holy Objects"],
    "rosary": ["Prayer Beads", "Devotional", "Marian"],
    "cord": ["Devotional"],
    "scapular": ["Devotional", "Marian", "Consecration"],
    "monstrance": ["Eucharistic", "Liturgical"],
    "eucharistic_host": ["Eucharistic", "Liturgical"]
}
ALL_CATEGORIES = sorted({c for v in ITEM_CATEGORIES.values() for c in v})

# ---------- UTILITIES ----------
def humanize(key: str) -> str:
    return key.replace("_", " ").title()

def first_existing(stem: Path) -> Path | None:
    for ext in EXTS:
        p = stem.with_suffix(ext)
        if p.exists():
            return p
    return None

def multiple_existing(stem: Path, max_images=3):
    results = []
    candidates = [stem] + [stem.parent / f"{stem.name}_{i}" for i in range(1, max_images)]
    for candidate in candidates:
        p = first_existing(candidate)
        if p:
            results.append(p)
    return results

def read_bytes(path: Path) -> bytes | None:
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception:
        return None

def to_data_uri(p: Path, data: bytes) -> str:
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"

def img_data_uri(path: Path | None, fallback: Path | None) -> str:
    if path:
        data = read_bytes(path)
        if data:
            return to_data_uri(path, data)
    if fallback:
        fb = read_bytes(fallback)
        if fb:
            return f"data:image/jpeg;base64,{base64.b64encode(fb).decode('utf-8')}"
    return ""

def hires_for(original_path: Path | None) -> Path | None:
    """
    Try to locate a higher-resolution alternative near the original:
    name_hires, name_full, name@2x, name_large (same extension priority order).
    Falls back to original if none found.
    """
    if not original_path:
        return None
    stem = original_path.with_suffix("")
    suffix_candidates = [f"{stem}", f"{stem}_hires", f"{stem}_full", f"{stem}@2x", f"{stem}_large"]
    for base in suffix_candidates:
        for ext in EXTS:
            p = Path(str(base)).with_suffix(ext)
            if p.exists():
                return p
    return original_path

# ---------- BACKGROUND ----------
bg_file = first_existing(ASSETS_DIR / "background")
ph_file = first_existing(ASSETS_DIR / "placeholder")
bg_uri = img_data_uri(bg_file, ph_file)

# ---------- STYLES ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Cinzel+Decorative:wght@700&display=swap');

.stApp {{
  background-image: linear-gradient(rgba(10,10,20,0.55), rgba(10,10,20,0.55)), url('{bg_uri}');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  min-height: 200vh;
}}

h1.app-title {{
  font-family: 'IM Fell English SC', 'Cinzel Decorative', serif;
  text-align: center;
  color: #fff;
  text-shadow: 0 2px 10px rgba(0,0,0,0.6);
  letter-spacing: 0.5px;
  margin: 10px 0 24px 0;
  font-size: 2.4rem;
}}

section.main > div.block-container {{
  padding-top: 1.0rem;
  padding-bottom: 4.0rem;
}}

.sac-card {{
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 22px;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}}

.sac-img {{
  width: 100%;
  display: block;
  border-radius: 12px;
  transition: transform .3s ease, filter .3s ease, box-shadow .3s ease;
  box-shadow: 0 0 0 rgba(255,255,255,0);
  cursor: zoom-in;
}}
.sac-img:hover {{
  transform: scale(1.08);
  filter: brightness(1.06);
  box-shadow: 0 14px 34px rgba(255,255,220,0.3);
}}

div[data-testid="stExpander"] > details {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}}
div[data-testid="stExpander"] summary {{
  color: #fff;
  font-weight: 700;
}}
div[data-testid="stExpander"] p, div[data-testid="stExpander"] div p {{
  color: #f2f2f2;
  line-height: 1.5;
  margin-bottom: 0.8rem;
}}

/* ---- Modal Lightbox (CSS-driven; no JS needed) ---- */
.lb-toggle {{ display: none; }}

.lb-open-btn {{
  margin-top: 10px;
  display: inline-block;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.35);
  color: #fff;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
  text-decoration: none;
  font-weight: 600;
}}
.lb-open-btn:hover {{
  filter: brightness(1.06);
  transform: translateY(-1px);
}}

.lb-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.85);
  backdrop-filter: blur(2px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}}
.lb-inner {{
  position: relative;
  max-width: 96vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.lb-img {{
  max-width: 96vw;
  max-height: 90vh;
  border-radius: 10px;
  box-shadow: 0 10px 40px rgba(0,0,0,.6);
}}
.lb-close {{
  position: absolute;
  top: -48px;
  right: 0;
  font-size: 26px;
  background: rgba(255,255,255,0.22);
  border: 1px solid rgba(255,255,255,0.35);
  color: #fff;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
}}
/* Show overlay when checkbox is checked */
.lb-toggle:checked + label.lb-open-btn + .lb-overlay {{
  display: flex;
}}
@media (max-width: 768px) {{
  .lb-close {{ top: -44px; }}
}}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='app-title'>Catholic Sacramentals</h1>", unsafe_allow_html=True)

# ---------- SIDEBAR: Search / View / Categories ----------
st.sidebar.subheader("Explore")
view_mode = st.sidebar.radio("View Mode", ["Grid", "Timeline"], index=0)
search_query = st.sidebar.text_input("Search sacramentals…", "").strip().lower()
selected_categories = st.sidebar.multiselect("Filter by category", ALL_CATEGORIES, default=[])

def matches_filters(key: str) -> bool:
    ok_search = True
    if search_query:
        text = (humanize(key) + " " + DESC.get(key, "")).lower()
        ok_search = search_query in text
    ok_cat = True
    if selected_categories:
        item_cats = ITEM_CATEGORIES.get(key, [])
        ok_cat = any(c in item_cats for c in selected_categories)
    return ok_search and ok_cat

# Determine display order
order = ITEM_KEYS if view_mode == "Grid" else [k for k in TIMELINE if k in ITEM_KEYS]
DISPLAY_KEYS = [k for k in order if matches_filters(k)]

# ---------- Collect all image URIs per item (for potential JS lightbox / future use) ----------
def uris_for_item(item_key: str):
    paths = multiple_existing(ASSETS_DIR / item_key, max_images=3)
    out = []
    for p in paths:
        hi = hires_for(p)
        out.append(img_data_uri(hi, ph_file))
    if not out and ph_file:
        out = [img_data_uri(ph_file, ph_file)]
    return out
all_item_uris = {k: uris_for_item(k) for k in ITEM_KEYS}

# ---------- GRID / TIMELINE ----------
cols = st.columns(3, gap="large") if view_mode == "Grid" else [st]

for idx, key in enumerate(DISPLAY_KEYS):
    col = cols[idx % 3] if view_mode == "Grid" else cols[0]
    with col:
        images = multiple_existing(ASSETS_DIR / key, max_images=3)
        st.markdown('<div class="sac-card">', unsafe_allow_html=True)

        selected_idx = 0
        if images:
            if len(images) > 1:
                selected_idx = st.radio(
                    "", list(range(len(images))),
                    horizontal=True, label_visibility="collapsed", key=f"radio_{key}"
                )
                show_path = images[selected_idx]
            else:
                show_path = images[0]
            hires_path = hires_for(show_path)
            img_uri = img_data_uri(hires_path, ph_file)
            tooltip = FACTS.get(key, humanize(key))
            st.markdown(
                f'<img src="{img_uri}" alt="{humanize(key)}" class="sac-img" '
                f'data-group="{key}" data-index="{selected_idx}" data-fact="{tooltip}" title="{tooltip}"/>',
                unsafe_allow_html=True
            )
        else:
            if ph_file:
                ph_uri = img_data_uri(ph_file, ph_file)
                tooltip = FACTS.get(key, humanize(key))
                st.markdown(
                    f'<img src="{ph_uri}" alt="{humanize(key)}" class="sac-img" '
                    f'data-group="{key}" data-index="0" data-fact="{tooltip}" title="{tooltip}"/>',
                    unsafe_allow_html=True
                )

        # Modal Lightbox (CSS-driven): open with a button; enlarge selected image only
        # Unique per-item checkbox id
        lb_id = f"lb_{key}"
        current_img_uri = (img_data_uri(hires_for(images[selected_idx]), ph_file)
                           if images else (img_data_uri(ph_file, ph_file) if ph_file else ""))

        st.markdown(
            f'''
            <input type="checkbox" id="{lb_id}" class="lb-toggle"/>
            <label for="{lb_id}" class="lb-open-btn">🔍 View {humanize(key)}</label>
            <div class="lb-overlay">
              <div class="lb-inner">
                <label for="{lb_id}" class="lb-close">✕</label>
                <img class="lb-img" src="{current_img_uri}" alt="{humanize(key)}"/>
              </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

        with st.expander(humanize(key), expanded=False):
            text = DESC.get(key, "Description coming soon.")
            for para in text.split("\n"):
                if para.strip():
                    st.write(para.strip())

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- LEGACY LIGHTBOX COMPONENT (kept; harmless). Can be used for future JS needs ----------
images_json = json.dumps(all_item_uris)
st.components.v1.html(f"""
<div id="lightbox-overlay" style="display:none"></div>
<script>
// Reserved for future JS-based lightbox; current app uses CSS lightbox.
</script>
""", height=10)
