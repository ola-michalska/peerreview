from traceback import print_tb

import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

#create our own class of db connection errors
class DBConnError(Exception):
    pass

#try connect to db
def connect_db():
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return conn


#get all songs in order
def get_all_songs():
    db_conn = None
    try:
        db_conn = connect_db()
        cur = db_conn.cursor()
        print("Connected to database")

        query = """
        SELECT rank_id, name, artist, genre, added_date 
        FROM song_rank
        ORDER BY rank_id ASC; 
        """

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception:
        raise DBConnError("Failed to read data from database :(")

    finally:
        if db_conn:
            db_conn.close()
            print("Database connection is closed")
    return []

#add new song to ranking
def add_song(rank_id, name, artist, genre):
    try:
        db_conn = connect_db()
        cur = db_conn.cursor()
        print("Connected to database! :)")

        # ON DUPLICATE KEY means if rank_id exists, update it, or else add new entry
        query = """
        INSERT INTO song_rank (rank_id, name, artist, genre)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        name = VALUES(name),
        artist = VALUES(artist),
        genre = VALUES(genre);
        """

        cur.execute(query, (rank_id, name, artist, genre))
        db_conn.commit()
        print(f"Your song {name} was successfully added!")
        cur.close()

    except Exception:
        raise DBConnError("Failed to add new song...sorry!")

    finally:
        if db_conn:
            db_conn.close()
            print("Database connection is closed.")


def delete_song(rank_id):
    try:
        db_conn = connect_db()
        cur = db_conn.cursor()
        print("Connected to database! :)")

        query = """
        DELETE FROM song_rank 
        WHERE rank_id = %s;
        """

        cur.execute(query, (rank_id,))
        db_conn.commit()

        rows_deleted = cur.rowcount  # number of affected rows
        cur.close()

        if rows_deleted > 0:
            print(f"Song of rank {rank_id} was successfully deleted")
            return True
        else:
            print(f"No song found with rank {rank_id} to delete")
            return False

    except Exception as e:
        print(f"Error deleting song: {e}")
        # Optionally, handle or log the exception properly here
        return False

    finally:
        if db_conn:
            db_conn.close()
            print(f"Database connection is closed.")

