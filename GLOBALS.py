DATABASE_URL = 'sqlite:///user_product_data.db'

CONTRIBUTION_PERC = 0.03

USERS = [

    {
        "name": "John Von Neumann",
        "sex": "m",
        "age": 73,
        "country": "USA",
        "city": "New York",
        "longitude": -73.935242,
        "latitude": 40.730610,
        "donating": True,
        "charity_id": 1
    },
    {
        "name": "Albert Einstein",
        "sex": "m",
        "age": 76,
        "country": "USA",
        "city": "Philadelphia",
        "longitude": -75.165222,
        "latitude": 39.952583,
        "donating": False,
    },
    {
        "name": "Alexander the Great",
        "sex": "m",
        "age": 32,
        "country": "Greece",
        "city": "Athens",
        "longitude": 23.727539,
        "latitude": 37.983810,
        "donating": True,
        "charity_id": 3
    },
    {
        "name": "Sakamoto Ryouma",
        "sex": "m",
        "age": 48,
        "country": "Japan",
        "city": "Tokyo",
        "longitude": 139.839478,
        "latitude": 35.652832,
        "donating": False
    },
    {
        "name": "Florence Nightingale",
        "sex": "f",
        "age": 90,
        "country": "England",
        "city": "London",
        "longitude": -0.118092,
        "latitude": 51.509865,
        "donating": False
    },
]


PRODUCT_LISTINGS = {

    "John Von Neumann": [
        {
            "id": 1,
            "name": "Navy Blue Peacoat",
            "url": "img1",
            "description": "Fashioned from the Kinloch Anderson 1925 “Travelling Ulster” this classic pea coat has been adapted for modern living and is made from the finest 100% Wool Melton cloth. "
                           "This jacket is beautifully finished with complementing Kinloch Anderson satin lining and beautiful silk Kinloch Anderson Tartan piping on the inside. "
                           "The coat benefits from two front flap pockets lined with Kinloch Anderson silk tartan and two internal chest pockets. The front can be buttoned to the neck or left open and complemented with a cashmere scarf for blustery weather. ",
            "price": 201.00,  # Dollars
            "condition": "Good",
            "size": "L",
            "shipping_cost": 4.00
        },
        {
            "id": 2,
            "name": "Denim Shirt",
            "url": "img2",
            "description": "The Men's Denim Shirt is a classic wardrobe piece, "
                           "and a perfect all-rounder for multiple work day scenarios. "
                           "Pair this shirt with one of our denim aprons for a popular double-denim look, or coordinate with black skinny jeans and sneakers. "
                           "The medium-wash fabric is super soft and breathable, ensuring you remain confident and comfortable in your work wear, "
                           "while modern design features include a button down collar and contrast white buttons for a distinctive fashion edge. ",
            "price": 10.00,  # Dollars
            "condition": "New",
            "size": "L",
            "shipping_cost": 0.00
        },
        {
            "id": 3,
            "name": "Me on a T-shirt",
            "url": "img3",
            "description": "Tight fit v-neck, light blue T-shirt with a black and white portrait of me and my name emblazoned underneath. 100% cotton t-shirt. Excellent printing quality.",
            "price": 6.00,  # Dollars
            "condition": "New",
            "size": "XL",
            "shipping_cost": 1.00
        },
    ],
    "Albert Einstein": [
        {
            "id": 4,
            "name": "Vintage 3 Piece Suit",
            "url": "img4",
            "description": "Mens Tweed Check Vintage 3 Piece Suit. Complete With Blazer, Trouser & Waistcoat polyester blend. Textured Tweed Material with Velvet Trim, Fitted Design. "
                           "Great For Smart Formal Occasions Weddings, Parties, Proms.",
            "price": 210.00,  # Dollars
            "condition": "Like New",
            "size": "M",
            "shipping_cost": 10.00
        },
        {
            "id": 5,
            "name": "Stylish Men's Shorts",
            "url": "img5",
            "description": "These shorts are very comfortable. They are a nice easy shorts to to wear for a social gathering or just lounge around. Comfortable elastic waistband. Mock fly (No opening). "
                           "67% cotton, 33% polyester.",
            "price": 22.30,  # Dollars
            "condition": "Good",
            "size": "M",
            "shipping_cost": 3.00
        },
        {
            "id": 6,
            "name": "Trilby Fedora Hat",
            "url": "img6",
            "description": "The Barber Wool Blend Trilby Fedora Hat by Goorin Bros features a stylish monochromatic look in a rich coffee-brown tweed fabric. "
                           "Adorned with a simple self-fabric hat band outlined in contrast blue stitching, The Barber Fedora is finished with a small Goorin Bros side pin and striped fabric lining. Casual, comfortable and relaxed, The Barber is a great everyday style to rock all fall and winter long. ",
            "price": 35.00,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 3.00
        },

    ],
    "Sakamoto Ryouma": [
        {
            "id": 7,
            "name": "Hoshi Kabuto Helmet",
            "url": "img7",
            "description": "Edo period helmet with riveted pointed nail ribs. The suji or ribs are riveted with pointed nails. "
                           "This gives the helmet its exceptional changing reflection. On the top is a large round hole (tehen) edged with a curved iron plate. "
                           "Large antlers (kuwagata) and a five-piece neck-guard (shikoro) with indigo-blue cords. The fukigaeshi is decorated with an unidentified crest. "
                           "Suitable for any aspiring or seasoned warrior.",
            "price": 300.00,  # Dollars
            "condition": "Good",
            "size": "M",
            "shipping_cost": 10.00
        },
        {
            "id": 8,
            "name": "Geta Sandals - Scorched Kiri",
            "url": "img8",
            "description": "These high-quality geta are made from scorched kiri (paulownia), giving them a nice aged look, with a black felt strap. "
                           "Wearing them takes a bit of getting used to but they are ideal for cosplay or just for gaining a bit of height!",
            "price": 125.00,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 5.00
        },
        {
            "id": 9,
            "name": "Yukata Samurai Robe",
            "url": "img9",
            "description": "Japanese long Yukata Kimono Robe. Top quality, authentic 100% cotton. Primary Color: Blue",
            "price": 44.99,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 7.00
        },
        {
            "id": 10,
            "name": "White T",
            "url": "img10",
            "description": "This t-shirt is light weight and ideal for one off promotional events such as fun runs or charity events. "
                           "These items are suitable for t-shirt printing and transfer applications.",
            "price": 15.00,  # Dollars
            "condition": "Like New",
            "size": "M",
            "shipping_cost": 7.00
        },
    ],
    "Alexander the Great": [
        {
            "id": 11,
            "name": "Gold Plated Helmet",
            "url": "img11",
            "description": "Spartan hoplites were often depicted bearing a transverse horsehair crest on their helmet, which was possibly used to identify officers.[42] In the Archaic period, Spartans were armored with flanged bronze cuirasses, leg greaves, and a helmet, often of the Corinthian type. It is often disputed which torso armor the Spartans wore during the Persian Wars, though it seems likely they either continued to wear bronze cuirasses of a more sculptured type, or instead had adopted the linothōrax. During the later 5th century BC, when warfare had become more flexible and full-scale phalanx confrontations became rarer, the Greeks abandoned most forms of body armor. The Lacedaemonians also adopted a new tunic, the exōmis, which could be arranged so that it left the right arm and shoulder uncovered and free for action in combat",
            "price": 2000.00,  # Dollars
            "condition": "Like New",
            "size": "M",
            "shipping_cost": 10.00
        },
        {
            "id": 12,
            "name": "Grey Converse Shoes",
            "url": "img12",
            "description": "The Converse Chuck 70 Leather delivers a pinstripe upper with a suede tongue and patch for a look inspired by the Converse Crafted Boot.",
            "price": 30.00,  # Dollars
            "condition": "Good",
            "size": "M",
            "shipping_cost": 3.00
        }
    ]
}


CHARITY_INFO = [
    {
        "name": "Against Malaria Foundation",
        "mission": "Malaria kills half a million people every year and 400 million fall ill. Before bed nets were made available, it was three or more times that. Nets are a proven intervention - a more effective a way of saving lives than any other. There is still a long way to go and every death from malaria is preventable. "
                   "We help protect people from malaria. We fund anti-malaria nets, specifically long-lasting insecticidal nets (LLINs), and work with distribution partners to ensure they are used. We track and report on net use and malaria case data.",
        "url": "https://www.againstmalaria.com/default.aspx",
        "media": "charity1"
    },
    {
        "name": "Bill & Melinda Gates Foundation",
        "mission": "We seek to unlock the possibility inside every individual. We see equal value in all lives. And so we are dedicated to improving the quality of life for individuals around the world. From the education of students in Chicago, to the health of a young mother in Nigeria, we are catalysts of human promise everywhere. ",
        "url": "https://www.gatesfoundation.org",
        "media": "charity2"
    },
    {
        "name": "WWF",
        "mission": "WWF’s work has evolved from saving species and landscapes to addressing the larger global threats and forces that impact them. Recognizing that the problems facing our planet are increasingly more complex and urgent, we have refined the way in which we work around an ambitious new strategy. "
                   "Our new strategy puts people at the center and organizes our work around six key areas: forests, marine, freshwater, wildlife, food and climate. By linking these six areas in an integrated approach, we can better leverage our unique assets and direct all our resources to protecting vulnerable places, species and communities worldwide.",
        "url": "https://www.worldwildlife.org/",
        "media": "charity3"
    },
    {
        "name": "Save the Children",
        "mission": "In the U.S. and around the world, we give children a healthy start in life, the opportunity to learn and protection from harm. When crisis strikes, we are always among the first to respond and the last to leave. We do whatever it takes to save children, transforming their lives and the future we share.",
        "url": "https://www.savethechildren.org/",
        "media": "charity4"
    }

]


