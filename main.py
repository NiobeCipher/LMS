import Interactions
from Books import Books

interaction = Interactions.Interactions()

if __name__ == '__main__':
    book = Books()
    book.add({'title': 'Title', 'author': 'Author', 'pub': 'Pub', 'year': 2017, 'isbn': 0, 'quantity': 1})
