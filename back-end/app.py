import os
from app import create_app, db
from app.models.user import User
from flask_migrate import Migrate


# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app('default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    # config = dict(
    #     debug=True,
    #     host='0.0.0.0',
    #     port=8088,
    # )
    # app.run(**config)
    app.run(port=8088)
