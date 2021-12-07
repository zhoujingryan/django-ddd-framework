from ..fields import Field


class EntityMeta(type):
    """metaclass of all entity"""

    def __new__(cls, name, bases, attrs, **kwargs):
        parents = [b for b in bases if isinstance(b, EntityMeta)]
        if not parents:
            return super().__new__(cls, name, bases, attrs, **kwargs)

        module = attrs.pop("__module__")
        new_attrs = {"__module__": module}
        field_meta = {}
        for obj_name, obj in attrs.items():
            new_attrs[obj_name] = obj
            if isinstance(obj, Field):
                field_meta[obj_name] = obj

        new_class = super().__new__(cls, name, bases, new_attrs, **kwargs)

        meta = getattr(new_class, "Meta", None)
        setattr(new_class, "_meta", meta)
        setattr(meta, "field_meta", field_meta)
        is_abstract = getattr(meta, "abstract", False)
        mapper_class = getattr(meta, "mapper", None)
        if is_abstract and mapper_class:
            raise TypeError(
                "abstract entity class {} should not bind the mapper {}".format(
                    new_class.__name__, mapper_class.__name__
                )
            )
        elif not is_abstract and not mapper_class:
            raise TypeError(
                "entity class {} has no mapper class".format(new_class.__name__)
            )
        return new_class
