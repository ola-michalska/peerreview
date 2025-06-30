from flask import Flask, jsonify, request
from db_utils import get_all_books_db, get_book_by_title_db, get_book_by_author_db, \
    get_book_by_genre_db, add_new_user_db, add_book_to_user_db, get_user_db, get_book_by_id_db, \
    delete_user_by_id_db

app = Flask(__name__)


@app.route('/books')
def get_books():
    res = get_all_books_db()
    return jsonify(res)

# http://127.0.0.1:5001/books


@app.route('/title/<title>')
def get_by_title(title):
    res = get_book_by_title_db(title)
    return jsonify(res)

# http://127.0.0.1:5001/books/<title>

@app.route('/author/<author>')
def get_by_author(author):
    res = get_book_by_author_db(author)
    return jsonify(res)

# http://127.0.0.1:5001/author/<author>

@app.route('/genre/<genre>')
def get_by_genre(genre):
    res = get_book_by_genre_db(genre)
    return jsonify(res)

# http://127.0.0.1:5001/genre/<genre>

@app.route('/id/<book_id>')
def get_by_id(book_id):
    res = get_book_by_id_db(book_id)
    return jsonify(res)

# http://127.0.0.1:5001/id/<book_id>


@app.route("/user/add", methods=["POST"])
def new_user():
    new_user_dict = request.get_json()
    return jsonify(add_new_user_db(new_user_dict))

# http://127.0.0.1:5001/user/add

@app.route('/user/<user_name>')
def get_user(user_name):
    res = get_user_db(user_name)
    return jsonify(res)

# http://127.0.0.1:5001/user/<user_name>


@app.route("/user_book/add", methods=["POST"])
def add_book_to_user():
    user_book_dict = request.get_json()
    return jsonify(add_book_to_user_db(user_book_dict))

# http://127.0.0.1:5001/user_book/add

@app.route("/users/remove/<user_id>", methods=["DELETE"])
def del_user_by_id(user_id):
    return jsonify(delete_user_by_id_db(user_id))




if __name__ == '__main__':
    app.run(debug=True, port=5001)