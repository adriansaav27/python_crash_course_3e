def make_album(artist_name, album_name, number_of_songs=None):
    desciption = album_name
    if number_of_songs != None:
        desciption = f"{album_name} ({number_of_songs})"
    return {artist_name: desciption}


print(make_album("Rosalía", "Motomami"))
print(make_album("C. Tangana", "Madrileño"))
print(make_album("Aitana", "alpha"))
print(make_album("Taylor Swift", "Speak now", 10))
