from flask import (
    request,
    Blueprint,
)
from ..models.user import User


bp = Blueprint('api', __name__)


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    u = User.query.filter_by(username=data['username']).first()
    if u.verify_password(data['password']):
        return 
    return 'Hello'


# 写在最后是为了防止循环导入
from . import user
from . import tic
