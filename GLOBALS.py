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
        "donating": True
    },
    {
        "name": "Albert Einstein",
        "sex": "m",
        "age": 76,
        "country": "USA",
        "city": "Philadelphia",
        "longitude": -75.165222,
        "latitude": 39.952583,
        "donating": True
    },
    {
        "name": "Alexander the Great",
        "sex": "m",
        "age": 32,
        "country": "Greece",
        "city": "Athens",
        "longitude": 23.727539,
        "latitude": 37.983810,
        "donating": False
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
            "description": "Fashioned from the Kinloch Anderson 1925 “Travelling Ulster” this classic pea coat has been adapted for modern living and is made from the finest 100% Wool Melton cloth."
                           "This jacket is beautifully finished with complementing Kinloch Anderson satin lining and beautiful silk Kinloch Anderson Tartan piping on the inside."
                           "The coat benefits from two front flap pockets lined with Kinloch Anderson silk tartan and two internal chest pockets.FalseThe front can be buttoned to the neck or left open and complemented with a cashmere scarf for blustery weather.",
            "price": 201,  # Dollars
            "condition": "Good",
            "size": "L",
            "shipping_cost": 4
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
            "price": 10,  # Dollars
            "condition": "New",
            "size": "L",
            "shipping_cost": 0
        },
        {
            "id": 3,
            "name": "Me on a T-shirt",
            "url": "img3",
            "description": "Tight fit v-neck, light blue T-shirt with a black and white portrait of me and my name emblazoned underneath. 100% cotton t-shirt. Excellent printing quality",
            "price": 6,  # Dollars
            "condition": "New",
            "size": "XL",
            "shipping_cost": 1
        },
    ],
    "Albert Einstein": [
        {
            "id": 4,
            "name": "Mens Check Vintage Herringbone Tweed Charcoal Grey 3 Piece Suit",
            "url": "img4",
            "description": "Mens Tweed Check Vintage 3 Piece Suit. Complete With Blazer, Trouser & Waistcoat polyester blend. Textured Tweed Material with Velvet Trim, Fitted Design"
                           "Great For Smart Formal Occasions Weddings, Parties, Proms.",
            "price": 209.99,  # Dollars
            "condition": "Like New",
            "size": "M",
            "shipping_cost": 10
        },
        {
            "id": 5,
            "name": "Stylish Men's Shorts",
            "url": "img5",
            "description": "These shorts are very comfortable. They are a nice easy shorts to to wear for a social gathering or just lounge around. Comfortable elastic waistband. Mock fly (No opening)."
                           "67% cotton, 33% polyester.",
            "price": 22.30,  # Dollars
            "condition": "Good",
            "size": "M",
            "shipping_cost": 3
        },
        {
            "id": 6,
            "name": "The Barber Wool Blend Trilby Fedora Hat",
            "url": "img6",
            "description": "The Barber Wool Blend Trilby Fedora Hat by Goorin Bros features a stylish monochromatic look in a rich coffee-brown tweed fabric. "
                           "Adorned with a simple self-fabric hat band outlined in contrast blue stitching, The Barber Fedora is finished with a small Goorin Bros side pin and striped fabric lining. Casual, comfortable and relaxed, The Barber is a great everyday style to rock all fall and winter long. ",
            "price": 35,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 3
        },

    ],
    "Sakamoto Ryouma": [
        {
            "id": 7,
            "name": "Hoshi Kabuto Helmet",
            "url": "img7",
            "description": "Edo period helmet with riveted pointed nail ribs. The suji or ribs are riveted with pointed nails. "
                           "This gives the helmet its exceptional changing reflection. On the top is a large round hole (tehen) edged with a curved iron plate. "
                           "Large antlers (kuwagata) and a five-piece neck-guard (shikoro) with indigo-blue cords. The fukigaeshi is decorated with an unidentified crest."
                           "Suitable for any aspiring or seasoned warrior.",
            "price": 300,  # Dollars
            "condition": "Good",
            "size": "M",
            "shipping_cost": 10
        },
        {
            "id": 8,
            "name": "Geta Sandals - Scorched Kiri",
            "url": "img8",
            "description": "These high-quality geta are made from scorched kiri (paulownia), giving them a nice aged look, with a black felt strap. "
                           "Wearing them takes a bit of getting used to but they are ideal for cosplay or just for gaining a bit of height!",
            "price": 125,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 5
        },
        {
            "id": 9,
            "name": "Traditional Japanese Men Yukata Kimono Vintage Samurai Robe OBI Cotton Blue",
            "url": "img9",
            "description": "Japanese long Yukata Kimono Robe. Top quality, authentic 100% cotton. Primary Color: Blue",
            "price": 44.99,  # Dollars
            "condition": "Poor",
            "size": "M",
            "shipping_cost": 7
        },
    ]


}


CHARITY_INFO = [
    {
        "name": "Against Malaria Foundation",
        "mission": "We help protect people from malaria. We fund anti-malaria nets, specifically long-lasting insecticidal nets (LLINs), and work with distribution partners to ensure they are used. We track and report on net use and malaria case data.",
        "url": "https://www.againstmalaria.com/default.aspx"
    },
    {
        "name": "Bill & Melinda Gates Foundation",
        "mission": "We seek to unlock the possibility inside every individual. We see equal value in all lives. And so we are dedicated to improving the quality of life for individuals around the world. From the education of students in Chicago, to the health of a young mother in Nigeria, we are catalysts of human promise everywhere.",
        "url": "https://www.gatesfoundation.org"
    }
]


