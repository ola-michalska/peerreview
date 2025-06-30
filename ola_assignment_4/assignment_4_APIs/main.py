import json
import requests
from prettytable import from_db_cursor
from assignment_4_APIs.db_utils import _connect_to_db


def get_all_books():
    result = requests.get(
        'http://127.0.0.1:5001/books',
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_book_by_title(title):
    result = requests.get(
        'http://127.0.0.1:5001/title/{}'.format(title),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_book_by_author(author):
    result = requests.get(
        'http://127.0.0.1:5001/author/{}'.format(author),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_book_by_genre(genre):
    result = requests.get(
        'http://127.0.0.1:5001/genre/{}'.format(genre),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_book_by_id(book_id):
    result = requests.get(
        'http://127.0.0.1:5001/id/{}'.format(book_id),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def add_new_user(new_user_dict):
    endpoint = "http://127.0.0.1:5001/user/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_user_dict)
    )

    return result.json()

def collect_user_data(user_name):
    new_user_dict = {
        "user_name": user_name,
    }

    return new_user_dict


def get_user_by_name(user_name):
    result = requests.get(
        'http://127.0.0.1:5001/user/{}'.format(user_name),
        headers={'content-type': 'application/json'}
    )
    return result.json()

#rent a new book
def add_book_to_user_front_end(user_book_dict):
    endpoint = "http://127.0.0.1:5001/user_book/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(user_book_dict)
    )

    return result.json()

def delete_user_by_id(user_id):
    endpoint = f"http://127.0.0.1:5001/users/remove/{user_id}"
    result = requests.delete(endpoint).json()
    print("Successfully deleted. Goodbye!")
    return result


# collect data to rent a new book
def collect_book_user_data(user_name):

    rented_book = input("Enter the ID number of the book you would like to rent out: ").strip()

    # Return the collected data as a dictionary
    user_book_dict = {
        "user_name": user_name,
        "rented_book": rented_book,
    }

    return user_book_dict


def rent_book(user):

    user_name = user[0][1]

    user_book_dict = collect_book_user_data(user_name)
    add_book_to_user_front_end(user_book_dict)

    #checks for the new book
    user_book = get_user_by_name(user_name)[0][2]

    book_title = get_book_by_id(user_book)[0][1]
    book_author = get_book_by_id(user_book)[0][2]

    print("You have rented: ")
    print(f"\x1B[3m{book_title}\x1B[0m by {book_author}.")

    print("Thank you for using the library, Goodbye!")


def check_book(user):


    user_book = user[0][2]

    if user_book is not None:
        book_title = get_book_by_id(user_book)[0][1]
        book_author = get_book_by_id(user_book)[0][2]

        print("You currently have the following book rented: ")
        print(f"\x1B[3m{book_title}\x1B[0m by {book_author}.")

        return_choice = input("Would you like to return it and find a new one? (y/n): ").lower().strip()

        if return_choice == "y":
            return browsing_menu(user)

        elif return_choice == "n":
            print("Thank you! Goodbye.")
            return None

        else:
            print("Please select a valid option.")
            return browsing_menu(user)
    else:
        print("You don't currently have any books rented.")
        return browsing_menu(user)

def book_display_route(book_route, book_info):
    where = ""

    if book_route == "title":
        where = "title"


    elif book_route == "author":
        where = "author"

    elif book_route == "genre":
        where = "genre"

    elif book_route == "id":
        where = "id"

    else:
        where = ''

    return display_book_table(where, book_info)

def display_book_table(where, book_info):

    db_connection = _connect_to_db()
    cur = db_connection.cursor()
    if where == "title":
        cur.execute(f"""
                SELECT  *
                FROM books 
                WHERE title = '{book_info}'
                """)
        book_table = from_db_cursor(cur)

    if where == "author":
        cur.execute(f"""
                SELECT  *
                FROM books 
                WHERE author = '{book_info}'
                """)
        book_table = from_db_cursor(cur)

    if where == "genre":
        cur.execute(f"""
                SELECT  *
                FROM books 
                WHERE genre = '{book_info}'
                """)
        book_table = from_db_cursor(cur)

    if where == "all_books":
        cur.execute(f"""
                SELECT  *
                FROM books 
                """)
        book_table = from_db_cursor(cur)

    return print(book_table)


def main_menu(user):

    print(f"Welcome back, {user[0][1]}!")
    print("What would you like to do today?")
    print("A. Rent out a new book.")
    print("B. Check what book I have currently.")
    print("C. Delete my account.")

    main_choice = input("Enter your choice (A / B / C): ").strip().upper()
    if main_choice == "A":
        return browsing_menu(user)

    elif main_choice == "B":
       return check_book(user)

    elif main_choice == "C":
        delete_check = input("Are you sure you want to delete your account? (y/n): ").lower().strip()
        if delete_check == "y":
            return delete_user_by_id(user[0][0])
        elif delete_check == "n":
            print("Thank you! Goodbye.")
            return main_menu(user)
        else:
            print("Please select a valid option.")
            return main_menu(user)

    else:
        return print("That is not a valid choice.")

def browsing_menu(user):

    print("Here are the browsing options:")
    print("A. By title")
    print("B. By genre")
    print("C. By author")
    print("D. Browse the whole catalogue")

    browsing_choice = input("Enter your choice: (A / B / C / D) ").strip().upper()

    if browsing_choice == "A":
        title = input("Enter the title of the book: ")

        book = get_book_by_title(title)
        book_title = book[0][1]

        if book:
            print(book_display_route("title", book_title))

            rent_choice = input("Would you like to rent this book out? (y/n): ")

            if rent_choice == "y":
                return rent_book(user)

            else:
                return main_menu(user)

        else:
            print("Sorry, we do not have this book. Please try another one.")
            return browsing_menu(user)

    elif browsing_choice == "B":
        genre = input("Enter the book genre: ").strip()
        book = get_book_by_genre(genre)

        if book:
            print(book_display_route("genre", genre))

            rent_choice = input("Would you like to rent one of these books out? (y/n): ")

            if rent_choice == "y":
                return rent_book(user)

            if rent_choice == "n":
                return main_menu(user)

            else:
                print("Please select a valid option.")
                return main_menu(user)

        else:
            print("Sorry, we do not have any books in this genre. Please try another one.")
            return browsing_menu(user)

    elif browsing_choice == "C":
        author = input("Enter the book author: ").strip()
        book = get_book_by_author(author)

        if book:
            print(book_display_route("author", author))

            rent_choice = input("Would you like to rent one of these books out? (y/n): ")

            if rent_choice == "y":
                return rent_book(user)

            else:
                return main_menu(user)

        else:
            print("Sorry, we do not have any books by this author. Please try another one.")
            return browsing_menu(user)

    elif browsing_choice == "D":

        print(display_book_table("all_books", "all"))

        rent_choice = input("Would you like to rent one of these books out? (y/n): ")

        if rent_choice == "y":
            return rent_book(user)

        else:
            return main_menu(user)


    else:
        print("Please select a valid option.")
        return browsing_menu(user)


def run():
    print("Welcome to the library!")
    user_name = input("Enter your name: ").strip()

    user = get_user_by_name(user_name)

    if not user:
        print("Sorry, you don't have an account yet.")
        print("Let's make you one now.")

        new_user_dict = collect_user_data(user_name)
        (add_new_user(new_user_dict))
        user = get_user_by_name(user_name)
        print("Your account has been created.")

        return main_menu(user)

    else:
        return main_menu(user)



if __name__ == '__main__':
    run()