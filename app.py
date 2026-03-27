from flask import Flask, render_template
import sqlite3
import qrcode
import os

app = Flask(__name__)

# ---------------- CONFIG ----------------
MYSQL_PASSWORD = "Sush@#14321*"

QR_FOLDER = "static/qr"
os.makedirs(QR_FOLDER, exist_ok=True)

# ---------------- MYSQL CONNECTION (NO DATABASE) ----------------
def get_db_connection():
    conn = sqlite3.connect('tree_aadhaar.db')
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- CREATE DATABASE & TABLE ----------------
def setup_database():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS trees (
            id VARCHAR(20) PRIMARY KEY,
            common_name VARCHAR(100),
            scientific_name VARCHAR(150),
            origin VARCHAR(100),
            lifespan VARCHAR(50),
            location VARCHAR(255),
            address VARCHAR(255),
            benefits TEXT,
            image VARCHAR(100)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

# ---------------- MYSQL CONNECTION (WITH DATABASE) ----------------

def get_db_connection():
    conn = sqlite3.connect('tree_aadhaar.db')
    conn.row_factory = sqlite3.Row
    return conn
# ---------------- INSERT TREE DATA ----------------
def ensure_tree_exists():
    conn = get_db_connection()
    cur = conn.cursor()

    # 🌴 CARYOTA URENS
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - ORN - 01",))
    if not cur.fetchone():
        cur.execute("""
            INSERT INTO trees (
                id, common_name, scientific_name, origin,
                lifespan, location, address, benefits, image
            ) VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            "SPMVV - ORN - 01",
            "Fishtail Palm",
            "Caryota urens",
            "India and Sri Lanka",
            "40–50 years",
            "https://maps.google.com/?q=13.615680396365784,79.39501707600789",
            "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
            "Produces palm jaggery\nImproves air quality\nOrnamental value\nPrevents soil erosion",
            "caryota_urens.jpg"
        ))

    # 🌿 NEEM TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 01",))
    if not cur.fetchone():
        cur.execute("""
            INSERT INTO trees (
                id, common_name, scientific_name, origin,
                lifespan, location, address, benefits, image
            ) VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            "SPMVV - MED - 01",
            "Neem",
            "Azadirachta indica",
            "Indian Subcontinent",
            "150–200 years",
            "https://maps.google.com/?q=13.616602108791563,79.39692835682624",
            "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
            "Leaves - Cure allergies and skin problems\nStem (twigs) - Keep teeth and gums healthy\nBark - Helps reduce fever and infections\nFlowers - Help in digestion\nSeeds (oil) - Cure skin and hair problems",
            "neem.jpg"
        ))

        # 🌴 FOXTAIL PALM 
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - ORN - 02",))
    if not cur.fetchone():
        cur.execute("""
            INSERT INTO trees (
                id, common_name, scientific_name, origin,
                lifespan, location, address, benefits, image
            ) VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            "SPMVV - ORN - 02",
            "Foxtail Palm",
            "Wodyetia bifurcata",
            "Australia",
            "20–30 years",
            " https://maps.google.com/?q=13.615745640147683,79.39506231750512",
            "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
            "Ornamental landscaping\nFast growing\nLow maintenance\nImproves air quality",
            "foxtail_palm.jpg"
        ))

        # 🌲 ARAUCARIACEAE TREE (NORFOLK ISLAND PINE)
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - ORN - 03",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - ORN - 03",
        "Norfolk Island Pine",
        "Araucaria heterophylla",
        "Norfolk Island (Australia)",
        "100–150 years",
        "https://maps.google.com/?q=13.618346972402614, 79.4007744513943",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Help in improving air quality and provide fresh environment\nBark - Used in minor traditional applications\nWood - Used for light construction and making decorative items\nOrnamental - Widely used for decoration and landscaping",
        "araucaria.jpg"
    ))

    # 🌳 MONOON LONGIFOLIUM (ASHOKA TREE)
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - ORN - 04",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - ORN - 04",
        "Ashoka Tree",
        "Monoon longifolium",
        "India and Sri Lanka",
        "50–80 years",
        "https://maps.google.com/?q=13.617610407215684,79.4007039529227",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Help in treating skin problems and allergies\nBark - Strengthens uterus and helps in menstrual problems\nFlowers - Help in controlling blood sugar and improving health\nStem - Reduces pain and inflammation\nRoots - Help in digestive problems like piles and diarrhea",
        "ashoka.jpg"
    ))

    # 🌳 BADAM TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 01",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - FRT - 01",
        "Badam Tree",
        "Terminalia catappa",
        "India and Southeast Asia",
        "40–60 years",
        "https://maps.google.com/?q=13.618735179297488,79.3993905592841",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves – Help in skin problems and reduce swelling\nBark – Helps cure fever and infections\nFruits – Good for health and give energy\nSeeds (almonds) – Good for brain and body strength\nRoots – Help in stomach problems",
        "badam.jpg"
    ))

    # 🌳 MANGO TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 02",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - FRT - 02",
        "Mango Tree",
        "Mangifera indica",
        "India",
        "100+ years",
        "https://maps.google.com/?q=13.6181106341823,79.3970289374755",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Help in controlling diabetes and improving digestion\nBark - Used for treating skin problems and infections\nFruits - Rich in vitamins and improve immunity and health",
        "mango.jpg"
    ))

    # 🌳 VELAGA TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 03",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - FRT - 03",
        "Velaga Tree",
        "Aegle marmelos",
        "India",
        "50–100 years",
        "https://maps.google.com/?q=13.618194,79.397917",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Help in managing diabetes and improving digestion\nFruits - Boost immunity and improve overall health\nPulp - Helps in curing diarrhea and detoxifying body\nLeaves extract - Helps in respiratory problems and reducing inflammation",
        "velaga.jpg"
    ))

    # 🌳 TEAK TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 01",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        "SPMVV - TIM - 01",
        "Teak Tree",
        "Tectona grandis",
        "India and Southeast Asia",
        "80–100 years",
        "https://maps.google.com/?q=13.618044419977826,79.39892036152743",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Used in treating skin problems and headaches\nBark - Helps in digestive issues and infections\nWood - Strong and durable used for furniture and construction\nSeeds - Used in traditional medicine for health benefits",
        "teak.jpg"
    ))

    # 🌳 STERCULIA FOETIDA TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 02",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "SPMVV - TIM - 02",
        "Jungle Almond Tree",
        "Sterculia foetida",
        "Tropical regions of Asia and Australia",
        "60-80 years",
        "https://maps.google.com/?q=13.61585776479455,79.39530752579779",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Used in traditional medicine to reduce swelling\nBark - Helps in treating skin infections and wounds\nSeeds (oil) - Used for industrial oil and sometimes for skin applications\nWood - Used for light construction and making utility items\nShade - Provides good shade in hot areas",
        "sterculia_foetida.jpg"
    ))

    # 🌳 AMLA TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 02",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - MED - 02",
    "Amla Tree",
    "Phyllanthus emblica",
    "India and Southeast Asia",
    "50-70 years",
    "https://maps.google.com/?q=13.615731681518477,79.39560251169299",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Fruits - Rich in Vitamin C and boosts immunity\nLeaves - Help in improving digestion and gut health\nSeeds - Support hair growth and strength\nBark - Used in traditional medicine for treatments\nFruits pulp - Keeps skin healthy and glowing",
    "amla.jpg"
))


# 🌳 BAKUL TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 03",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - MED - 03",
    "Bakul Tree",
    "Mimusops elengi",
    "India and Southeast Asia",
    "50-80 years",
    "https://maps.google.com/?q=13.615861312281313,79.39581017506002",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Leaves - Help in treating skin problems and wounds\nBark - Strengthens teeth and gums and helps in dental care\nFlowers - Support heart health and improve circulation\nFruits - Help in digestion and treating diarrhea\nSeeds - Help in managing blood sugar levels",
    "bakul.jpg"
))

# 🌳 RED SANDALWOOD TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 03",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - TIM - 03",
    "Red Sandalwood Tree",
    "Pterocarpus santalinus",
    "India",
    "100-150 years",
    "https://maps.google.com/?q=13.616523016815119,79.39699265277308",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Wood - Used for skin care and treating acne and pigmentation\nPowder - Helps in anti-aging and improving skin glow\nBark - Used for wound healing and reducing inflammation\nHeartwood - Helps in blood sugar control and improves circulation\nLeaves - Help in treating infections and respiratory problems",
    "redsandal.jpg"
))


# 🌳 PEEPAL TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 04",))
    if not cur.fetchone():
        cur.execute("""
        INSERT INTO trees (
            id, common_name, scientific_name, origin,
            lifespan, location, address, benefits, image
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "SPMVV - MED - 04",
        "Raavi Chettu",
        "Ficus religiosa",
        "India",
        "100-150 years",
        "https://maps.google.com/?q=13.617940548266168,79.39701360079378",
        "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
        "Leaves - Help in treating respiratory problems like cough and asthma\nBark - Used for digestive issues like diarrhea and constipation\nFruits - Help in managing blood sugar levels\nRoots - Strengthen gums and improve oral health\nLeaves extract - Helps in healing wounds and skin problems",
        "peepal.jpg"
))

# 🌳 PLUMERIA ALBA TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - ORN - 05",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - ORN - 05",
    "Deva Ganneru",
    "Plumeria alba",
    "Tropical America",
    "40-60 years",
    "https://maps.google.com/?q=13.618041253475255,79.39826873015885",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Leaves - Help in treating skin infections and wounds\nBark - Used for digestive problems like diarrhea and constipation\nFlowers - Reduce stress and improve mental well-being\nLatex - Helps in healing cuts and minor burns\nRoots - Help in reducing inflammation and pain",
    "plumeria.jpg"
))

# 🌳 PALMYRA PALM TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 04",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - FRT - 04",
    "Taati Chettu",
    "Borassus flabellifer",
    "India and Southeast Asia",
    "80-100 years",
    "https://maps.google.com/?q=13.616836689488888,79.39837068320054",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Fruits - Rich in vitamins and boost immunity\nSap - Acts as natural coolant and detoxifies body\nPulp - Helps in digestion and skin health\nJaggery - Helps in controlling blood sugar levels\nRoots - Improve digestion and support weight management",
    "palmyra.jpg"
))

# 🌳 JAMMI CHETTU
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 05",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - MED - 05",
    "Jammi Chettu",
    "Prosopis cineraria",
    "India",
    "50-100 years",
    "https://maps.google.com/?q=13.616380452756264,79.39833050102182",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Leaves - Help in treating respiratory problems like asthma and bronchitis\nBark - Used for skin diseases and wound healing\nFruits - Help in digestion and treating diarrhea\nSeeds - Help in managing diabetes\nRoots - Improve immunity and purify blood",
    "jammi.jpg"
))

# 🌳 BAMBOO TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 04",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - TIM - 04",
    "Veduru",
    "Dendrocalamus longispathus",
    "India and Southeast Asia",
    "30-50 years",
    "https://maps.google.com/?q=13.615900671387857,79.40003418630637",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Shoots - Edible and provide nutrition\nCulms - Used for construction, furniture and crafts\nLeaves - Contain antioxidants and improve health\nRoots - Help in soil conservation and prevent erosion\nWhole plant - Used for paper production and eco-friendly materials",
    "bamboo.jpg"
))

# 🌳 MAHUA TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 06",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - MED - 06",
    "Ippa Chettu",
    "Madhuca longifolia",
    "India",
    "60-80 years",
    "https://maps.google.com/?q=13.61605957269735,79.40026247516333",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Flowers - Rich in nutrients and boost energy and immunity\nBark - Helps in controlling diabetes and improving heart health\nSeeds (oil) - Used for pain relief and reducing inflammation\nFlowers extract - Helps in digestion and protects liver\nOil - Useful for skin care and wound healing",
    "mahua.jpg"
))

# 🌳 TAMARIND TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 05",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - FRT - 05",
    "Chintha Chettu",
    "Tamarindus indica",
    "India and Africa",
    "100-150 years",
    "https://maps.google.com/?q=13.616609340671204,79.40161984239265",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Fruits - Help in improving digestion and relieving constipation\nLeaves - Reduce inflammation and help in wound healing\nSeeds - Help in managing blood sugar levels\nPulp - Improves heart health and reduces cholesterol\nFruits - Rich in vitamins and boost immunity",
    "tamarind.jpg"
))

# 🌳 BANYAN TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 05",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - TIM - 05",
    "Marri Chettu",
    "Ficus benghalensis",
    "India",
    "200+ years",
    "https://maps.google.com/?q=13.616480565968553,79.40144691863972",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Twigs - Used for oral health and strengthening teeth\nAerial roots - Help in hair growth and treating skin problems\nBark - Used for treating diabetes and digestive issues\nLatex - Helps in healing wounds and skin infections\nLeaves - Improve immunity and reduce inflammation",
    "banyan.jpg"
))

# 🌳 PRACAXI TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - TIM - 06",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - TIM - 06",
    "Noone Vruksham",
    "Pentaclethra macroloba",
    "Amazon Rainforest (South America)",
    "60-100 years",
    "https://maps.google.com/?q=13.617910523002166,79.40113340004508",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Seeds (oil) - Helps in skin care and reduces scars and stretch marks\nOil - Used for healing wounds and reducing inflammation\nOil - Strengthens hair and improves hair growth\nSeeds - Have antibacterial and antifungal properties\nTree - Helps in soil improvement and environmental restoration",
    "pracaxi.jpg"
))

# 🌳 COCONUT TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 06",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - FRT - 06",
    "Kobbari Chettu",
    "Cocos nucifera",
    "Tropical regions",
    "60-80 years",
    "https://maps.google.com/?q=13.618649305651147,79.40050031075764",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Water - Hydrates body and provides electrolytes\nFruit - Rich in nutrients and gives energy\nOil - Helps in skin care and hair growth\nHusk - Used for making ropes, mats and eco-products\nLeaves - Used for shelter and traditional uses",
    "coconut.jpg"
))

# 🌳 JAMUN TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - FRT - 07",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - FRT - 07",
    "Neredu Chettu",
    "Syzygium cumini",
    "India",
    "50-100 years",
    "https://maps.google.com/?q=13.61746431072797,79.39991000733907",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Fruits - Help in controlling diabetes and improving digestion\nSeeds - Help in reducing blood sugar levels\nBark - Used for treating diarrhea and digestive problems\nLeaves - Improve oral health and kill bacteria\nFruits - Rich in antioxidants and boost immunity",
    "jamun.jpg"
))

# 🌳 KAPOK TREE
    cur.execute("SELECT id FROM trees WHERE id=?", ("SPMVV - MED - 07",))
    if not cur.fetchone():
        cur.execute("""
    INSERT INTO trees (
        id, common_name, scientific_name, origin,
        lifespan, location, address, benefits, image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "SPMVV - MED - 07",
    "Booruga Chettu",
    "Ceiba pentandra",
    "Tropical regions",
    "60-100 years",
    "https://maps.google.com/?q=13.617426723181781,79.40010848496632",
    "Sri Padmavati Mahila Visvavidyalayam, Tirupati",
    "Fiber - Used for making pillows, mattresses and insulation\nSeeds (oil) - Used for cooking and soap making\nBark - Helps in treating digestive problems and inflammation\nRoots - Have medicinal uses and help in detoxification\nTree - Helps in soil conservation and supports biodiversity",
    "kapok.jpg"
))
    conn.commit()
    cur.close()
    conn.close()

    # ---------------- QR GENERATION ----------------
    tree_ids = ["SPMVV - ORN - 01", "SPMVV - MED - 01", "SPMVV - ORN - 02", "SPMVV - ORN - 03", "SPMVV - ORN - 04", "SPMVV - FRT - 01", "SPMVV - FRT - 02", "SPMVV - FRT - 03","SPMVV - TIM - 01", "SPMVV - TIM - 02","SPMVV - MED - 02", "SPMVV - MED - 03", "SPMVV - TIM - 03", "SPMVV - MED - 04", "SPMVV - ORN - 05", "SPMVV - FRT - 04", "SPMVV - MED - 05", "SPMVV - TIM - 04", "SPMVV - MED - 06", "SPMVV - FRT - 05", "SPMVV - TIM - 05", "SPMVV - TIM - 06", "SPMVV - FRT - 06", "SPMVV - FRT - 07", "SPMVV - MED - 07"]
    BASE_URL = "https://tree-aadhaar-e13a.onrender.com"

    for tree_id in tree_ids:
        qr_path = f"{QR_FOLDER}/{tree_id}.png"

        if not os.path.exists(qr_path):
            qr_url = f"{BASE_URL}/tree/{tree_id}"
            qr = qrcode.make(qr_url)
            qr.save(qr_path)

# ---------------- INITIAL SETUP ----------------
setup_database()
ensure_tree_exists()

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return f"""
    <h2 style='text-align:center;color:#2e7d32;'>🌳 Tree Aadhaar System 🌳</h2>

    <div style='text-align:center; margin-top:20px;'>

        <a href='/tree/SPMVV - ORN - 01' style='
            background:linear-gradient(45deg,#43a047,#2e7d32);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌴 Caryota Tree
        </a>

        <a href='/tree/SPMVV - MED - 01' style='
            background:linear-gradient(45deg,#1b5e20,#66bb6a);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌿 Neem Tree
        </a>

        <a href='/tree/SPMVV - ORN - 02' style='
            background:linear-gradient(45deg,#6d4c41,#8d6e63);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌴 Foxtail Palm
        </a>

        <a href='/tree/SPMVV - ORN - 03' style='
            background:linear-gradient(45deg,#2e7d32,#66bb6a);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌲 Araucariaceae Tree
        </a>

        <a href='/tree/SPMVV - ORN - 04' style='
            background:linear-gradient(45deg,#1b5e20,#43a047);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌳 Ashoka Tree
        </a>

        <a href='/tree/SPMVV - FRT - 01' style='
            background:linear-gradient(45deg,#8d6e63,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌳 Badam Tree
        </a>

        <a href='/tree/SPMVV - FRT - 02' style='
            background:linear-gradient(45deg,#f57c00,#ffb74d);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🥭 Mango Tree
        </a>

        <a href='/tree/SPMVV - FRT - 03' style='
            background:linear-gradient(45deg,#2e7d32,#81c784);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌳 Velaga Tree
        </a>

        <a href='/tree/SPMVV - TIM - 01' style='
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;'>
            🌳 Teak Tree
        </a>

        <a href="/tree/SPMVV - TIM - 02" style="
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Sterculia foetida
        </a>

        <a href="/tree/SPMVV - MED - 02" style="
            background:linear-gradient(45deg,#2e7d32,#81c784);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Amla Tree
        </a>

        <a href="/tree/SPMVV - MED - 03" style="
            background:linear-gradient(45deg,#2e7d32,#66bb6a);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Bakul Tree
        </a>

        <a href="/tree/SPMVV - TIM - 03" style="
            background:linear-gradient(45deg,#8b0000,#c62828);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Red Sandalwood Tree
        </a>

        <a href="/tree/SPMVV - MED - 04" style="
            background:linear-gradient(45deg,#2e7d32,#66bb6a);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Raavi Chettu
        </a>

        <a href="/tree/SPMVV - ORN - 05" style="
            background:linear-gradient(45deg,#f5f5f5,#ffd54f);
            color:black;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Deva Ganneru Tree
        </a>

        <a href="/tree/SPMVV - FRT - 04" style="
            background:linear-gradient(45deg,#795548,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Taati Chettu
        </a>

        <a href="/tree/SPMVV - MED - 05" style="
            background:linear-gradient(45deg,#6d4c41,#8d6e63);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Jammi Chettu
        </a>

        <a href="/tree/SPMVV - TIM - 04" style="
            background:linear-gradient(45deg,#2e7d32,#81c784);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Veduru
        </a>

        <a href="/tree/SPMVV - MED - 06" style="
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Ippa Chettu
        </a>

        <a href="/tree/SPMVV - FRT - 05" style="
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
                    display:inline-block;">
            🌳 Chintha Chettu
        </a>

        <a href="/tree/SPMVV - TIM - 05" style="
            background:linear-gradient(45deg,#2e7d32,#66bb6a);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Marri Chettu
        </a>

        <a href="/tree/SPMVV - TIM - 06" style="
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Pracaxi Vruksham
        </a>

        <a href="/tree/SPMVV - FRT - 06" style="
            background:linear-gradient(45deg,#2e7d32,#81c784);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Kobbari Chettu
        </a>

        <a href="/tree/SPMVV - FRT - 07" style="
            background:linear-gradient(45deg,#4e342e,#8d6e63);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Neredu Chettu
        </a>

        <a href="/tree/SPMVV - MED - 07" style="
            background:linear-gradient(45deg,#6d4c41,#a1887f);
            color:white;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            font-weight:bold;
            font-size:18px;
            margin:10px;
            display:inline-block;">
            🌳 Booruga Chettu
        </a>

    </div>
    """

# ---------------- TREE CARD PAGE ----------------
@app.route("/tree/<tree_id>")
def tree_card(tree_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM trees WHERE id=?", (tree_id,))
    tree = cur.fetchone()
    cur.close()
    conn.close()

    if not tree:
        return "Tree not found in database"

    return render_template("tree_card.html", tree=tree)

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)