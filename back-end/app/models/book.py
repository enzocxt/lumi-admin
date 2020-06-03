import datetime
from flask import (
    url_for,
)
from app import db
from . import PaginatedAPIMixin


class Book(PaginatedAPIMixin, db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Float)
    abbr = db.Column(db.String(128))
    tag = db.Column(db.String(128))
    title = db.Column(db.String(128))
    subtitle = db.Column(db.String(128))
    author = db.Column(db.String(128))
    compile = db.Column(db.String(128))
    interpreter = db.Column(db.String(128))
    publish_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    overprint_date = db.Column(db.String(128))
    num_of_volumes = db.Column(db.String(128))
    language = db.Column(db.String(128))
    binding_style = db.Column(db.String(128))
    size = db.Column(db.String(128))
    num_of_pages = db.Column(db.Integer)
    num_of_bw_images = db.Column(db.Integer)
    num_of_color_images = db.Column(db.Integer)
    ISBN = db.Column(db.String(128))
    price = db.Column(db.Float)
    abstract = db.Column(db.Text)
    info_of_author = db.Column(db.Text)
    remark = db.Column(db.String(128))
    cid = db.Column(db.Integer)

    @classmethod
    def find_by(cls, **kwargs):
        ...

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data

    def __repr__(self):
        return f'<Book ({self.title})>'
