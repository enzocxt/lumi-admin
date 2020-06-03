from flask import (
    request,
    url_for,
    jsonify,
    make_response,
)
from .errors import bad_request
from . import bp


def route_img(abbr, fname):
    basedir = "D:/Workspace/luminocity/img"
    filename = f'{basedir}/{abbr}/{fname}'
    with open(filename, 'rb') as fin:
        return fin.read()


@bp.route('/file/<string:abbr>/<string:fname>', methods=['GET'])
def get_img(abbr, fname):
    """返回图书封面图片"""
    content = route_img(abbr, fname)
    response = make_response(content)
    return response
