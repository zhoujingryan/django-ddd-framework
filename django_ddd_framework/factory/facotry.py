from typing import Dict, Any, List

# from django_ddd_framework.utils import entity_to_dict
from django_ddd_framework.mapper import Join, Property
from django_ddd_framework.typing import EntityIns

# class GenericFactory:
#     def __init__(self, entity_cls: EntityClass):
#         self.entity_cls = entity_cls
#         print(entity_cls)
#
#     def load(self, **kwargs) -> EntityIns:
#         """python primitive data type -> domain object Entity"""
#         field_meta = self.entity_cls.Meta.field_meta
#         properties = self.entity_cls.Meta.mapper.get_properties()
#         joins = self.entity_cls.Meta.mapper.get_joins()
#         print(joins)
#         # todo: refs
#
#         entity = self.entity_cls()
#         for p in properties:
#             field_type = field_meta.get(p.name)
#             if p.name in kwargs:
#                 setattr(entity, p.name, field_type.to_internal_value(kwargs[p.name]))
#
#         # build all join keys according to join mapper
#         print(field_meta)
#         print(self.entity_cls.__name__)
#         print('->', [j.name for j in joins])
#         for j in joins:
#             print(j.name)
#             entity_field = field_meta.get(j.name)
#             if not entity_field.many:
#                 val = GenericFactory(j.join_class).load(**kwargs[j.name])
#             else:
#                 val = []
#                 data_list = kwargs[j.name]
#                 if not isinstance(data_list, list):
#                     raise ValueError(
#                         "data type of field {} is {}, expect list".format(
#                             j.name, type(data_list)
#                         )
#                     )
#                 for data in data_list:
#                     print(data)
#                     val.append(GenericFactory(j.join_class).load(**data))
#
#             setattr(entity, j.name, val)
#         return entity
#
#     def dump(self, entity: EntityIns) -> Dict[str, Any]:
#         """python primitive data type <- domain object Entity"""
#         return entity_to_dict(entity)


class Factory:
    def __new__(cls, *args, **kwargs):
        entity_cls = kwargs.get("entity_cls")
        cls.entity_cls = entity_cls
        return super().__new__(cls)

    @classmethod
    def create(cls, ):

        pass

    @classmethod
    def rebuild(cls, daos) -> List[EntityIns]:
        """rebuild a list of entity by dao"""
        assert all([d.get_class() == cls.entity_cls for d in daos]), "rebuild different DAO type is not allowed"
        res = []
        for d in daos:
            # set the concrete fields for entity
            args = d.to_dict()
            entity = cls.entity_cls(**args)

            res.append(entity)
        return res

    @classmethod
    def aggregates(cls, entity):
        """get all aggregates joined entity for the given entity"""

        def build_aggrs(entity_ins):
            if entity_ins is None:
                return
            res.append(entity_ins)
            mapper_cls = entity_ins.get_mapper_class()
            aggr_joins = mapper_cls.get_aggregate_joins()
            for j in aggr_joins:
                join_type = j.join_type
                name = j.name
                if join_type == Join.JoinType.OneToMany:
                    for e in getattr(entity_ins, name, []):
                        build_aggrs(e)
                elif join_type in (Join.JoinType.ManyToOne, Join.JoinType.OneToOne):
                    build_aggrs(getattr(entity_ins, name, None))

        res = []
        build_aggrs(entity)
        return res
