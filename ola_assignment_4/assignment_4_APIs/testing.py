from unittest import TestCase, main
from main import get_user_by_name, get_book_by_id, get_book_by_author, book_return_endpoint


class TestGetUserByName(TestCase):

    def test_existing_user(self):
        expected = 'Bob'
        actual = get_user_by_name("Bob")[0][1]
        self.assertEqual(expected, actual)

    def test_nonexisting_user(self):
        expected = []
        actual = get_user_by_name("mockname")
        self.assertEqual(expected, actual)

class TestGetBookById(TestCase):

    def test_existing_book(self):
        expected = 1
        actual = get_book_by_id(1)[0][0]
        self.assertEqual(expected, actual)

    def test_nonexisting_book(self):
        expected = []
        actual = get_book_by_id(18)
        self.assertEqual(expected, actual)

class TestGetBookByAuthor(TestCase):

    def test_existing_book(self):
        expected = 'Ocean Vuong'
        actual = get_book_by_author("Ocean Vuong")[0][2]
        self.assertEqual(expected, actual)

    def test_nonexisting_book(self):
        expected = []
        actual = get_book_by_author("mock name")
        self.assertEqual(expected, actual)

class TestRentingBook(TestCase):
    def test_return_book(self):
        expected = []
        actual = book_return_endpoint(2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()