favorite_places = {
    "Adrián": ["barcelona", "madrid", "valencia", 1],
    "Andra": ["la rioja", "galicia", "asturias", 2],
}

for key, value in favorite_places.items():
    print(key.title())
    for item in value:
        print(f"\t{item}")
