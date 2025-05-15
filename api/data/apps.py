import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Apps(SqlAlchemyBase):
    __tablename__ = 'apps'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    approve = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    image_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    app_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    seen = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)