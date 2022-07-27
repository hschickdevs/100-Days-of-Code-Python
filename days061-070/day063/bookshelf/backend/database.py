from sqlite3 import connect
import os
# from flask_sqlalchemy
from flask import Flask

DB_PATH = os.path.join(os.path.dirname(__file__), 'books-library.sqlite')

class LibraryDatabase:
    def __init__(self):
        self.db = connect(DB_PATH, check_same_thread=False)
        self.cursor = self.db.cursor()
        
    def add_book(self, id: int, title: str, author: str, rating: int, icon_url: str = None) -> None:
        """
        The add_book function adds a book to the database.
        It takes the name, author, rating, and icon_url of the book as arguments and returns nothing.
        
        :param name: The name of the book
        :param author: The author of the book
        :param rating: The rating of the book
        :param icon_url: The URL of the icon of the book
        :return: None
        """
        self.cursor.execute(f'INSERT INTO books VALUES({id}, "{title}", "{author}", {rating}, "{icon_url}")')
        self.db.commit()
        
    def remove_book(self, id: int) -> None:
        """
        The remove_book function removes a book from the database.
        It takes the id of the book as an argument and returns nothing.
        
        :param id: The id of the book
        :return: None
        """
        self.cursor.execute(f'DELETE FROM books WHERE id = {id}')
        self.db.commit()
        
    def update_book(self, id: int, name: str, author: str, rating: int, icon_url: str = None) -> None:
        """
        The update_book function updates a book in the database.
        It takes the id, name, author, rating, and icon_url of the book as arguments and returns nothing.
        
        :param id: The id of the book
        :param name: The name of the book
        :param author: The author of the book
        :param rating: The rating of the book
        :param icon_url: The URL of the icon of the book ('None' STRING if no icon URL)
        :return: None
        """
        self.cursor.execute(f'UPDATE books SET title = "{name}", author = "{author}", rating = {rating}, icon_url = "{icon_url}" WHERE id = {id}')
        self.db.commit()
        
    def load_books(self, id: int = None) -> list[dict]:
        """
        The load_books function loads books from the database.
        It takes no arguments and returns a list of books.
        
        :param self: Access the attributes and methods of the class in python
        :return: A list of book dictionaries
            - id: Primary key of the book
            - name: The name of the book
            - author: The author of the book
            - rating: The rating of the book
            - icon_url: The URL of the icon of the book ('None' STRING if no icon URL)
        """
        if id is None:
            self.cursor.execute("SELECT * FROM books")
        else:
            self.cursor.execute(f"SELECT * FROM books WHERE id = {id}")
            
        column_names = [column[0] for column in self.cursor.description]
        return [{column_names[i]: v for i, v in enumerate(book)} for book in self.cursor.fetchall()]
    
    def _get_column_names(self) -> list[str]:
        """
        The _get_column_names function returns the column names of the database.
        It takes no arguments and returns a list of column names.
        
        :param self: Access the attributes and methods of the class in python
        :return: A list of column names
        """
        self.cursor.execute("SELECT * FROM books")
        return [column[0] for column in self.cursor.description]
        
    def _create_table(self):
        """
        The _create_table function creates a table in the database.
        It takes no arguments and returns nothing.
        
        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating INTEGER NOT NULL, icon_url varchar(250))")


if __name__ == "__main__":
    db = LibraryDatabase()
    # db._create_table()
    # db.add_book("Harry Potter", "JK Rowling", 9)
    print(db.load_books())
    