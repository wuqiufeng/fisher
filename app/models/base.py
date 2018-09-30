from flask_sqlalchemy import SQLAlchemy as _SQLAlcmemy, BaseQuery
from sqlalchemy import SmallInteger, Column, Integer
from contextlib import contextmanager
from datetime import datetime
# from app.libs.error_code import NotFound
from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlcmemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):

    def filter_by(self, **kwargs):
        if 'status' not in kwargs:
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


    # def get_or_404(self, ident):
    #     rv = self.get(ident)
    #     if not rv:
    #         raise NotFound()
    #     return rv
    #
    # def first_or_404(self):
    #     rv = self.first()
    #     if not rv:
    #         raise NotFound()
    #     return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 对象字典化
    def __getitem__(self, item):
        return getattr(self, item)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0

    def keys(self):
        return self.fields

    # 隐藏key
    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self