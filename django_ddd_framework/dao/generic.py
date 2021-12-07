from django.apps import apps
from django.forms.models import model_to_dict
from typing import List, Any

from django_ddd_framework.typing import EntityIns, EntityClass
from django_ddd_framework.types import MapType
from django_ddd_framework.exceptions import DataIntegrityError, DataAccessError
from django_ddd_framework.dao.entity_dao import EntityDAO
from django_ddd_framework.factory import Factory
from .base import BaseDao


class GenericDao(BaseDao):
    """generic DAO implements for single entity"""

    @classmethod
    def create(cls, entity: EntityIns):
        mapper_cls = entity.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        dao = EntityDAO(entity.__class__).create(entity)
        args = dao.to_dict()
        try:
            model.objects.create(**args)
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def bulk_create(cls, entities: List[EntityIns]):
        if not entities:
            return
        mapper_cls = entities[0].get_mapper_class()
        entity_cls = entities[0].__class__
        daos = [EntityDAO(entity_cls).create(e) for e in entities]
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        creates = []
        for d in daos:
            creates.append(model(**d.to_dict()))
        try:
            model.objects.bulk_create(creates)
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def update(cls, entity: EntityIns):
        mapper_cls = entity.get_mapper_class()
        pk_field = mapper_cls.get_primary_key()
        dao = EntityDAO(entity.__class__).create(entity)
        args = dao.to_dict()
        args.pop(pk_field.name)
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        try:
            ins = model.objects.get(pk=entity.pk)
            for c in mapper_cls.get_column_names():
                old_val = getattr(ins, c, None)
                new_val = getattr(dao, c, None)
                if old_val != new_val:
                    setattr(ins, c, new_val)
            ins.save()
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def bulk_update(cls, entities: List[EntityIns]):
        if not entities:
            return
        pk_list = [e.pk for e in entities]
        entity_cls = entities[0].__class__
        repo_entities = cls.load_many(entity_cls, pk_list)
        mapper_cls = entity_cls.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        columns = mapper_cls.get_column_names()
        model = apps.get_model(db_notation)
        dao_dict = {e.pk: EntityDAO(entity_cls).create(e) for e in entities}
        updates = []
        fields = set()
        for ins in repo_entities:
            entity = dao_dict.get(ins.pk)
            should_updated = False
            for c in columns:
                new_val = getattr(entity, c, None)
                old_val = getattr(ins, c, None)
                if old_val != new_val:
                    should_updated = True
                    fields.add(c)
                    setattr(ins, c, new_val)
            if should_updated:
                updates.append(ins)
        try:
            model.objects.bulk_update(updates, fields)
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def delete(cls, entity: EntityIns):
        entity_cls = entity.__class__
        mapper_cls = entity_cls.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        try:
            ins = model.objects.get(pk=entity.pk)
            ins.delete()
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def bulk_delete(cls, entities: List[EntityIns]):
        pk_list = [e.pk for e in entities]
        entity_cls = entities[0].__class__
        mapper_cls = entity_cls.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        try:
            model.objects.filter(pk__in=pk_list).delete()
        except Exception as e:
            raise DataIntegrityError(e)    # pragma: no cover

    @classmethod
    def load(cls, entity_class: EntityClass, pk: Any) -> EntityIns:
        mapper_cls = entity_class.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        try:
            obj = model.objects.get(pk=pk)
        except Exception as e:
            raise DataAccessError(e)    # pragma: no cover
        data = model_to_dict(obj)
        dao = EntityDAO(entity_class).load(data)
        entities = Factory(entity_cls=entity_class).rebuild([dao])
        return entities[0]

    @classmethod
    def load_many(cls, entity_class: EntityClass, pks: List[Any]) -> List[EntityIns]:
        mapper_cls = entity_class.get_mapper_class()
        db_notation = mapper_cls.get_db_notation(MapType.GENERIC)
        model = apps.get_model(db_notation)
        try:
            objs = list(model.objects.filter(pk__in=pks))
        except Exception as e:
            raise DataAccessError(e)    # pragma: no cover
        daos = [EntityDAO(entity_class).load(model_to_dict(obj)) for obj in objs]
        result = Factory(entity_cls=entity_class).rebuild(daos)
        return result
