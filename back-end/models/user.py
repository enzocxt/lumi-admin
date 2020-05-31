from app import db


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
