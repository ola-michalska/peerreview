from flask import Flask, jsonify, request
from db_utils import get_all_songs, add_song, delete_song

app = Flask(__name__)

# ENDPOINT FOR VIEWING SONG RANKING
@app.route('/songs')
def get_songs():
    songs = get_all_songs()
    return jsonify(songs)

# http://127.0.0.1:5000/songs

# ENDPOINT FOR ADDING SONGS
@app.route('/add-song', methods=["POST"]) #POST cannot be done via browser, only main.py script client
def add_song_flask():
    data = request.get_json()

    rank_id = data["rank_id"]
    name = data["name"]
    artist = data["artist"]
    genre = data["genre"]

    result = add_song(rank_id, name, artist, genre)

    if result:
        return jsonify({'message': "Song added!!"})
    else:
        return jsonify({'message': "Song not added :("}), 400

# ENDPOINT FOR DELETING SONGS
@app.route("/delete-song/<int:rank_id>", methods=["DELETE"]) #DELETE cannot be done via browser, only main.py script client
def delete_song_flask(rank_id):
    result = delete_song(rank_id)

    if result:
        return jsonify({'message': "Song deleted!!"})
    else:
        return jsonify({'message': "Song could not be delted :("}), 400

if __name__ == "__main__":
    app.run(debug=True)

