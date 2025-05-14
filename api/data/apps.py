import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Apps(SqlAlchemyBase):
    __tablename__ = 'apps'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    app_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    app_seen = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)