from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from flask import (
    url_for,
)
from app import db


class User(db.Model):
    # 数据库使用的表名
    __tablename__ = 'users'
    # 类变量都是改模型的属性，定义为 db.Column 类的实例
    id = db.Column(db.Integer, primary_key=True)
    # Flask-SQLAlchemy 要求每个模型都定义主键，这一列经常命名为 id
    # index 设为 True，为列创建索引，提升查询效率
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.password = data['password']

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            # '_links': {
            #     'self': url_for('api.get_user', id=self.id)
            # }
        }
        if include_email:
            data['email'] = self.email
        return data

    def __repr__(self):
        return f'<User ({self.username})>'
