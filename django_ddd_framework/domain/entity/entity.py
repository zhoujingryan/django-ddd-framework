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
