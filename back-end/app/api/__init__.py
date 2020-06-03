from flask import (
    request,
    jsonify,
    url_for,
    Blueprint,
)
from ..models.user import User
from .errors import bad_request


bp = Blueprint('api', __name__)


# 写在最后是为了防止循环导入
from . import user
from . import article
from . import book
from . import static
from . import tic
