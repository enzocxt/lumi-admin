from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from flask import (
    url_for,
)
from app import db
from . import PaginatedAPIMixin
from .user import User


class AdminMenu(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_menu'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(128))
    name = db.Column(db.String(128))
    name_zh = db.Column(db.String(128))
    icon_cls = db.Column(db.String(128))
    component = db.Column(db.String(128))
    parent_id = db.Column(db.Integer)
    # 获取当前登录用户的 id
    # 根据用户 id 查询出该用户对应所有角色的 id
    # 根据这些角色的 id，查询出所有可访问的菜单项
    # 根据 parent_id 把子菜单放进父菜单对象中，整理返回具有正确层级关系的菜单数据

    @classmethod
    def get_menus(cls, username):
        # 获取当前用户
        u = User.query.filter_by(username=username).first()
        # 获取当前用户对应的所有角色的 id 列表
        roles = AdminUserRole.query.filter_by(uid=u.id).all()
        # print('roles:', len(roles))
        rids = [r.rid for r in roles]
        # 查询出这些角色对应的所有菜单项
        mids = []
        for rid in rids:
            rms = AdminRoleMenu.query.filter_by(rid=rid).all()
            # print('role menu:', len(rms))
            mids.extend([rm.mid for rm in rms])
        mids = list(set(mids))
        # print('menu ids:', mids)
        menus = []
        for mid in mids:
            menu = AdminMenu.query.filter_by(id=mid).first()
            menus.append(menu)
        # 处理菜单项结构
        menus = cls.handle_menus(menus)
        return menus

    @classmethod
    def handle_menus(cls, menus):
        for m in menus:
            children = AdminMenu.query.filter_by(parent_id=m.id).all()
            if len(children) > 0:
                m.children = children
        menus = [m for m in menus if m.parent_id == 0]
        return menus

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        if 'children' in data:
            data['children'] = [d.to_dict() for d in data['children']]
        return data


class AdminRole(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    name_zh = db.Column(db.String(128))
    enabled = db.Column(db.Integer)

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data


class AdminRoleMenu(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_role_menu'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer)
    mid = db.Column(db.Integer)

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data


class AdminUserRole(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_user_role'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    rid = db.Column(db.Integer)

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data


class AdminPermission(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_permission'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    desc_ = db.Column(db.String(128))
    url = db.Column(db.String(128))

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data


class AdminRolePermission(PaginatedAPIMixin, db.Model):
    __tablename__ = 'admin_role_permission'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer)
    pid = db.Column(db.Integer)

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data
