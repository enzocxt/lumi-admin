from . import bp


@bp.route('/user', methods=['POST'])
def create_user():
    """注册一个新用户"""
    ...


@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    """返回一个用户"""
    # return jsonify(User.query.get_or_404(id).to_dict())
    ...
