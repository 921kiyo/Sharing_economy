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
    },
    {
        "name": "Albert Einstein",
        "sex": "m",
        "age": 76,
        "country": "USA",
        "city": "Philadelphia",
        "longitude": -75.165222,
        "latitude": 39.952583,
    },
    {
        "name": "Alexander the Great",
        "sex": "m",
        "age": 32,
        "country": "Greece",
        "city": "Athens",
        "longitude": 23.727539,
        "latitude": 37.983810,
    },
    {
        "name": "Oda Nobunaga",
        "sex": "m",
        "age": 48,
        "country": "Japan",
        "city": "Tokyo",
        "longitude": 139.839478,
        "latitude": 35.652832,
    },
    {
        "name": "Florence Nightingale",
        "sex": "f",
        "age": 90,
        "country": "England",
        "city": "London",
        "longitude": -0.118092,
        "latitude": 51.509865,
    },
]


PRODUCT_LISTINGS = {

    "John Von Neumann": [
        {
            "id": 1,
            "name": "Navy Blue Peacoat",
            "url": "https://static-mercariapp-uk.akamaized.net/photos/m59397082818_1.jpg?1540043962",
            "description": "Smooth navy blue Peacoat. Suitable for any aspiring computer scientist.",
            "price": 26,  # Dollars
            "condition": "Good",
            "size": "L",
            "shipping_cost": 4
        },
        {
            "id": 2,
            "name": "Denim Shirt",
            "url": "https://static-mercariapp-uk.akamaized.net/photos/m31249014654_1.jpg?1540040441",
            "description": "Men's suave denim shirt. Super cool worker look.",
            "price": 10,  # Dollars
            "condition": "New",
            "size": "L",
            "shipping_cost": 0
        },
    ],
    "Albert Einstein": [
        {
            "id": 3,
            "name": "Incredible Supreme Jumper",
            "url": "https://ae01.alicdn.com/kf/HTB1Fj2gJVXXXXcqXVXXq6xXFXXXb/Supreme-Sweatshirts-Casual-Hoodies-Brand-Clothing-Couples-Clothes-Men-Women-Tops-Fashion-Moleton-Feminino-Einstein-funny.jpg",
            "description": "Comfortable jumper with an incredibly handsome man on it.",
            "price": 64,  # Dollars
            "condition": "Like New",
            "size": "M",
            "shipping_cost": 1
        },
        {
            "id": 4,
            "name": "Stylish Men's Shorts",
            "url": "https://images.express.com/is/image/expressfashion/0026_03532966_0713?cache=on&wid=361&fmt=jpeg&qlt=75,1&resmode=sharp2&op_usm=1,1,5,0&defaultImage=Photo-Coming-Soon",
            "description": "Great for the beach!",
            "price": 22,  # Dollars
            "condition": "Poor",
            "size": "XL",
            "shipping_cost": 5
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


