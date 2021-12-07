from django_ddd_framework.domain import Entity
from django_ddd_framework.repository import GenericRepository


class GenericService:
    entity: Entity = None
    repository_class: GenericRepository = None
