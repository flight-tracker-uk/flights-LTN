"""London Luton Airport (LTN) destinations — April 2026."""

DESTINATIONS = {
    "LTN": {
        "name": "London Luton",
        "routes": {
            # UK & Ireland
            "ABZ": "Aberdeen",
            "BFS": "Belfast",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "GLA": "Glasgow",
            "INV": "Inverness",
            "IOM": "Isle of Man",
            "JER": "Jersey",
            "KIR": "Kerry",
            "NOC": "Knock",
            "ORK": "Cork",
            # Spain (Mainland)
            "AGP": "Malaga",
            "ALC": "Alicante",
            "BCN": "Barcelona",
            "GRO": "Girona",
            "MAD": "Madrid",
            "RMU": "Murcia",
            "REU": "Reus",
            "SVQ": "Seville",
            # Balearic Islands
            "IBZ": "Ibiza",
            "MAH": "Menorca",
            "PMI": "Palma de Majorca",
            # Canary Islands
            "ACE": "Lanzarote",
            "FUE": "Fuerteventura",
            "LPA": "Gran Canaria",
            "TFS": "Tenerife South",
            # Italy
            "BLQ": "Bologna",
            "BGY": "Milan Bergamo",
            "CTA": "Catania",
            "FCO": "Rome Fiumicino",
            "NAP": "Naples",
            "OLB": "Olbia (Sardinia)",
            "PMO": "Palermo",
            "PSA": "Pisa",
            "TRN": "Turin",
            "VCE": "Venice Marco Polo",
            "VRN": "Verona",
            # France
            "BOD": "Bordeaux",
            "BZR": "Beziers",
            "CDG": "Paris Charles de Gaulle",
            "GNB": "Grenoble",
            "LYS": "Lyon",
            "NCE": "Nice",
            # Germany
            "BER": "Berlin",
            "DTM": "Dortmund",
            "MUC": "Munich",
            # Greece
            "ATH": "Athens",
            "CFU": "Corfu",
            "CHQ": "Chania",
            "HER": "Heraklion (Crete)",
            "JMK": "Mykonos",
            "JSI": "Skiathos",
            "KGS": "Kos",
            "PVK": "Preveza",
            "RHO": "Rhodes",
            "ZTH": "Zakynthos (Zante)",
            # Portugal
            "FAO": "Faro",
            "FNC": "Madeira",
            "LIS": "Lisbon",
            "OPO": "Porto",
            # Turkey
            "ADB": "Izmir",
            "AYT": "Antalya",
            "BJV": "Bodrum",
            "DLM": "Dalaman",
            "IST": "Istanbul",
            # Poland
            "BZG": "Bydgoszcz",
            "GDN": "Gdansk",
            "KRK": "Krakow",
            "KTW": "Katowice",
            "LUZ": "Lublin",
            "POZ": "Poznan",
            "RZE": "Rzeszow",
            "SZY": "Szczytno",
            "WAW": "Warsaw",
            "WRO": "Wroclaw",
            # Romania
            "BCM": "Bacau",
            "CLJ": "Cluj-Napoca",
            "CND": "Constanta",
            "CRA": "Craiova",
            "GHV": "Brasov",
            "IAS": "Iasi",
            "OTP": "Bucharest",
            "SBZ": "Sibiu",
            "SCV": "Suceava",
            "SUJ": "Satu Mare",
            "TGM": "Targu Mures",
            "TSR": "Timisoara",
            # Austria & Switzerland
            "BSL": "Basel",
            "GVA": "Geneva",
            "INN": "Innsbruck",
            "SZG": "Salzburg",
            "ZRH": "Zurich",
            # Eastern Europe & Balkans
            "BEG": "Belgrade",
            "BOJ": "Burgas",
            "BTS": "Bratislava",
            "BUD": "Budapest",
            "DEB": "Debrecen",
            "KIV": "Chisinau",
            "KSC": "Kosice",
            "KUN": "Kaunas",
            "PDV": "Plovdiv",
            "PRG": "Prague",
            "PRN": "Pristina",
            "PUY": "Pula",
            "SJJ": "Sarajevo",
            "SKP": "Skopje",
            "SOF": "Sofia",
            "SPU": "Split",
            "TAT": "Poprad",
            "TBS": "Tbilisi",
            "TIA": "Tirana",
            "TIV": "Tivat",
            "TLL": "Tallinn",
            "VAR": "Varna",
            "VNO": "Vilnius",
            # Netherlands
            "AMS": "Amsterdam",
            # Scandinavia & Nordics
            "KEF": "Reykjavik",
            "RVN": "Rovaniemi",
            "TOS": "Tromso",
            # Cyprus
            "LCA": "Larnaca",
            "PFO": "Paphos",
            # North Africa
            "AGA": "Agadir",
            "DJE": "Djerba",
            "NBE": "Enfidha",
            "RAK": "Marrakech",
            # Middle East & Egypt
            "AMM": "Amman",
            "CAI": "Cairo",
            "HRG": "Hurghada",
            "SPX": "Giza",
            "SSH": "Sharm El Sheikh",
            "TLV": "Tel Aviv",
            # Malta
            "MLA": "Malta",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
