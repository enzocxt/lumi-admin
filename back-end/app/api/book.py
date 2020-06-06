from flask import (
    request,
    url_for,
    jsonify,
    make_response,
)
from .. import db
from ..models.book import Book, Category
from .errors import bad_request
from . import bp


@bp.route('/book/test', methods=['GET'])
def book():
    """返回图书测试"""
    return jsonify({'test': 'Book!'})


def add_category(category, book):
    book['category'] = {
        'id': book['cid'],
        'name': category[book['cid']],
    }


@bp.route('/books', methods=['GET'])
def get_books():
    """返回所有图书"""
    categories = [c.to_dict() for c in Category.query.all()]
    category = {c['id']: c['name'] for c in categories}
    books = [b.to_dict() for b in Book.query.all()]
    for b in books:
        add_category(category, b)
    response = jsonify(books)
    return response


@bp.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    """返回一本图书"""
    response = jsonify(Book.query.get_or_404(id).to_dict())
    return response


@bp.route('/book/<int:per_page>/<int:page>', methods=['GET'])
def get_books_page(per_page, page):
    """返回文章集合，分页"""
    data = Book.to_collection_dict(Book.query, page, per_page, 'api.get_books_page')
    response = jsonify(data['items'])
    return response


@bp.route('/category/<int:cid>/books', methods=['GET'])
def get_books_of_category(cid):
    categories = [c.to_dict() for c in Category.query.all()]
    category = {c['id']: c['name'] for c in categories}
    books = Book.query.filter_by(cid=cid).all()
    books = [b.to_dict() for b in books]
    for b in books:
        add_category(category, b)
    response = jsonify(books)
    return response
