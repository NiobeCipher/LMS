import json

from Databases import Databases




class Books:
    def __init__(self):
        self.database = Databases()
        self.book = None
        self.all_books = self.database.load_books()

    def add(self, book):
        self.book = book
        self.add_if_existed()

    def add_if_existed(self):
        for book in self.all_books['all_books']:
            if self.book['isbn'] == book['isbn']:
                book['quantity'] += 1
        self.database.save_books(self.all_books)
