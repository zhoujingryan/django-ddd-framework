from ..typing import EntityIns
from typing import Any, Dict, List
from ..domain import fields
from collections import defaultdict
from django_ddd_framework.mapper import Join


def entity_to_dict(entity: EntityIns) -> Dict[Any, Dict]:
    """python primitive data type <- domain object Entity"""
    if not entity:
        return {}
    entity_cls = entity.__class__
    field_meta = entity_cls.Meta.field_meta

    res = {}
    for field_name, field in field_meta.items():
        if isinstance(field, fields.EntityField):
            if field.many:
                val = []
                for elem in getattr(entity, field_name, []):
                    val.append(entity_to_dict(elem))
            else:
                val = entity_to_dict(getattr(entity, field_name, None))
        else:
            val = getattr(entity, field_name, None)
        res[field_name] = val
    return res


def _get_dao_map(entity: EntityIns, result: Dict, is_aggregation: bool = False):
    if entity is None:
        return

    entity_cls = entity.__class__
    field_meta = entity_cls.Meta.field_meta
    properties = entity_cls.Meta.mapper.get_properties()
    joins = (
        entity_cls.Meta.mapper.get_joins()
        if not is_aggregation
        else entity_cls.Meta.mapper.get_aggregate_joins()
    )

    data = {}
    for p in properties:
        val = getattr(entity, p.name)
        data[p.column] = val

    for j in joins:
        field = field_meta[j.name]
        if field.many:
            for elem in getattr(entity, j.name, []):
                _get_dao_map(elem, result, is_aggregation)
        else:
            ent = getattr(entity, j.name, None)
            _get_dao_map(ent, result, is_aggregation)
            if j.join_type in [Join.JoinType.ManyToOne, Join.JoinType.OneToOne]:
                data[j.join_key] = getattr(ent, "pk")

    if data:
        result[entity_cls].append(data)


def entity_to_dao(entities: List[EntityIns]) -> Dict[Any, List[Dict[str, Any]]]:
    """according to mapper, transfer a list of entities into its DAO representation classified by entity class name"""

    res = defaultdict(list)
    for e in entities:
        _get_dao_map(e, res)
    return res


def aggregate_to_dao(entities: List[EntityIns]) -> Dict[Any, List[Dict[str, Any]]]:
    """
    according to mapper
    transfer a list of aggregation entities into its DAO representation
    classified by entity class name
    """
    res = defaultdict(list)
    for e in entities:
        _get_dao_map(e, res, is_aggregation=True)
    return res
