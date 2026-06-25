import random

WASTE_INFO = {

    "plastic": {

        "emoji": "🟡",

        "color": "#FFD700",

        "impact": "🔴 High",

        "bin": "♻ Plastic Recycling Bin",

        "facts": [

            "Around 11 million metric tons of plastic enter the oceans every year.",

            "Plastic pollution harms marine life and can break down into tiny microplastics.",

            "Many plastic items remain in the environment for hundreds of years.",

            "Reducing single-use plastics helps protect wildlife and ecosystems.",

            "Choosing reusable alternatives can significantly reduce plastic waste."

        ],

        "tips": [

            "Carry reusable shopping bags.",

            "Use reusable water bottles.",

            "Avoid single-use plastics whenever possible.",

            "Recycle clean plastic waste."

        ]
    },

    "paper": {

        "emoji":"🔵",

        "color":"#4DA6FF",

        "impact":"🟢 Low",

        "bin":"📄 Paper Recycling Bin",

        "facts":[

            "Recycling paper helps conserve forests and reduces the need for fresh wood pulp.",

            "Paper can often be recycled several times before its fibers become too short.",

            "Producing recycled paper generally uses less energy than making new paper."

        ],

        "tips":[

            "Recycle clean and dry paper.",

            "Print only when necessary.",

            "Reuse notebooks and paper whenever possible."

        ]
    },

    "glass": {

        "emoji":"🟣",

        "color":"#9B59B6",

        "impact":"🟢 Low",

        "bin":"🍾 Glass Recycling Bin",

        "facts":[

            "Glass can be recycled repeatedly without losing quality.",

            "Recycling glass saves raw materials and energy.",

            "Clean glass is easier to recycle than contaminated glass."

        ],

        "tips":[

            "Recycle bottles and jars.",

            "Handle broken glass carefully.",

            "Separate glass from general waste."

        ]
    },

    "metal": {

        "emoji":"⚫",

        "color":"#808080",

        "impact":"🟡 Medium",

        "bin":"🥫 Metal Recycling Bin",

        "facts":[

            "Recycling aluminum saves a significant amount of energy compared with producing new aluminum.",

            "Metal can often be recycled many times without losing quality.",

            "Recycling metal reduces the need for mining."

        ],

        "tips":[

            "Recycle beverage cans.",

            "Keep metal waste clean.",

            "Separate metal from mixed waste."

        ]
    },

    "battery": {

        "emoji":"🔴",

        "color":"#E74C3C",

        "impact":"☠ Hazardous",

        "bin":"🔋 E-Waste Collection Center",

        "facts":[

            "Batteries contain hazardous materials that should not enter regular landfills.",

            "Improper battery disposal can contaminate soil and groundwater.",

            "Rechargeable batteries help reduce waste over time."

        ],

        "tips":[

            "Never throw batteries into household trash.",

            "Use authorized e-waste collection points.",

            "Choose rechargeable batteries when practical."

        ]
    },

    "organic": {

        "emoji":"🟢",

        "color":"#2ECC71",

        "impact":"🟢 Low",

        "bin":"🌿 Compost Bin",

        "facts":[

            "Organic waste can be composted into nutrient-rich fertilizer.",

            "Separating food waste helps reduce landfill methane emissions.",

            "Composting returns nutrients to the soil."

        ],

        "tips":[

            "Compost fruit and vegetable waste.",

            "Avoid mixing organic waste with recyclables.",

            "Use compost to improve garden soil."

        ]
    },

    "textile": {

        "emoji":"🟤",

        "color":"#8B4513",

        "impact":"🟡 Medium",

        "bin":"👕 Textile Recycling / Donation",

        "facts":[

            "Extending the life of clothing reduces environmental impact.",

            "Many textiles can be donated or recycled instead of being discarded.",

            "Repairing garments helps reduce waste."

        ],

        "tips":[

            "Donate wearable clothes.",

            "Repair before replacing.",

            "Use textile recycling programs."

        ]
    }

}

def get_waste_info(class_name):
    info = WASTE_INFO[class_name.lower()]

    return {
        "emoji":info["emoji"],
        "color":info["color"],
        "impact":info["impact"],
        "bin":info["bin"],
        "fact":random.choice(info["facts"]),
        "tips":info["tips"]
    }
