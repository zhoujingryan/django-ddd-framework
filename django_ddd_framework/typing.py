from typing import Type, ClassVar
from django_ddd_framework.domain import Entity
from django_ddd_framework.mapper import MetaDataMapper
from django_ddd_framework.dao.entity_dao import EntityDAO


__all__ = ["EntityIns", "EntityClass", "MapperClass", "DAOIns", "DAOClass"]


EntityClass = ClassVar[Entity]
EntityIns = Type[Entity]

MapperClass = ClassVar[MetaDataMapper]

DAOIns = Type[EntityDAO]
DAOClass = ClassVar[EntityDAO]
