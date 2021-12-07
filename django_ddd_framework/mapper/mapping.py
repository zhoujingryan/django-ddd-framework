from .join import Join
from .property import Property
from .ref import Ref
from typing import List, Optional
from django_ddd_framework.types import MapType


class MappingMeta(type):
    def __new__(mcs, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, MappingMeta)]
        if not parents:
            return super().__new__(mcs, name, bases, attrs)

        # validate entity
        if not attrs.get("entity", None):
            raise ValueError(
                "no entity for metadata mapping {} is not allowed".format(name)
            )

        # validate properties
        attrs["properties"] = attrs.get("properties", [])
        if not all([isinstance(p, Property) for p in attrs["properties"]]):
            raise ValueError("mapper class {} properties type error".format(name))
        primary_key = [p for p in attrs["properties"] if p.primary_key]
        if len(primary_key) == 0:
            raise ValueError(
                "mapper class properties does not contain a primary key field"
            )
        elif len(primary_key) > 1:
            raise ValueError(
                "mapper class properties contain more than one primary key"
            )
        elif len(primary_key) == 1:
            attrs["pk"] = primary_key[0]

        # validate joins
        attrs["joins"] = attrs.get("joins", [])
        if not all([isinstance(j, Join) for j in attrs["joins"]]):
            raise ValueError("mapper class {} joins type error".format(name))

        # validate refs
        attrs["refs"] = attrs.get("refs", [])
        if not all([isinstance(r, Ref) for r in attrs["refs"]]):
            raise ValueError("mapper class {} refs type error".format(name))

        # read only field names
        read_only = [p.name for p in attrs["properties"] if p.read_only]
        attrs["read_only_fields"] = read_only

        # aggregate joins
        attrs["aggregate_joins"] = [j for j in attrs["joins"] if j.is_aggregation]

        # concrete
        concretes = []
        for j in attrs["joins"]:
            if j.join_type == Join.JoinType.ManyToOne or (
                j.join_type == Join.JoinType.OneToOne and not j.is_reverse
            ):
                concretes.append(j)
        attrs["concrete_fields"] = concretes + attrs["properties"]

        # column names
        columns = []
        for f in attrs['concrete_fields']:
            name = f.name
            if isinstance(f, Property):
                column = f.column
            elif isinstance(f, Join):
                column = f.join_key
            else:
                continue
            columns.append(column)
        attrs['column_names'] = columns

        # related fields
        related = []
        for j in attrs["joins"]:
            if j.join_type in [Join.JoinType.OneToOne, Join.JoinType.ManyToOne]:
                related.append(j)
        attrs["related_fields"] = related

        # db notation
        notations = attrs.get("DBNotation")
        if not notations:
            raise ValueError(
                "metadata mapping {} without db notation is not allowed".format(name)
            )

        new_class = super().__new__(mcs, name, bases, attrs)
        return new_class


class MetaDataMapper(metaclass=MappingMeta):
    class DBNotation:
        generic = None

    # the entity name of the declared mapper
    entity = None

    properties: List[Property] = []
    joins: List[Join] = []
    refs: List[Ref] = []

    pk_generator = None

    lookup_field = "pk"
    lookup_kwargs = {}

    @classmethod
    def get_db_notation(cls, map_type: MapType) -> Optional[str]:
        return getattr(cls.DBNotation, map_type.GENERIC.value)

    @classmethod
    def get_properties(cls) -> List[Property]:
        return cls.properties

    @classmethod
    def get_joins(cls) -> List[Join]:
        return cls.joins

    @classmethod
    def get_aggregate_joins(cls) -> List[Join]:
        return cls.aggregate_joins

    @classmethod
    def get_refs(cls) -> List[Ref]:
        return cls.refs

    @classmethod
    def get_read_only_fields(cls) -> List[str]:
        return cls.read_only_fields

    @classmethod
    def get_primary_key(cls):
        return cls.pk

    @classmethod
    def get_concrete_fields(cls):
        return cls.concrete_fields

    @classmethod
    def get_column_names(cls):
        return cls.column_names

    @classmethod
    def get_related_fields(cls):
        return cls.related_fields
