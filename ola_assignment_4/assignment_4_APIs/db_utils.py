import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return cnx

def get_all_books_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM books"""
        cur.execute(query)
        result = cur.fetchall()
        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_user_db(user_name):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM users
        WHERE user_name = '{}'
            """.format(user_name)
        cur.execute(query)
        result = cur.fetchall()
        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_book_by_title_db(title):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """
            SELECT  *
            FROM books 
            WHERE title = '{}'
            """.format(title)

        cur.execute(query)

        result = cur.fetchall()
        print(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result

def get_book_by_author_db(author):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """
            SELECT  *
            FROM books 
            WHERE author = '{}'
            """.format(author)

        cur.execute(query)

        result = cur.fetchall()
        print(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result

def get_book_by_genre_db(genre):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """
            SELECT  *
            FROM books 
            WHERE genre = '{}'
            """.format(genre)

        cur.execute(query)

        result = cur.fetchall()
        print(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result

def get_book_by_id_db(book_id):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """
            SELECT  *
            FROM books 
            WHERE book_id = '{}'
            """.format(book_id)

        cur.execute(query)

        result = cur.fetchall()
        print(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result

def add_new_user_db(new_user_dict):
    db_connection = None

    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = f"""
         INSERT INTO users (user_name)
         VALUES ('{new_user_dict['user_name']}')
         """
        cur.execute(query)

        db_connection.commit()

        print("User added successfully!")

        result = cur.fetchall()

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def add_book_to_user_db(user_book_dict):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        print("ADD THIS book to the user TO DB:", user_book_dict)

        query = f"""
        UPDATE users
        SET rented_book = '{user_book_dict['rented_book']}'
        WHERE user_name = '{user_book_dict['user_name']}'
        """

        cur.execute(query)

        db_connection.commit()

        print("book added successfully!")

        result = cur.fetchall()

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def delete_user_by_id_db(user_id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM users WHERE user_id = {}""".format(user_id)
        cur.execute(del_query)

        db_connection.commit()

        print(f"Record with user_id {user_id} deleted successfully.")

        remaining_records = cur.fetchall()
        cur.close()

        return remaining_records


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == '__main__':
    ...