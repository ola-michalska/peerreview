import requests
import json

#display songs
def get_songs():
    response = requests.get("http://127.0.0.1:5000/songs")
    if response.ok:
        return  response.json()
    return []

def add_song(rank_id, name, artist, genre):
    song = {
        "rank_id": rank_id,
        "name": name,
        "artist": artist,
        "genre": genre
    }
    response = requests.post("http://127.0.0.1:5000/add-song", json=song)
    return response.json()

def delete_song(rank_id):
    response = requests.delete(f"http://127.0.0.1:5000/delete-song/{rank_id}")
    return response.json()

def display_songs(songs):
    for song in songs:
        print(f"{song[0]}. {song[1]} by {song[2]} | Genre: {song[3]}")

def run():
    print("======================================")
    print("Welcome to the Music Ranking System!")
    print("======================================")

    print("Please select one of the following options:")
    print("1 - View Ranked Songs")
    print("2 - Add a song")
    print("3 - Delete a song by rank number")
    option = input("Enter 1,2, or 3: ")
    print("======================================")

    if option == "1":
        print("You've selected Option 1: View Ranked Songs")
        songs = get_songs()
        display_songs(songs)

    elif option == "2":
        print("You've selected Option 2: Add a song")
        print("Please enter the new song's details below")
        rank = input("Rank: ")
        name = input("Name: ")
        artist = input("Artist: ")
        genre = input("genre: ")
        add_song(rank, name, artist, genre)
        print("Song successfully added!")

        # Show updated rankings
        print("======================================")
        print("Updated Song Rankings:")
        songs = get_songs()
        display_songs(songs)

    elif option == "3":
        print("You've selected Option 3: Delete a song")
        song_to_delete = input("Please enter the song's rank to delete it: ")
        delete_song(song_to_delete)
        print("Song successfully deleted!")

        # Show updated rankings
        print("======================================")
        print("Updated Song Rankings:")
        songs = get_songs()
        display_songs(songs)

    else:
        print("Whoops! Invalid choice!!")

if __name__ == "__main__":
    run()