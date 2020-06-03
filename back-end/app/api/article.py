from flask import (
    request,
    url_for,
    jsonify,
    make_response,
)
from .. import db
from ..models.article import Article
from .errors import bad_request
from . import bp


@bp.route('/article/test', methods=['GET'])
def article():
    """返回一篇文章"""
    return jsonify({'test': 'Article!'})


@bp.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    """返回一篇文章"""
    response = jsonify(Article.query.get_or_404(id).to_dict())
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/article/<int:per_page>/<int:page>', methods=['GET'])
def get_articles(per_page, page):
    """返回文章集合，分页"""
    # per_page = min(request.args.get('page_size', 10, type=int), 10)
    data = Article.to_collection_dict(Article.query, page, per_page, 'api.get_articles')
    response = jsonify(data['items'])
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response
