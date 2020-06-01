import re
from flask import (
    request,
    url_for,
    jsonify,
)
from .. import db
from ..models.user import User
from .errors import bad_request
from . import bp


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data!')

    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    if 'password' not in data or not data.get('password', None):
        message['password'] = 'Please provide a valid password.'

    u = User.query.filter_by(username=data['username']).first()
    if u is None:
        message['username'] = 'User ({}) does not exist!'.format(data['username'])
    if len(message) > 0:
        return bad_request(message)

    response = jsonify(u.to_dict())
    if u.verify_password(data['password']):
        response.status_code = 200
    return response


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data!')

    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    if 'password' not in data or not data.get('password', None):
        message['password'] = 'Please provide a valid password.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'

    if User.query.filter_by(username=data['username']).first():
        message['username'] = 'Please use a different username.'
    if User.query.filter_by(email=data.get('email', None)).first():
        message['email'] = 'Please use a different email address.'
    if len(message) > 0:
        return bad_request(message)

    u = User()
    u.from_dict(data, new_user=True)
    db.session.add(u)
    db.session.commit()
    response = jsonify(u.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('api.get_user', id=u.id)
    return response


@bp.route('/user', methods=['POST'])
def create_user():
    """注册一个新用户"""
    ...


@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    """返回一个用户"""
    return jsonify(User.query.get_or_404(id).to_dict())
