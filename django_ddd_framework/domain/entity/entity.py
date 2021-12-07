from .meta import EntityMeta


class Entity(metaclass=EntityMeta):
    """the base domain entity class"""

    class Meta:
        abstract = True
        mapper = None

    def __init__(self, *args, **kwargs):
        meta = self._meta

        if getattr(meta, "abstract", False):
            raise TypeError("abstract entity cannot be instantiated")

        # fields = meta.field_meta
        # for field in fields.keys():
        #     val = kwargs.get(field, None)
        #     setattr(self, field, val)
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def pk(self):
        return getattr(self, self._meta.mapper.get_primary_key().name)

    @classmethod
    def get_mapper_class(cls):
        return cls._meta.mapper

    # @classmethod
    # def bind_mapper(cls, metadata_cls):
    #     is_abstract = cls._meta.is_abstract
    #
    #     setattr(cls._meta, "mapper", metadata_cls)

    @property
    def DAO(self):
        from django_ddd_framework.dao.entity_dao import EntityDAO

        return EntityDAO(self.__class__).create(self)

    @property
    def factory(self):
        from django_ddd_framework.factory import Factory

        return Factory(self.__class__)
