from flask import jsonify
from . import bp


@bp.route('/tic', methods=['GET'])
def tic():
    """前端 Vue.js 用来测试与后端 Flask API 的连通性"""
    return jsonify('Tac!')
