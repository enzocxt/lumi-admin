from flask import (
    request,
    url_for,
    jsonify,
    make_response,
)
from .. import db
from ..models.book import Book
from .errors import bad_request
from . import bp


@bp.route('/book/test', methods=['GET'])
def book():
    """返回图书测试"""
    return jsonify({'test': 'Book!'})


@bp.route('/books', methods=['GET'])
def get_books():
    """返回所有图书"""
    response = jsonify([b.to_dict() for b in Book.query.all()])
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    """返回一篇文章"""
    response = jsonify(Book.query.get_or_404(id).to_dict())
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/article/<int:per_page>/<int:page>', methods=['GET'])
def get_books_page(per_page, page):
    """返回文章集合，分页"""
    data = Book.to_collection_dict(Book.query, page, per_page, 'api.get_books_page')
    response = jsonify(data['items'])
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response
