from flask import (
    Blueprint,
)


# 构造函数有两个必须制定的参数：名称 和 蓝本所在的包或模块
main = Blueprint('main', __name__)

# 避免循环导入依赖
from . import (
    views,
    errors,
)
