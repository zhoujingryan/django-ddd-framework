from typing import List, Any, Optional
from collections import defaultdict

from ..dao import BaseDao
from django_ddd_framework.typing import EntityIns, EntityClass
from django.db import transaction


class GenericRepository(BaseDao):

    @classmethod
    def create(cls, entity: EntityIns):
        pass

    @classmethod
    def bulk_create(cls, entities: List[EntityIns]):
        pass

    @classmethod
    def update(cls, entity: EntityIns):
        pass

    @classmethod
    def bulk_update(cls, entities: List[EntityIns]):
        pass

    @classmethod
    def delete(cls, entity: EntityIns):
        pass

    @classmethod
    def bulk_delete(cls, entities: List[EntityIns]):
        pass

    @classmethod
    def load(cls, entity_class: EntityClass, pk: Any) -> EntityIns:
        pass

    @classmethod
    def load_many(cls, entity_class: EntityClass, pks: List[Any]) -> List[EntityIns]:
        pass
