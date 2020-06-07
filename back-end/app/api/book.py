import os
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


@bp.route('/book/<string:abbr>/imgs', methods=['GET'])
def get_book_imgs(abbr):
    """返回一本图书的所有图片（不包括封面）"""
    # 从所有图书文件夹中找到图书缩写 abbr 对应的图书文件夹
    # 然后从该文件夹中取出所有图片的文件名（不包括封面图片）
    apidir = "http://localhost:8088/api/file"
    basedir = "D:/Workspace/luminocity/img"
    bookdir = f'{basedir}/{abbr}'
    fnames = os.listdir(bookdir)
    fnames = [fn for fn in fnames if fn.endswith('.jpg')]
    fnames = [f'{apidir}/{abbr}/{fn}' for fn in fnames[1:]]
    response = jsonify(fnames)
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
