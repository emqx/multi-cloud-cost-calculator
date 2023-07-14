from flask import jsonify, Blueprint

base_api_bp = Blueprint('base_api_bp', __name__)


@base_api_bp.route('/hello')
def hello():
    return jsonify({'msg': 'hello'})
