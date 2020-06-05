import re
from flask import (
    request,
    url_for,
    jsonify,
    make_response,
)
from .. import db
from ..models.user import User
from ..models.menu import AdminMenu, AdminRole
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
    # 这里没有 id 信息
    db.session.add(u)
    db.session.commit()
    # 由于 id 是 primary key，数据库自动会添加 id 数据，应该是 autoincrement
    # print(u.to_dict())
    response = jsonify(u.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('api.get_user', id=u.id)
    return response


@bp.route('/menu', methods=['GET'])
def get_menu():
    # print(request.environ['HTTP_ORIGIN'])
    username = 'admin'  # current_user()
    menus = AdminMenu.get_menus(username)
    data = [m.to_dict() for m in menus]
    response = jsonify(data)
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/authentication', methods=['GET'])
def authenticate():
    response = jsonify({
        'data': 'auth success'
    })
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/user', methods=['POST'])
def create_user():
    """注册一个新用户"""
    ...


@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    """返回一个用户"""
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/admin/user', methods=['GET', 'PUT'])
def get_users():
    """返回用户集合，分页"""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 10)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    response = jsonify(data['items'])
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response


@bp.route('/admin/role', methods=['GET'])
def get_roles():
    """返回用户角色，分页"""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 10)
    data = AdminRole.to_collection_dict(AdminRole.query, page, per_page, 'api.get_roles')
    response = jsonify(data['items'])
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    return response
