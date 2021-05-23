from sqlalchemy import and_
from sqlalchemy import asc, desc, func
from models import Author, Book, Publisher
from treelib import Tree
#Tree - zadanie - trzymać rekordy w strukturze drzewiastej

def get_books_by_publishers(session, ascending=True):
    if not isinstance(ascending, bool):
        raise ValueError(f'Sorting value invalid: {ascending}.')

    direction = asc if ascending else desc

    return (
        session
            .query(Publisher.name, func.count(Book.title).label("total_books"))
            .join(Publisher.books)
            .group_by(Publisher.name)
            .order_by(direction("total_books"))
    )