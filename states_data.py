"""
Rich destination data for the Bharat Yatra AI travel planner.
Each entry includes description, highlights, best time, budget,
and curated Unsplash image URLs.
"""

INDIA_STATES = {
    "Kashmir": {
        "full_name": "Jammu & Kashmir",
        "tagline": "Heaven on Earth",
        "description": (
            "Nestled in the lap of the Himalayas, Kashmir enchants with its "
            "pristine Dal Lake, snow-dusted peaks, lush meadows of Gulmarg, "
            "and the timeless beauty of Mughal gardens. Shikaras glide "
            "across mirror-still waters while walnut and chinar trees paint "
            "the valleys in autumn gold."
        ),
        "highlights": [
            "Dal Lake houseboat stay",
            "Gulmarg gondola & skiing",
            "Pahalgam valley trek",
            "Mughal Gardens — Shalimar & Nishat",
            "Sonamarg glacier trail",
        ],
        "best_time": "March – October",
        "budget": "₹25,000 – ₹60,000 per person (5 days)",
        "capital": "Srinagar",
        "images": [
            "https://images.unsplash.com/photo-1597074866923-dc0589150458?w=600&q=80",
            "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=600&q=80",
        ],
    },
    "Rajasthan": {
        "full_name": "Rajasthan",
        "tagline": "Land of Kings",
        "description": (
            "Rajasthan is a living tapestry of golden forts, ornate havelis, "
            "vibrant bazaars, and endless Thar desert dunes. From the pink "
            "walls of Jaipur to the blue lanes of Jodhpur and the romantic "
            "lakes of Udaipur, every city tells a royal tale. Camel safaris "
            "under star-lit skies and folk music around bonfires make it "
            "unforgettable."
        ),
        "highlights": [
            "Jaipur — Amber Fort & Hawa Mahal",
            "Udaipur — City Palace & Lake Pichola",
            "Jaisalmer — Sam sand dunes & camel safari",
            "Jodhpur — Mehrangarh Fort",
            "Ranthambore — Tiger safari",
        ],
        "best_time": "October – March",
        "budget": "₹20,000 – ₹55,000 per person (7 days)",
        "capital": "Jaipur",
        "images": [
            "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=600&q=80",
            "https://images.unsplash.com/photo-1477587458883-47145ed94245?w=600&q=80",
        ],
    },
    "Kerala": {
        "full_name": "Kerala",
        "tagline": "God's Own Country",
        "description": (
            "Kerala unfolds as a lush green paradise where coconut palms "
            "sway over tranquil backwaters, tea plantations carpet misty "
            "hills, and Ayurvedic traditions heal body and soul. Cruise on "
            "a kettuvallam through Alleppey, spot elephants at Periyar, or "
            "watch the sunset from Varkala's crimson cliffs."
        ),
        "highlights": [
            "Alleppey backwater houseboat",
            "Munnar tea gardens & Eravikulam NP",
            "Varkala & Kovalam beaches",
            "Periyar Wildlife Sanctuary",
            "Kathakali dance performances",
        ],
        "best_time": "September – March",
        "budget": "₹18,000 – ₹50,000 per person (5 days)",
        "capital": "Thiruvananthapuram",
        "images": [
            "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=600&q=80",
            "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=600&q=80",
        ],
    },
    "Goa": {
        "full_name": "Goa",
        "tagline": "Beach Paradise",
        "description": (
            "India's pocket-sized paradise blends sun-kissed beaches with "
            "Portuguese colonial charm. From the vibrant shacks of Baga "
            "to the serene sands of Palolem, Goa offers laid-back vibes, "
            "fresh seafood, centuries-old churches, spice plantations, and "
            "a nightlife scene that pulses till dawn."
        ),
        "highlights": [
            "Baga & Calangute beach life",
            "Old Goa — Basilica of Bom Jesus",
            "Dudhsagar waterfalls",
            "Palolem & Agonda beaches",
            "Spice plantation tours",
        ],
        "best_time": "November – February",
        "budget": "₹15,000 – ₹40,000 per person (4 days)",
        "capital": "Panaji",
        "images": [
            "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=600&q=80",
            "https://images.unsplash.com/photo-1587922546307-776227941871?w=600&q=80",
        ],
    },
    "Ladakh": {
        "full_name": "Ladakh",
        "tagline": "Land of High Passes",
        "description": (
            "A stark, lunar landscape of barren mountains, turquoise lakes, "
            "and ancient Buddhist monasteries perched on cliff edges. Ladakh "
            "is the ultimate frontier — where Pangong Lake changes colours "
            "by the hour, Nubra Valley's sand dunes surprise at 10,000 ft, "
            "and Khardung La stands among the world's highest motorable passes."
        ),
        "highlights": [
            "Pangong Tso lake",
            "Nubra Valley & Diskit monastery",
            "Khardung La pass",
            "Hemis & Thiksey monasteries",
            "Magnetic Hill & Zanskar rafting",
        ],
        "best_time": "June – September",
        "budget": "₹30,000 – ₹70,000 per person (7 days)",
        "capital": "Leh",
        "images": [
            "https://images.unsplash.com/photo-1626015365107-84e7e4e1f244?w=600&q=80",
            "https://images.unsplash.com/photo-1621996659490-3275b4d0d951?w=600&q=80",
        ],
    },
    "Varanasi": {
        "full_name": "Uttar Pradesh — Varanasi",
        "tagline": "Spiritual Capital of India",
        "description": (
            "One of the oldest continuously inhabited cities on Earth, "
            "Varanasi is where life and death merge along the sacred Ganges. "
            "Witness the hypnotic Ganga Aarti at Dashashwamedh Ghat, lose "
            "yourself in the labyrinthine alleys, savor the famous Banarasi "
            "paan and kachori, and feel centuries of devotion in every stone."
        ),
        "highlights": [
            "Ganga Aarti at Dashashwamedh Ghat",
            "Sunrise boat ride on the Ganges",
            "Kashi Vishwanath Temple",
            "Sarnath — Buddha's first sermon",
            "Banarasi silk weaving",
        ],
        "best_time": "October – March",
        "budget": "₹12,000 – ₹30,000 per person (3 days)",
        "capital": "Varanasi",
        "images": [
            "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=600&q=80",
            "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=600&q=80",
        ],
    },
    "Himachal": {
        "full_name": "Himachal Pradesh",
        "tagline": "Mountain Magic",
        "description": (
            "Apple orchards, deodar forests, roaring rivers, and snow-capped "
            "peaks — Himachal is India's mountain playground. Whether you're "
            "paragliding over Bir Billing, trekking through Hampta Pass, "
            "relaxing in Manali's hot springs, or soaking in Shimla's "
            "colonial charm, the hills never disappoint."
        ),
        "highlights": [
            "Manali — Solang Valley & Rohtang",
            "Shimla — Mall Road & heritage rail",
            "Dharamshala & McLeod Ganj",
            "Spiti Valley road trip",
            "Bir Billing paragliding",
        ],
        "best_time": "March – June, Oct – Dec",
        "budget": "₹15,000 – ₹45,000 per person (5 days)",
        "capital": "Shimla",
        "images": [
            "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=600&q=80",
            "https://images.unsplash.com/photo-1585136917228-44d4ee9e050a?w=600&q=80",
        ],
    },
    "Tamil Nadu": {
        "full_name": "Tamil Nadu",
        "tagline": "Temple Trail",
        "description": (
            "Tamil Nadu is the cradle of Dravidian civilization, home to "
            "awe-inspiring gopurams that pierce the sky, the shore temples "
            "of Mahabalipuram, the French quarter of Pondicherry, and the "
            "cool Nilgiri hills of Ooty. Classical Bharatanatyam, filter "
            "coffee, and Chettinad cuisine add cultural richness."
        ),
        "highlights": [
            "Meenakshi Temple, Madurai",
            "Mahabalipuram shore temples",
            "Pondicherry — French Quarter",
            "Ooty & Nilgiri Mountain Railway",
            "Rameswaram — Pamban Bridge",
        ],
        "best_time": "November – February",
        "budget": "₹15,000 – ₹40,000 per person (5 days)",
        "capital": "Chennai",
        "images": [
            "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=600&q=80",
            "https://images.unsplash.com/photo-1621778706924-4b546e4f0b21?w=600&q=80",
        ],
    },
    "North East": {
        "full_name": "North East India — Seven Sisters",
        "tagline": "Unexplored Paradise",
        "description": (
            "India's best-kept secret — eight states of rolling green hills, "
            "living root bridges, pristine rivers, vibrant tribal festivals, "
            "and rhino-dotted grasslands. Meghalaya's Cherrapunji is among "
            "the wettest places on Earth, while Kaziranga shelters the one-horned "
            "rhino. Every state has its own distinct culture and cuisine."
        ),
        "highlights": [
            "Kaziranga NP — One-horned rhino",
            "Cherrapunji — Living root bridges",
            "Tawang monastery, Arunachal",
            "Loktak Lake, Manipur",
            "Hornbill Festival, Nagaland",
        ],
        "best_time": "October – April",
        "budget": "₹25,000 – ₹65,000 per person (7 days)",
        "capital": "Guwahati (gateway)",
        "images": [
            "https://images.unsplash.com/photo-1622308644420-2275cf5b8e21?w=600&q=80",
            "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?w=600&q=80",
        ],
    },
    "Andaman": {
        "full_name": "Andaman & Nicobar Islands",
        "tagline": "Island Paradise",
        "description": (
            "Crystal-clear turquoise waters, white sand beaches, coral reefs "
            "teeming with marine life, and lush tropical forests — the Andaman "
            "Islands are India's answer to the Maldives. Dive at Havelock, "
            "explore the cellular jail's poignant history, and kayak through "
            "bioluminescent waters at night."
        ),
        "highlights": [
            "Radhanagar Beach, Havelock",
            "Scuba diving & snorkeling",
            "Cellular Jail, Port Blair",
            "Neil Island — natural bridge",
            "Bioluminescent kayaking",
        ],
        "best_time": "November – April",
        "budget": "₹30,000 – ₹65,000 per person (5 days)",
        "capital": "Port Blair",
        "images": [
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&q=80",
            "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600&q=80",
        ],
    },
    "Gujarat": {
        "full_name": "Gujarat",
        "tagline": "Land of Legends",
        "description": (
            "From the white salt desert of the Rann of Kutch glowing under "
            "a full moon to the majestic Gir — the last refuge of Asiatic "
            "lions — Gujarat blends heritage, wildlife, and vibrant culture. "
            "The step-wells of Adalaj, the temples of Dwarka, and Ahmedabad's "
            "street food scene are unmissable."
        ),
        "highlights": [
            "Rann of Kutch — white desert",
            "Gir National Park — Asiatic lions",
            "Somnath & Dwarka temples",
            "Statue of Unity",
            "Ahmedabad heritage walk",
        ],
        "best_time": "October – March",
        "budget": "₹18,000 – ₹45,000 per person (5 days)",
        "capital": "Gandhinagar",
        "images": [
            "https://images.unsplash.com/photo-1609948543911-7f9c5f937180?w=600&q=80",
            "https://images.unsplash.com/photo-1590080876351-941da357b4cf?w=600&q=80",
        ],
    },
    "Karnataka": {
        "full_name": "Karnataka",
        "tagline": "One State, Many Worlds",
        "description": (
            "Karnataka spans ancient Hampi's boulder-strewn ruins, Coorg's "
            "misty coffee estates, Mysore's illuminated palace, and the "
            "pristine beaches of Gokarna. The Western Ghats harbour rich "
            "biodiversity, while Bangalore pulses as India's tech capital "
            "with a thriving café and craft-beer culture."
        ),
        "highlights": [
            "Hampi — UNESCO ruins",
            "Mysore Palace & Chamundi Hills",
            "Coorg — coffee plantations",
            "Gokarna beaches",
            "Jog Falls",
        ],
        "best_time": "October – February",
        "budget": "₹15,000 – ₹40,000 per person (5 days)",
        "capital": "Bengaluru",
        "images": [
            "https://images.unsplash.com/photo-1600100397608-e4e0cfddee25?w=600&q=80",
            "https://images.unsplash.com/photo-1570458436416-b8fcccfe883f?w=600&q=80",
        ],
    },
    "Uttarakhand": {
        "full_name": "Uttarakhand",
        "tagline": "Land of the Gods",
        "description": (
            "Known as Dev Bhoomi, Uttarakhand is where sacred rivers are born "
            "and ancient temples dot every hillside. Trek to the Valley of "
            "Flowers, raft the Ganges at Rishikesh, seek blessings at "
            "Kedarnath, or simply lose yourself in the silence of Jim "
            "Corbett's forests listening for a tiger's call."
        ),
        "highlights": [
            "Rishikesh — rafting & yoga",
            "Kedarnath & Badrinath temples",
            "Valley of Flowers trek",
            "Jim Corbett National Park",
            "Nainital & Mussoorie hill stations",
        ],
        "best_time": "March – June, Sep – Nov",
        "budget": "₹15,000 – ₹45,000 per person (5 days)",
        "capital": "Dehradun",
        "images": [
            "https://images.unsplash.com/photo-1606210122158-eeb10e0a3101?w=600&q=80",
            "https://images.unsplash.com/photo-1588083949404-c4f1ed1323b3?w=600&q=80",
        ],
    },
    "Punjab": {
        "full_name": "Punjab",
        "tagline": "Land of Five Rivers",
        "description": (
            "Punjab pulses with warmth, from the golden glow of the Harmandir "
            "Sahib (Golden Temple) reflecting in its sacred pool to the "
            "Wagah Border ceremony's electric energy. Amritsar's culinary "
            "trail — butter chicken, amritsari kulcha, lassi — is reason "
            "enough to visit."
        ),
        "highlights": [
            "Golden Temple, Amritsar",
            "Wagah Border ceremony",
            "Jallianwala Bagh memorial",
            "Amritsar street food trail",
            "Anandpur Sahib",
        ],
        "best_time": "October – March",
        "budget": "₹12,000 – ₹30,000 per person (3 days)",
        "capital": "Chandigarh",
        "images": [
            "https://images.unsplash.com/photo-1609947017136-9dab4b23bcb1?w=600&q=80",
            "https://images.unsplash.com/photo-1588096344356-9b4ccb9da0eb?w=600&q=80",
        ],
    },
    "Odisha": {
        "full_name": "Odisha",
        "tagline": "Soul of Incredible India",
        "description": (
            "Odisha's cultural depth is unmatched — from the Sun Temple of "
            "Konark and Jagannath Puri to the tribal heartlands of Koraput "
            "and the pristine Chilika Lake, Asia's largest brackish-water "
            "lagoon. The annual Rath Yatra is a spectacle of devotion that "
            "draws millions."
        ),
        "highlights": [
            "Konark Sun Temple — UNESCO",
            "Jagannath Temple, Puri",
            "Chilika Lake — Irrawaddy dolphins",
            "Tribal village tours",
            "Puri beach & sand art festival",
        ],
        "best_time": "October – March",
        "budget": "₹12,000 – ₹35,000 per person (4 days)",
        "capital": "Bhubaneswar",
        "images": [
            "https://images.unsplash.com/photo-1590080875515-8a3a8dc5735e?w=600&q=80",
            "https://images.unsplash.com/photo-1621996659490-3275b4d0d951?w=600&q=80",
        ],
    },
}

NEIGHBOURS = {
    "Nepal": {
        "flag": "🇳🇵",
        "tagline": "Himalayan Trails",
        "description": (
            "Home to eight of the world's ten tallest peaks including Everest, "
            "Nepal offers world-class trekking, ancient temples in Kathmandu "
            "Valley, and Lumbini — the birthplace of Buddha."
        ),
        "highlights": ["Everest Base Camp trek", "Kathmandu & Bhaktapur",
                        "Pokhara & Phewa Lake", "Chitwan safari", "Lumbini"],
        "best_time": "Oct – Dec, March – May",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=600&q=80",
    },
    "Sri Lanka": {
        "flag": "🇱🇰",
        "tagline": "Pearl of the Indian Ocean",
        "description": (
            "A compact island brimming with ancient ruins, emerald tea "
            "highlands, golden beaches, and leopard-roaming national parks."
        ),
        "highlights": ["Sigiriya rock fortress", "Kandy — Temple of Tooth",
                        "Ella train ride", "Yala leopard safari", "Galle Fort"],
        "best_time": "Dec – March (west), May – Sep (east)",
        "image": "https://images.unsplash.com/photo-1586015553444-b147e614ce6d?w=600&q=80",
    },
    "Bhutan": {
        "flag": "🇧🇹",
        "tagline": "Last Shangri-La",
        "description": (
            "The world's only carbon-negative country, Bhutan measures "
            "Gross National Happiness. Tiger's Nest monastery, dzongs, "
            "and untouched Himalayan valleys make it magical."
        ),
        "highlights": ["Tiger's Nest (Paro Taktsang)", "Punakha Dzong",
                        "Thimphu valley", "Bumthang temples", "Dochula Pass"],
        "best_time": "March – May, Sep – Nov",
        "image": "https://images.unsplash.com/photo-1553856622-d1b352e24ec4?w=600&q=80",
    },
    "Maldives": {
        "flag": "🇲🇻",
        "tagline": "Tropical Bliss",
        "description": (
            "A string of 1,200 coral islands with overwater villas, "
            "powder-white beaches, and some of the best diving spots "
            "on the planet."
        ),
        "highlights": ["Overwater villa stay", "Snorkeling with mantas",
                        "Malé fish market", "Bioluminescent beach", "Island hopping"],
        "best_time": "November – April",
        "image": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=600&q=80",
    },
    "Myanmar": {
        "flag": "🇲🇲",
        "tagline": "Golden Pagodas",
        "description": (
            "Ancient Bagan's 2,000+ temples at sunrise, Shwedagon Pagoda's "
            "golden dome, Inle Lake's floating gardens — Myanmar is a land "
            "frozen in time."
        ),
        "highlights": ["Bagan temple sunrise", "Shwedagon Pagoda",
                        "Inle Lake boat tour", "Mandalay Hill", "Golden Rock"],
        "best_time": "November – February",
        "image": "https://images.unsplash.com/photo-1540611025311-01df3cef54b5?w=600&q=80",
    },
    "Bangladesh": {
        "flag": "🇧🇩",
        "tagline": "River Deltas",
        "description": (
            "The Sundarbans mangrove forest — home of the Royal Bengal Tiger — "
            "the world's longest natural beach at Cox's Bazar, and the "
            "Mughal heritage of Old Dhaka."
        ),
        "highlights": ["Sundarbans mangrove safari", "Cox's Bazar beach",
                        "Old Dhaka heritage", "Srimangal tea gardens", "Paharpur ruins"],
        "best_time": "October – March",
        "image": "https://images.unsplash.com/photo-1598219257010-1cabb42bbc42?w=600&q=80",
    },
}
