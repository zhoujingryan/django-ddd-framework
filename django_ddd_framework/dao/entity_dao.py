from django_ddd_framework.mapper import Property, Join
from typing import Dict


class EntityDAO:
    class Meta:
        klass = None
        columns = []

    def __init__(self, entity_cls):
        self.Meta.klass = entity_cls
        self.Meta.columns = entity_cls.get_mapper_class().get_column_names()

    def create(self, entity):
        """entity -> DAO"""
        fields = entity.get_mapper_class().get_concrete_fields()
        for f in fields:
            name = f.name
            if isinstance(f, Property):
                column = f.column
                value = getattr(entity, name, None)
            elif isinstance(f, Join):
                column = f.join_key
                joined_entity = getattr(entity, name, None)
                value = getattr(joined_entity, "pk", None)
            else:
                continue
            setattr(self, column, value)
        return self

    def load(self, data: Dict):
        """python primitive data type -> DAO"""
        for c in self.Meta.columns:
            setattr(self, c, data.get(c))
        return self

    def get_class(self):
        """get the entity class for this DAO"""
        return self.Meta.klass

    def to_dict(self):
        res = {}
        for field_name in self.Meta.columns:
            res[field_name] = getattr(self, field_name, None)
        return res
