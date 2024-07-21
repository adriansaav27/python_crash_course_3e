def make_album(artist_name, album_name, number_of_songs=None):
    desciption = album_name
    if number_of_songs != None:
        desciption = f"{album_name} ({number_of_songs})"
    return {artist_name: desciption}


while True:
    print("Insert 'quit' to exit program :)")

    artist_name = input("Insert the artist name: ")
    if artist_name == "quit":
        break
    album_name = input("Insert the album name: ")
    if album_name == "quit":
        break

    print(make_album(artist_name, album_name))
