from flask import (
    Flask,
    render_template,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from config import config
from config import DevelopmentConfig as Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config.from_object(Config)

    # Enable CORS
    # enable 'Access-Control-Allow-Credentials'
    # 相当于在路由函数末尾加上如下两行（response headers 添加字段）
    # response.headers['Access-Control-Allow-Credentials'] = 'true'
    # response.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    CORS(app, supports_credentials=True)
    # Init Flask-SQLAlchemy
    db.init_app(app)
    # Init Flask-Migrate
    migrate.init_app(app, db)

    # 添加路由和自定义的错误页面
    from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    from .api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
