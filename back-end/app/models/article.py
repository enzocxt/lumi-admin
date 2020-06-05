import datetime
from flask import (
    url_for,
)
from app import db
from . import PaginatedAPIMixin


class Article(PaginatedAPIMixin, db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(128))
    article_content_md = db.Column(db.Text)
    article_content_html = db.Column(db.Text)
    article_abstract = db.Column(db.String(128))
    article_cover = db.Column(db.String(128))
    article_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def find_by(cls, **kwargs):
        ...

    def from_dict(self, data):
        attrmap = {
            'id': 'id',
            'articleTitle': 'article_title',
            'articleContentMd': 'article_content_md',
            'articleContentHtml': 'article_content_html',
            'articleAbstract': 'article_abstract',
            'articleCover': 'article_cover',
            'articleDate': 'article_date',
        }
        for field in attrmap:
            if field in data:
                setattr(self, attrmap[field], data[field])

    def to_dict(self):
        data = self.__dict__.copy()
        del data['_sa_instance_state']
        return data

    def __repr__(self):
        return f'<Article ({self.article_title})>'
