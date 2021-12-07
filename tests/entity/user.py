from django_ddd_framework.domain import fields, Entity
from django_ddd_framework.mapper import MetaDataMapper, Property
from ..ddd.utils import uuid_gen


class UserMetaDataMapper(MetaDataMapper):
    class DBNotation:
        generic = "ddd.UserModel"

    pk_generator = uuid_gen

    properties = [
        Property(name="id", column="id", primary_key=True),
        Property(name="username", column="username"),
    ]


class User(Entity):
    id = fields.CharField()
    username = fields.CharField()
