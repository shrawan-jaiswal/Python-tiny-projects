LeoMessi = {
    "Intermiami" : {
        "Jersey_no" : 10,
        "Coach" : "Tata Martino",
        "Color" : "Pink",
    },
    "PSG" : {
        "Jersey_no" : 30,
        "Coach" : "Ernesto Valverde",
        "Color" : "Blue",
    },
}

for club, details in LeoMessi.items():
    print(f"\nClub:{club}")
    Jersey = f"{details["Jersey_no"]}"
    Manager = f"{details["Coach"]}"
    Color = f"{details["Color"]}"

    print(f"Jersey_no: {Jersey}")
    print(f"Manager: {Manager}")
    print(f"Color: {Color}")
    
