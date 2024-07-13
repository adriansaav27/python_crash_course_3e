cities = {
    "barcelona" : [ "spain", 1_600_000 ],
    "munich" : [ "germany", 1_400_000 ],
    "roma" : [ "italy", 2_800_000 ]
}

for key, value in cities.items():
    print(f"{key.title()}")
    for item in value:
        print(item)
    print("\n")