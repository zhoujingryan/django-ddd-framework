import abc
from django_ddd_framework.typing import EntityIns, EntityClass
from typing import List, Any


class BaseDao(metaclass=abc.ABCMeta):
    """interface of DAO"""

    @classmethod
    @abc.abstractmethod
    def create(cls, entity: EntityIns):
        pass

    @classmethod
    @abc.abstractmethod
    def bulk_create(cls, entities: List[EntityIns]):
        pass

    @classmethod
    @abc.abstractmethod
    def update(cls, entity: EntityIns):
        pass

    @classmethod
    @abc.abstractmethod
    def bulk_update(cls, entities: List[EntityIns]):
        pass

    @classmethod
    @abc.abstractmethod
    def delete(cls, entity: EntityIns):
        pass

    @classmethod
    @abc.abstractmethod
    def bulk_delete(cls, entities: List[EntityIns]):
        pass

    @classmethod
    @abc.abstractmethod
    def load(cls, entity_class: EntityClass, pk: Any) -> EntityIns:
        pass

    @classmethod
    @abc.abstractmethod
    def load_many(cls, entity_class: EntityClass, pks: List[Any]) -> List[EntityIns]:
        pass
