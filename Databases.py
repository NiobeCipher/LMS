import json


class Databases:
    def __init__(self):
        self.json_books_path = 'data/books.json'

    def load_books(self):
        with open(self.json_books_path, 'r') as f:
            return json.load(f)

    def save_books(self, books):
        with open(self.json_books_path, 'w') as f:
            json.dump(books, f)
