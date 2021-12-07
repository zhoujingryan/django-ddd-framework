from django_ddd_framework.domain import fields, Entity
from ..mapper.commodity import CommodityMapper


class Commodity(Entity):
    id = fields.IntegerField()
    name = fields.CharField()
    sales_price = fields.IntegerField()

    class Meta:
        mapper = CommodityMapper
