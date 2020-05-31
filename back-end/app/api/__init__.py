from flask import (
    request,
    jsonify,
    url_for,
    Blueprint,
)
from ..models.user import User
from .errors import bad_request


bp = Blueprint('api', __name__)


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
    print(response)
    return response


# 写在最后是为了防止循环导入
from . import user
from . import tic
