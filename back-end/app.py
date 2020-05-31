import os
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    Blueprint,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'random string'

# 应用使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中
# Flask-SQLAlchemy 文档还建议把 SQLALCHEMY_TRACK_MODIFICATIONS 键设为 False
# 一遍在不需要跟踪对象变化时降低内存消耗
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db 对象时 SQLAlchemy 类的实例，表示应用使用的数据库
db = SQLAlchemy(app)


class User(db.Model):
    # 数据库使用的表名
    __tablename__ = 'users'
    # 类变量都是改模型的属性，定义为 db.Column 类的实例
    id = db.Column(db.Integer, primary_key=True)
    # Flask-SQLAlchemy 要求每个模型都定义主键，这一列经常命名为 id
    # index 设为 True，为列创建索引，提升查询效率
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f'<User ({self.username})'


# 创建并注册一个 shell 上下文处理器
# flask shell 命令将自动把这些对象导入 shell
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
# app.register_blueprint(user_routes, url_prefix='/todo')


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=8088,
    )
    app.run(**config)
